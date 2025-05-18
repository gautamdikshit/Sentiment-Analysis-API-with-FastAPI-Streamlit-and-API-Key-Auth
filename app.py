import streamlit as st
import requests

st.title("🧠 Sentiment Analysis App")

api_key = st.text_input("Enter your API Key:", type="password")
text_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if not api_key:
        st.warning("Please enter an API key.")
    elif text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"text": text_input},
            headers={"X-API-Key": api_key}
        )
        if response.status_code == 200:
            result = response.json()
            st.success(f"Sentiment: **{result['sentiment']}**")
        else:
            st.error(f"Error: {response.json()['detail']}")
