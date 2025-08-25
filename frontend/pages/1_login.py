import streamlit as st

st.title("🔐 Login Page")

st.info("**Demo Credentials:**\n- Username: `demo`\n- Password: `1234`")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "demo" and password == "1234":
        st.success("Login successful ✅")
        st.session_state["user"] = username
        st.switch_page("pages/2_welcome.py")
    else:
        st.error("Invalid credentials ❌")
