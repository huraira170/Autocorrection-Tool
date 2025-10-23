# app.py
import streamlit as st
from textblob import TextBlob
from openai import OpenAI
import os

st.set_page_config(page_title="AI Autocorrect Tool", page_icon="🧠")

st.title("🧠 AI Autocorrect Tool")
st.write("Fix your spelling and grammar using AI or offline NLP")

text = st.text_area("Enter your text below:")

mode = st.radio("Choose mode:", ["Offline (Free)", "Online (OpenAI GPT)"])

if st.button("Correct Text"):
    if mode == "Offline (Free)":
        corrected = str(TextBlob(text).correct())
        st.success(corrected)
    else:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Correct grammar and spelling: {text}"}]
        )
        st.success(response.choices[0].message.content)

