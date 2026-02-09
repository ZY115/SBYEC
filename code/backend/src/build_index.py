"""
Offline FAISS index builder.
Run this locally or in GitHub Actions to pre-build the vector index.
Avoids rebuilding on every HF Spaces startup.
"""

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def build_index(data_dir="data", index_dir="faiss_index"):
    print("Loading documents...")
    documents = []

    if os.path.exists(data_dir):
        for filename in sorted(os.listdir(data_dir)):
            if filename.endswith('.txt'):
                filepath = os.path.join(data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    documents.append(f.read())

    if not documents:
        print("ERROR: No .txt files found in data/")
        return

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    split_docs = []
    for doc in documents:
        split_docs.extend(text_splitter.split_text(doc))

    print(f"  {len(documents)} files -> {len(split_docs)} chunks")

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Building FAISS index...")
    vectorstore = FAISS.from_texts(texts=split_docs, embedding=embeddings)

    os.makedirs(index_dir, exist_ok=True)
    vectorstore.save_local(index_dir)
    print(f"Index saved to {index_dir}/")


if __name__ == "__main__":
    build_index()
