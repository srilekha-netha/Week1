from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# === CONFIG ===
file_path = "cc.pdf"  # Change to your .pdf file if needed
chunk_size = 1000
chunk_overlap = 200

# === LOADER ===
if file_path.endswith(".txt"):
    loader = TextLoader(file_path)
elif file_path.endswith(".pdf"):
    loader = PyPDFLoader(file_path)
else:
    raise ValueError("Unsupported file type. Please use .txt or .pdf")

documents = loader.load()

# === SPLITTER ===
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

chunks = splitter.split_documents(documents)

# === OUTPUT ===
print(f"✅ Loaded {len(documents)} full document(s)")
print(f"🧩 Split into {len(chunks)} chunks using RecursiveCharacterTextSplitter")
