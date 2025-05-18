# Sentiment-Analysis-API-with-FastAPI-Streamlit-and-API-Key-Auth

A lightweight and secure sentiment analysis application built with **FastAPI** for the backend and **Streamlit** for the frontend. This project demonstrates how to build an authenticated API with rate limiting and visualize predictions via an interactive web UI.

⚠️ Disclaimer: The primary focus of this project is to demonstrate secure API development with FastAPI, Streamlit integration, API key authentication, and rate limiting.
So, the sentiment analysis model used here was trained in a past experiment and may not deliver state-of-the-art accuracy.

---

## 🎥 Demo Video

[▶️ Watch Demo](https://www.dropbox.com/scl/fi/opnnszej1p0h1fjwkpvvl/Screen-Recording-2025-05-18-224456.mp4?rlkey=3ev9aazaese861tb19gx73kji&st=fo8u9c3g&dl=0)


## 🚀 Features

- 🔐 **API Key Authentication**
- 📉 **Rate Limiting** (per API key)
- 💬 **Sentiment Prediction** (positive/negative)
- 🌐 **Streamlit Frontend** for easy testing
- ⚡ Built using FastAPI and a pre-trained ML model

## Start the FastAPI server
`uvicorn main:app --reload`
Server runs at: http://127.0.0.1:8000

## Run the Streamlit app
In a new terminal: `streamlit run app.py`
Streamlit runs at: http://localhost:8501



