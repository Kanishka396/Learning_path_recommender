import base64
import os
import streamlit as st

def set_background():
    bg_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "assets",
        "bg.jpg"
    )

    with open(bg_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
