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
    Returns a formatted answer string, or None if LLM is needed.
    """
    q = question.lower()
    combined = "\n\n".join(chunks[:5])  # top 5 chunks

    # --- Contact info ---
    if any(w in q for w in ["phone", "call", "number", "contact", "reach"]):
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

    if any(w in q for w in ["email", "mail"]):
        emails = CONTACT_PATTERNS["email"].findall(combined)
        if emails:
            unique = list(dict.fromkeys(emails))
            return "Email: " + ", ".join(unique[:3])

    if any(w in q for w in ["address", "location", "where", "located", "directions", "find you"]):
        addrs = CONTACT_PATTERNS["address"].findall(combined)
        if addrs:
            return f"Address: {addrs[0]}"
        # Fallback: look for known address in text
        if "11611" in combined:
            return "Address: 11611 NE 152nd Avenue, Brush Prairie, WA 98606"

    # --- Events ---
    if any(w in q for w in ["event", "upcoming", "happening", "schedule", "when"]):
        # Find event-related chunks and return them directly
        event_chunks = [c for c in chunks if any(
            kw in c.lower() for kw in ["event", "upcoming", "peppermint", "halloween", "spring farm", "books at"]
        )]
        if event_chunks:
            return event_chunks[0].strip()

    # --- Pricing ---
    price_match = re.findall(r"\$\d+(?:\.\d{2})?(?:/\w+)?", combined)
    if any(w in q for w in ["cost", "price", "how much", "fee", "pricing"]) and price_match:
        # Return the chunk that contains pricing
        for chunk in chunks[:5]:
            if "$" in chunk:
                return chunk.strip()

    # --- Team / staff ---
    if any(w in q for w in ["team", "staff", "instructor", "board", "who works"]):
        team_chunks = [c for c in chunks if any(
            kw in c for kw in ["Manager", "Instructor", "President", "Treasurer", "Secretary"]
        )]
        if team_chunks:
            return team_chunks[0].strip()

    # --- Hours / lessons ---
    if any(w in q for w in ["lesson", "riding", "class", "learn to ride"]):
        lesson_chunks = [c for c in chunks if "lesson" in c.lower() or "riding" in c.lower()]
        if lesson_chunks:
            return lesson_chunks[0].strip()

    # --- Programs ---
    if any(w in q for w in ["program", "camp", "volunteer", "field trip", "books", "encounter"]):
        for chunk in chunks[:5]:
            return chunk.strip()

    # --- Generic: if the top chunk has high relevance, return it ---
    # For simple factual questions, the top retrieved chunk is often sufficient
    if chunks:
        top = chunks[0].strip()
        # Only return directly if the chunk is substantive
        if len(top) > 50:
            return top

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
If you can't find the answer, say "For the most up-to-date information, please call (564) 208-1315 or email info@silverbuckleranch.org"

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
        print("Chatbot is ready!")

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

    def ask(self, question: str) -> str:
        if not question.strip():
            return "Please ask a question about SBYEC!"

        # Retrieve relevant chunks
        docs = self.retriever.invoke(question)
        chunks = [doc.page_content for doc in docs]

        if not chunks:
            return "For the most up-to-date information, please call (564) 208-1315 or email info@silverbuckleranch.org"

        # Tier 1: Try rule-based extraction
        if not is_complex_query(question):
            answer = extract_answer_from_chunks(question, chunks)
            if answer:
                return answer

        # Tier 2: Fall back to LLM for complex queries
        context = "\n\n".join(chunks[:5])
        return get_llm_answer(question, context)


# --- Startup ---
print("Starting SBYEC Chatbot...")
chatbot = SBYECChatbot()


def respond(message, history):
    return chatbot.ask(message)


demo = gr.ChatInterface(
    fn=respond,
    title="SBYEC Chatbot",
    description="Ask me anything about Silver Buckle Youth Equestrian Center!",
    examples=[
        "Where is SBYEC located?",
        "What programs do you offer?",
        "What events are coming up?",
        "How can I contact you?",
    ],
    cache_examples=False,
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
