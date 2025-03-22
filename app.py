import streamlit as st
import openai

# 🎨 Custom Page Style
st.set_page_config(page_title="Dr. Tofi's Bot", page_icon="🤖", layout="wide")

# 🔥 Custom CSS for Styling
st.markdown("""
    <style>
        body {background-color: #f4f4f4;}
        .stChatMessage {border-radius: 10px; padding: 10px; margin-bottom: 10px;}
        .user {background-color: #DCF8C6; text-align: right;}
        .assistant {background-color: #E3E3E3;}
        .title {text-align: center; color: #ff5733;}
        .created {text-align: center; font-size: 16px; color: #888;}
    </style>
""", unsafe_allow_html=True)

# 🔑 OpenAI API Key
openai.api_key = "your-openai-api-key"  # 🛑 Yahan apni API key lagani hai!

# 🎯 Chatbot Title
st.markdown("<h1 class='title'>🤖 Dr. Tofi's Bot</h1>", unsafe_allow_html=True)
st.markdown("<p class='created'>✨ Created by Sheeraz Ahmed ✨</p>", unsafe_allow_html=True)

# 💬 Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 📜 Show Chat History
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "assistant"
    st.markdown(f"<div class='stChatMessage {role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# ✍ User Input Box
user_input = st.chat_input("Type your message here...")

if user_input:
    # 👤 Show User Message
    st.markdown(f"<div class='stChatMessage user'>{user_input}</div>", unsafe_allow_html=True)
    
    # 🧠 AI Response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    bot_reply = response["choices"][0]["message"]["content"]
    
    # 🤖 Show Bot Message
    st.markdown(f"<div class='stChatMessage assistant'>{bot_reply}</div>", unsafe_allow_html=True)

    # 💾 Save to Chat History
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
