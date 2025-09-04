import os
import streamlit as st
from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit setup
st.set_page_config(page_title="📄 RAG", layout="centered")
st.title("📄 GenAI RAG Chatbot")

# Ensure uploads folder exists
os.makedirs("uploads", exist_ok=True)

# PDF Text Extractor
def extract_text_from_pdf(uploaded_file):
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload a GenAI-related PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("📖 Reading and chunking the PDF..."):
        raw_text = extract_text_from_pdf(uploaded_file)

        # ✅ Chunk the text properly
        splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )
        chunks = splitter.split_text(raw_text)
        documents = [Document(page_content=chunk) for chunk in chunks]

        # ✅ Create embeddings & FAISS index
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(documents, embeddings)

        # ✅ Setup Groq LLM
        llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama3-8b-8192"
        )

        # ✅ Create RAG chain
        rag_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_type="similarity", k=3),
            return_source_documents=True
        )

    # Input query
    query = st.text_input("❓ Ask something from the uploaded GenAI PDF")

    if st.button("💬 Get Answer") and query:
        with st.spinner("🤖 Thinking..."):
            result = rag_chain.invoke(query)
            st.success(result["result"])

            with st.expander("📚 Retrieved Context Chunks"):
                for i, doc in enumerate(result["source_documents"], 1):
                    st.markdown(f"**Chunk {i}:**\n{doc.page_content}")
else:
    st.info("📄 Upload your GenAI reference PDF to begin.")
