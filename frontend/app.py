import streamlit as st

# Set page config
st.set_page_config(page_title="Kuber AI", page_icon="🤖", layout="wide")

# Info: Streamlit multipage apps automatically show all files in the 'pages' directory as sidebar navigation.
# You do NOT need to manually switch pages using st.switch_page in the main app file.

st.title("Kuber AI")
# st.image("assets/robot.png", width=300)
st.markdown("Welcome to Kuber AI! Please use the sidebar to navigate between Login, Welcome, Chat, and Invest pages.")

# Optionally, you can display a message or logo here.

