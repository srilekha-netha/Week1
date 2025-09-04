import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load Groq API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Poem Generator", layout="centered")
st.title("🎨 Poem Generator")
st.markdown("Generate a personalized poem")

# Sidebar input
with st.sidebar:
    st.header("Customize")
    topic = st.text_input("Topic", placeholder="e.g. stars, dreams, time")
    tone = st.selectbox("Tone", ["Emotional", "Funny", "Romantic", "Dark", "Surreal"])
    length = st.slider("Poem Length (lines)", 4, 20, 8)
    generate = st.button("Generate Poem")

# On click
if generate:
    if not topic:
        st.warning("Please enter a topic!")
        st.stop()

    with st.spinner("✨ Generating your poetic masterpiece..."):

        # ✅ Use Groq's LLaMA 4 Model
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="meta-llama/llama-4-maverick-17b-128e-instruct"
        )

        # Prompt
        prompt = PromptTemplate.from_template(
            "Write a {tone} poem about '{topic}' in around {length} lines. "
            "Be vivid, poetic, and creative. Avoid repetition."
        )

        chain = prompt | llm | StrOutputParser()

        poem = chain.invoke({
            "topic": topic,
            "tone": tone.lower(),
            "length": length
        })

        # Display
        st.subheader("📜 Your Poem")
        st.markdown(f"```\n{poem.strip()}\n```")
        st.success("Poem generated successfully!")
