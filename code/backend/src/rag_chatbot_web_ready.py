"""
Web-Ready RAG-enabled Chatbot for SBYEC Website
This version includes auto-refresh and Flask API for web deployment
"""

import os
import shutil
from datetime import datetime
from langchain_community.llms import Ollama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


class SBYECChatbotWebReady:
    def __init__(self, data_directory="data", chroma_persist_dir="./chroma_db"):
        """Initialize the chatbot with RAG capabilities"""
        print("Initializing SBYEC Chatbot (Web-Ready Version)...")

        self.data_directory = data_directory
        self.chroma_persist_dir = chroma_persist_dir
        self.last_loaded = None

        # 1. Initialize the local LLM (Ollama)
        print("Connecting to Ollama (local AI model)...")
        # Use 1B for free servers, 3B for local/paid (uncomment line below)
        self.llm = Ollama(model="llama3.2:1b", temperature=0.3)
        # self.llm = Ollama(model="llama3.2:3b", temperature=0.3)  # Better accuracy, slower

        # 2. Initialize embeddings (converts text to numbers for search)
        print("Loading embedding model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # 3. Load and initialize the knowledge base
        self._initialize_knowledge_base()

        print("Chatbot is ready!\n")

    def _initialize_knowledge_base(self):
        """Load documents and create vector database"""
        print(f"Loading content from {self.data_directory}/...")
        self.documents = self._load_documents()

        print("Creating vector database...")
        self.vectorstore = self._create_vectorstore()

        print("Setting up question-answering system...")
        self.qa_chain = self._create_qa_chain()

        self.last_loaded = datetime.now()
        print(f"   Knowledge base loaded at: {self.last_loaded.strftime('%Y-%m-%d %H:%M:%S')}")

    def _load_documents(self):
        """Load all text files from the data directory"""
        documents = []

        # Read all .txt files in the data directory
        if os.path.exists(self.data_directory):
            for filename in os.listdir(self.data_directory):
                if filename.endswith('.txt'):
                    filepath = os.path.join(self.data_directory, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            documents.append(content)
                    except Exception as e:
                        print(f"Error reading {filename}: {e}")

        if not documents:
            print("Warning: No .txt files found in data directory!")
            documents = ["SBYEC is a community organization."]  # Fallback

        # Split documents into smaller chunks for better retrieval
        # OPTIMIZED: Larger chunks to keep related info together
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  # Increased to keep context together
            chunk_overlap=150,  # More overlap for better matching
            separators=["\n\n", "\n", ". ", " ", ""]
        )

        split_docs = []
        for doc in documents:
            split_docs.extend(text_splitter.split_text(doc))

        print(f"   Loaded {len(documents)} files, split into {len(split_docs)} chunks")
        return split_docs

    def _create_vectorstore(self):
        """Create a vector database from documents"""
        # Convert documents to vectors and store in ChromaDB
        vectorstore = Chroma.from_texts(
            texts=self.documents,
            embedding=self.embeddings,
            persist_directory=self.chroma_persist_dir
        )
        return vectorstore

    def _create_qa_chain(self):
        """Create a question-answering chain"""
        template = """You are a helpful assistant for the Silver Buckle Youth Equestrian Center (SBYEC).

Your role is to answer questions based ONLY on the provided context. Be direct, friendly, and concise.

IMPORTANT RULES:
1. If the context contains the answer, provide it clearly and completely
2. Always include specific details like addresses, phone numbers, dates, or names when available
3. For events questions: Look for "Upcoming Events", "Peppermints", "Halloween", "Spring Farm", event names, or dates like "12/13/25"
4. If you find event information, list ALL events mentioned with their dates
5. If you're not sure or can't find the information, say "For the most up-to-date information, please call (564) 208-1315 or email info@silverbuckleranch.org"
6. Don't make up information - only use what's in the context

Context:
{context}

Question: {question}

Helpful Answer:"""

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 10}  # Retrieve more chunks for better coverage
            ),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=False
        )

        return qa_chain

    def refresh_knowledge_base(self):
        """Reload the knowledge base from updated files"""
        print("\nRefreshing knowledge base...")

        # Clear existing vector database
        if os.path.exists(self.chroma_persist_dir):
            shutil.rmtree(self.chroma_persist_dir)
            print("   Cleared old vector database")

        # Reinitialize
        self._initialize_knowledge_base()
        print("Knowledge base refreshed!\n")

    def check_for_updates(self):
        """Check if content files have been updated"""
        if not os.path.exists(self.data_directory):
            return False

        # Check modification time of content files
        latest_mod_time = None
        for filename in os.listdir(self.data_directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(self.data_directory, filename)
                mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                if latest_mod_time is None or mod_time > latest_mod_time:
                    latest_mod_time = mod_time

        # If files were modified after last load, update needed
        if latest_mod_time and self.last_loaded and latest_mod_time > self.last_loaded:
            return True

        return False

    def ask(self, question, auto_refresh=False):
        """
        Ask the chatbot a question

        Args:
            question: The question to ask
            auto_refresh: If True, check for updates before answering
        """
        # Auto-refresh if requested and updates detected
        if auto_refresh and self.check_for_updates():
            print("📢 New content detected, refreshing knowledge base...")
            self.refresh_knowledge_base()

        response = self.qa_chain.invoke({"query": question})
        return response["result"]

    def chat(self):
        """Interactive chat session"""
        print("=" * 60)
        print("SBYEC AI Chatbot - Powered by RAG + Local LLM")
        print("Silver Buckle Youth Equestrian Center")
        print("=" * 60)
        print("\nAsk me anything about SBYEC!")
        print("Type 'quit' to exit, 'refresh' to reload content")
        print("\nSuggested questions:")
        print("  - Where is SBYEC located?")
        print("  - What programs do you offer?")
        print("  - What events are coming up?")
        print("  - How can I contact you?\n")

        while True:
            question = input("You: ").strip()

            if question.lower() in ['quit', 'exit', 'bye']:
                print("\nChatbot: Thank you for your interest in SBYEC! Visit us at sbyec.org or call (564) 208-1315. Goodbye!")
                break

            if question.lower() == 'refresh':
                self.refresh_knowledge_base()
                continue

            if not question:
                continue

            print("\nChatbot: ", end="", flush=True)
            answer = self.ask(question, auto_refresh=True)
            print(f"{answer}\n")


if __name__ == "__main__":
    # Initialize and run the chatbot
    chatbot = SBYECChatbotWebReady(data_directory="data")
    chatbot.chat()
