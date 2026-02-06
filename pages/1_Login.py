import streamlit as st
from utils.ui import set_background

# Page config MUST be first
st.set_page_config(page_title="PathFinder Login", layout="centered")

# Apply background
set_background()

# -------------------- LOGIN UI --------------------
st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email and password:
        st.session_state["logged_in"] = True
        st.session_state["user_email"] = email
        st.success("Login successful!")
        st.switch_page("pages/2_Home.py")
    else:
        st.error("Please enter email and password")
