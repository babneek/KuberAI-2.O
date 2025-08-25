import streamlit as st

st.set_page_config(page_title="Kuber.AI", page_icon="🤖", layout="centered")

st.title("Kuber.AI")
# st.image(
#     r"c:\Users\BABNEEK\OneDrive\Desktop\projects\KuberAI-2.O\frontend\assets\robot.png",
#     width=150
# )

st.markdown("### Ask me Your Financial Queries")
st.markdown("Begin your first Chat with Kuber AI :coin: 10")

# Gold-related suggestions
suggestions = [
    "Is gold a good investment in 2025?",
    "What are the benefits of investing in gold?",
    "How to buy digital gold safely?",
    "Should I invest in gold ETFs or physical gold?",
    "What factors affect gold prices?",
]

# Session state for input box
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def fill_input(suggestion):
    st.session_state.user_input = suggestion

st.markdown("#### Gold Investment Suggestions:")
cols = st.columns(len(suggestions))
for i, suggestion in enumerate(suggestions):
    with cols[i]:
        st.button(suggestion, on_click=fill_input, args=(suggestion,))

# FIX: Remove 'value' argument to avoid widget/session state conflict
user_query = st.text_input("Message Kuber.AI", key="user_input")

if st.button("Send"):
    if st.session_state.user_input.strip():
        st.session_state.chat_query = st.session_state.user_input
        st.switch_page("pages/3_chat.py")


st.markdown("🔒 Your data is safe with us")
