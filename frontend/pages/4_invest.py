import streamlit as st
import datetime
import requests

if "user" not in st.session_state:
    st.warning("Please login first!")
    st.stop()

st.title("🪙 Buy Digital Gold")

st.markdown("""
<style>
.big-invest-btn {
    background-color: #1a6cff;
    color: white;
    border-radius: 25px;
    padding: 1em 2.5em;
    font-size: 1.3em;
    font-weight: bold;
    border: none;
    margin-top: 1.5em;
    margin-bottom: 1em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown("#### Enter Amount to Invest")
amount = st.text_input("Amount in ₹", value="", key="gold_amount")

st.markdown("#### Enter Current Gold Price (per gram)")
gold_price = st.text_input("Gold Price (₹/g)", value="10341.52", key="gold_price")

weight = 0
try:
    amt = float(amount) if amount else 0
    price = float(gold_price) if gold_price else 0
    weight = amt / price if price > 0 else 0
except ValueError:
    st.error("Please enter valid numbers.")

st.markdown(f"**Gold you will get:** `{weight:.4f} g`")

if st.button("Invest Now", key="invest_now", use_container_width=True):
    username = st.session_state["user"]
    now = datetime.datetime.now()
    st.success(
        f"""
        🎉 **Congratulations, {username}!**
        
        You have successfully invested in digital gold.
        
        **Investment Details:**
        - **Date & Time:** {now.strftime("%Y-%m-%d %H:%M:%S")}
        - **Amount Invested:** ₹{amt:.2f}
        - **Gold Price:** ₹{price:.2f}/g
        - **Gold Weight:** {weight:.4f} g
        """
    )
    # Save to database
    purchase_data = {
        "username": st.session_state["user"],
        "amount": amt,
        "gold_price": price,
        "weight": weight
    }
    resp = requests.post("http://127.0.0.1:8000/invest", json=purchase_data)
    if resp.status_code == 200 and resp.json().get("status") == "success":
        st.info("Purchase saved to database.")
    else:
        st.error("Failed to save purchase.")




