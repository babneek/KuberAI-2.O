import streamlit as st
import requests

API_URL = "https://kuberai-2o-production.up.railway.app"

if "user" not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("💬 Kuber AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Handle query from welcome page
if "chat_query" in st.session_state and st.session_state.chat_query:
    user_input = st.session_state.chat_query
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    try:
        response = requests.post(f"{API_URL}/chat", json={"query": user_input})
        bot_answer = response.json().get("answer", "Sorry, no response.")
    except Exception as e:
        bot_answer = f"Error: {e}"
    st.session_state.chat_history.append({"role": "bot", "content": bot_answer})
    st.session_state.chat_query = ""  # Clear after use

# Display chat history first
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Kuber.AI:** {msg['content']}")
        # Bright suggestion card after every bot response
        st.markdown("""
            <div style="background-color:#ffe066; color:#222; padding:16px; border-radius:12px; margin-top:10px; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                <span style="font-size:18px; font-weight:bold;">
                    <span style="font-size:22px;">💡</span> Would you like to buy digital gold now?
                </span><br>
                <span style="font-size:16px;">Start your investment in <b>24k 99.99% pure gold</b> – securely stored and insured.</span>
            </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Buy Digital Gold", key=f"buy_gold_{msg['content']}"):
                st.switch_page("pages/4_invest.py")
        with col2:
            st.button("Not Now", key=f"not_now_{msg['content']}")

# Chat input box at the bottom
st.markdown("---")
user_input = st.text_input("Type your question about gold investment:", key="chat_input")
if st.button("Send", key="send_btn"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        try:
            response = requests.post(f"{API_URL}/chat", json={"query": user_input})
            bot_answer = response.json().get("answer", "Sorry, no response.")
        except Exception as e:
            bot_answer = f"Error: {e}"
        st.session_state.chat_history.append({"role": "bot", "content": bot_answer})
        st.experimental_rerun()

st.markdown("🔒 Your info is secure and private.")
