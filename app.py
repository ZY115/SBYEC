"""
SBYEC Chatbot for Hugging Face Spaces
Tiered retrieval: rule-based first, Groq LLM only when needed.
"""

import os
import re
import gradio as gr
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# --- Tier 1: Rule-based extraction (no LLM, no API calls) ---

# Patterns for structured info extraction
CONTACT_PATTERNS = {
    "phone": re.compile(r"\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}"),
    "email": re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
    "address": re.compile(r"\d+\s+NE\s+\d+\w*\s+Avenue[^,]*,\s*\w[\w\s]*,\s*\w{2}\s+\d{5}"),
}

# Keywords that signal a complex query needing the LLM
COMPLEX_QUERY_WORDS = [
    "compare", "summarize", "summary", "explain why", "difference between",
    "recommend", "opinion", "which is better", "pros and cons",
    "what do you think", "how does.*differ", "advantages",
]

COMPLEX_PATTERN = re.compile("|".join(COMPLEX_QUERY_WORDS), re.IGNORECASE)


def is_complex_query(question: str) -> bool:
    """Decide whether the question needs LLM reasoning."""
    return bool(COMPLEX_PATTERN.search(question))


def extract_answer_from_chunks(question: str, chunks: list[str]) -> str | None:
    """
    Try to answer from retrieved chunks using rules.
    Only handles cases where a direct extraction is clearly correct.
    Returns None to let the LLM handle everything else.
    """
    q = question.lower()
    combined = "\n\n".join(chunks[:5])

    # --- Contact: phone ---
    if any(w in q for w in ["phone", "call", "number"]):
        phones = CONTACT_PATTERNS["phone"].findall(combined)
        emails = CONTACT_PATTERNS["email"].findall(combined)
        if phones or emails:
            parts = []
            if phones:
                parts.append(f"Phone: {phones[0]}")
            if emails:
                unique_emails = list(dict.fromkeys(emails))
                parts.append(f"Email: {unique_emails[0]}")
            return "\n".join(parts)

    # --- Contact: email ---
    if any(w in q for w in ["email", "mail"]):
        emails = CONTACT_PATTERNS["email"].findall(combined)
        if emails:
            unique = list(dict.fromkeys(emails))
            return "Email: " + ", ".join(unique[:3])

    # --- Contact: address ---
    if any(w in q for w in ["address", "located", "directions", "find you"]):
        addrs = CONTACT_PATTERNS["address"].findall(combined)
        if addrs:
            return f"Address: {addrs[0]}"
        if "11611" in combined:
            return "Address: 11611 NE 152nd Avenue, Brush Prairie, WA 98606"

    # Everything else goes to LLM for a proper synthesized answer
    return None


# --- Tier 2: LLM via Groq (only when rules can't answer) ---

_llm_chain = None


def get_llm_answer(question: str, context: str) -> str:
    """Call Groq LLM for complex queries. Lazy-loaded to avoid import if unused."""
    global _llm_chain

    groq_key = os.environ.get("GROQ_API_KEY")
    if not groq_key:
        return "For more detailed information, please call (564) 208-1315 or email info@silverbuckleranch.org"

    if _llm_chain is None:
        from langchain_groq import ChatGroq
        from langchain.chains import LLMChain
        from langchain.prompts import PromptTemplate

        llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0.3,
            max_tokens=300,
            groq_api_key=groq_key,
        )

        template = """You are a helpful assistant for the Silver Buckle Youth Equestrian Center (SBYEC).
Answer based ONLY on the context below. Be direct, friendly, and concise.

IMPORTANT RULES:
1. If the context mentions specific upcoming events with dates (e.g. "Critter Club February 22nd"), ALWAYS include them with their exact dates
2. Look carefully for "Upcoming Events" sections — these are the most important and timely details
3. Include specific details: names, dates, prices, ages, times when available
4. If you can't find the answer, say "For the most up-to-date information, please call (564) 208-1315 or email info@silverbuckleranch.org"

Context:
{context}

Question: {question}

Answer:"""

        prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        _llm_chain = LLMChain(llm=llm, prompt=prompt)

    try:
        return _llm_chain.invoke({"context": context, "question": question})["text"]
    except Exception:
        return "Sorry, I'm temporarily unable to provide a detailed answer. Please call (564) 208-1315."


# --- Main chatbot ---

class SBYECChatbot:
    def __init__(self):
        print("Initializing SBYEC Chatbot...")

        print("Loading embedding model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Load pre-built index if available, otherwise build on the fly
        if os.path.exists("faiss_index"):
            print("Loading pre-built FAISS index...")
            self.vectorstore = FAISS.load_local(
                "faiss_index", self.embeddings, allow_dangerous_deserialization=True
            )
        else:
            print("No pre-built index found, building from data/...")
            docs = self._load_documents()
            self.vectorstore = FAISS.from_texts(texts=docs, embedding=self.embeddings)

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity", search_kwargs={"k": 10}
        )

        # Keep all chunks for keyword fallback search
        self.all_chunks = self._load_all_chunks()
        print("Chatbot is ready!")

    def _load_all_chunks(self):
        """Load all text chunks for keyword search fallback."""
        chunks = []
        data_dir = "data"
        if os.path.exists(data_dir):
            for filename in sorted(os.listdir(data_dir)):
                if filename.endswith('.txt'):
                    with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                        chunks.append(f.read())
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=150,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        all_split = []
        for doc in chunks:
            all_split.extend(splitter.split_text(doc))
        return all_split

    def _load_documents(self):
        documents = []
        data_dir = "data"
        if os.path.exists(data_dir):
            for filename in sorted(os.listdir(data_dir)):
                if filename.endswith('.txt'):
                    with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
                        documents.append(f.read())
        if not documents:
            documents = ["SBYEC is a community organization."]

        from langchain.text_splitter import RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=150,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        split_docs = []
        for doc in documents:
            split_docs.extend(splitter.split_text(doc))
        return split_docs

    def _keyword_search(self, question: str, top_k: int = 3) -> list[str]:
        """Search all chunks by keyword overlap as a fallback for semantic search."""
        # Strip punctuation from query words so "events?" matches "events"
        q_words = set(re.sub(r"[^\w\s]", "", question.lower()).split())
        # Remove very common stop words that would match too many chunks
        q_words -= {"a", "an", "the", "is", "are", "do", "does", "what", "how", "any", "you", "your", "we", "our", "i", "my", "to", "for", "of", "in", "at", "on", "and", "or"}
        scored = []
        for chunk in self.all_chunks:
            chunk_lower = chunk.lower()
            score = sum(1 for w in q_words if w in chunk_lower)
            # Boost chunks that contain date-like patterns or event keywords
            if re.search(r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\b", chunk_lower):
                score += 3
            if "upcoming" in chunk_lower or "event" in chunk_lower:
                score += 2
            if score > 0:
                scored.append((score, chunk))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [chunk for _, chunk in scored[:top_k]]

    def ask(self, question: str) -> str:
        if not question.strip():
            return "Please ask a question about SBYEC!"

        # Retrieve relevant chunks via semantic search
        docs = self.retriever.invoke(question)
        chunks = [doc.page_content for doc in docs]

        # For event-related queries, supplement with keyword fallback
        q_lower = question.lower()
        event_words = ["event", "upcoming", "coming up", "schedule", "next", "when is", "activities", "happening"]
        if any(w in q_lower for w in event_words):
            keyword_chunks = self._keyword_search(question)
            # Prepend keyword chunks (up to 3) so date-specific info is guaranteed in context
            existing = set(chunks)
            prepend = [kc for kc in keyword_chunks if kc not in existing]
            chunks = prepend + chunks

        if not chunks:
            return "For the most up-to-date information, please call (564) 208-1315 or email info@silverbuckleranch.org"

        # Tier 1: Try rule-based extraction
        if not is_complex_query(question):
            answer = extract_answer_from_chunks(question, chunks)
            if answer:
                return answer

        # Tier 2: Fall back to LLM for complex queries
        context = "\n\n".join(chunks[:12])
        return get_llm_answer(question, context)


# --- Startup ---
print("Starting SBYEC Chatbot...")
chatbot = SBYECChatbot()


def respond(message, history):
    return chatbot.ask(message)


demo = gr.ChatInterface(
    fn=respond,
    title="",
    description="Ask me anything about Silver Buckle Youth Equestrian Center!",
    examples=[
        "What events are coming up?",
        "What programs do you offer?",
        "How can I contact you?",
    ],
    cache_examples=False,
    theme=gr.themes.Soft(),
    css="footer { display: none !important; }",
)

if __name__ == "__main__":
    demo.launch(show_api=False)
