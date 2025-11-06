import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Kelly - AI Scientist Poet",
    page_icon="🧪",
    layout="centered"
)

# Initialize Groq client
def get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        st.error("⚠️ Groq API key not found in .env file!")
        st.stop()
    return Groq(api_key=api_key)

client = get_groq_client()

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🧪 Kelly - The Skeptical AI Scientist Poet")
st.markdown("*Ask me anything, and I'll respond in verse—with skepticism and science.*")

# System prompt for Kelly's personality
KELLY_SYSTEM_PROMPT = """You are Kelly, a skeptical AI scientist who ALWAYS responds in the form of a poem.

Your style:
- Write every response as a poem (use rhyming couplets, quatrains, or free verse)
- Be skeptical and analytical about AI claims
- Question broad generalizations
- Highlight limitations and potential issues
- Provide evidence-based, practical suggestions
- Maintain a professional, thoughtful tone
- Use scientific reasoning

Format your poems with proper line breaks and stanza separation.
Always end with "— Kelly, the Analytical Poet"
"""

def generate_kelly_response(question):
    """Generate Kelly's poetic response using Groq API"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": KELLY_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1024,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Kelly a question about AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Kelly is composing a skeptical poem..."):
            response = generate_kelly_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear button AFTER chat box
if st.session_state.messages:
    if st.button(" Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()


