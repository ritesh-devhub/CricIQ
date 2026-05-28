import streamlit as st
import requests

st.set_page_config(
    page_title="CricIQ",
    layout="wide"
)

st.title("🏏 CricIQ")
st.subheader("Ask cricket questions in plain English")

query = st.text_input(
    "Ask a cricket question"
)

if st.button("Submit"):

    if query:
        st.success(f"You asked: {query}")

        response = requests.get(
            "http://127.0.0.1:8000/health"
        )

        st.json(response.json())