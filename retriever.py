import os
import faiss
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from config import OPENAI_API_KEY

# Directory paths
DATA_DIR = "data/documents/"
INDEX_DIR = "data/faiss_index/"

# Load HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def load_and_process_documents():
    """Loads PDFs, extracts text, splits into chunks, and converts to embeddings."""
    docs = []
    
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_DIR, filename))
            docs.extend(loader.load())
    
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_documents(docs)

    return texts

def create_faiss_index():
    """Creates a FAISS index for document retrieval."""
    texts = load_and_process_documents()
    if not texts:
        print("No documents found!")
        return None

    vector_store = FAISS.from_documents(texts, embeddings)
    vector_store.save_local(INDEX_DIR)
    print("FAISS index created and saved!")

def retrieve_documents(query, top_k=3):
    """Retrieves top-k most relevant text chunks based on query."""
    vector_store = FAISS.load_local(INDEX_DIR, embeddings, allow_dangerous_deserialization=True)
    docs = vector_store.similarity_search(query, k=top_k)
    
    return [doc.page_content for doc in docs]

if __name__ == "__main__":
    create_faiss_index()
