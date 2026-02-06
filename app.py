import streamlit as st
from utils.ui import set_background

# Page config must be first
st.set_page_config(
    page_title="PathFinder",
    layout="wide"
)

# Apply background globally
set_background()

# Route to Login page
st.switch_page("pages/1_Login.py")
