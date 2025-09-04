import streamlit as st
from bedrock_api import get_diet_advice
from fpdf import FPDF
import re

# Set page configuration
st.set_page_config(page_title="Dietician Health Chatbot", page_icon="🥗", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f0f9f7;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to clear chat
def clear_chat():
    st.session_state.chat_history = []

# Remove emojis and non-ASCII characters
def remove_emojis(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

# Function to download chat as TXT
def download_chat_txt():
    chat_lines = []
    for sender, msg in st.session_state.chat_history:
        name = "You" if sender == "user" else "Dietician"
        chat_lines.append(f"{name}: {msg}\n")
    return "\n".join(chat_lines)

# Function to download chat as PDF
def download_chat_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    for sender, msg in st.session_state.chat_history:
        name = "You" if sender == "user" else "Dietician"
        clean_msg = remove_emojis(f"{name}: {msg}")
        pdf.multi_cell(0, 10, clean_msg + "\n")

    return pdf.output(dest='S').encode('latin1')


# Sidebar content
with st.sidebar:
    st.title("🍏 Nutrition Tips")
    st.markdown("### 🥦 Eat Smart:")
    st.markdown("- Fiber-rich veggies")
    st.markdown("- Whole grains")
    st.markdown("### 💧 Stay Hydrated")
    st.markdown("- 8+ glasses water/day")
    st.markdown("### 💤 Sleep & Activity")
    st.markdown("- 7–9 hours of sleep")
    st.markdown("- 30 min of exercise")

    st.divider()
    st.subheader("🧹 Chat Controls")
    if st.button("Clear Chat 🗑️"):
        clear_chat()

    if st.session_state.chat_history:
        txt_data = download_chat_txt()
        st.download_button("📄 Download Chat (TXT)", txt_data, file_name="dietician_chat.txt")

        pdf_data = download_chat_pdf()
        st.download_button("📄 Download Chat (PDF)", pdf_data, file_name="dietician_chat.pdf")


# Initial welcome message
if not st.session_state.chat_history:
    st.session_state.chat_history.append(("assistant", "Hi there! I'm your certified dietician 🤗. What can I help you with today?"))

# Chat input box
user_input = st.chat_input("Ask your question...")

# Process new input
if user_input:
    with st.spinner("Thinking..."):
        reply = get_diet_advice(user_input)

    # Save to history (append once)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", reply))

# Display full chat history
for sender, msg in st.session_state.chat_history:
    avatar = "🧑" if sender == "user" else "🥗"
    with st.chat_message(sender, avatar=avatar):
        st.markdown(msg)
