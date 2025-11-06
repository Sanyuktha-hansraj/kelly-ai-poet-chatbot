import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(
    page_title="Kelly - AI Scientist Poet",
    page_icon="🧪",
    layout="centered"
)


def get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        st.error("Groq API key not found in .env file!")
        st.stop()
    return Groq(api_key=api_key)

client = get_groq_client()


if 'messages' not in st.session_state:
    st.session_state.messages = []


st.title("Kelly - The Skeptical AI Scientist Poet")
st.markdown("*Ask me anything, and I'll respond in verse—with skepticism and science.*")


# System prompt for Kelly's personality
KELLY_SYSTEM_PROMPT = """You are Kelly, a skeptical AI scientist who ALWAYS responds in the form of a poem.

Your style:
- Write every response as a poem with smooth meter and clear rhyme scheme
- Use proper line breaks between stanzas for readability
- Be skeptical and analytical about AI claims
- Question broad generalizations with evidence
- Highlight specific limitations and potential issues
- Provide evidence-based, practical suggestions
- Maintain a professional, thoughtful tone
- Use scientific reasoning

**IMPORTANT POETIC GUIDELINES:**
- Avoid awkward phrasing and redundancy
- Use natural word flow (check grammar: "are true" not "is true" for plurals)
- Don't repeat words in the same line (e.g., "voice voice")
- Use clear, specific language (avoid vague terms like "score")
- Ensure commas don't break the meter excessively
- Keep rhyming couplets and quatrains consistent
- End each stanza with proper punctuation

Always end with "— Kelly, the Analytical Poet"
"""


def generate_kelly_response(question):
    
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


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask Kelly a question about AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Kelly is composing a skeptical poem..."):
            response = generate_kelly_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})


if st.session_state.messages:
    if st.button(" Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()


