import streamlit as st
import google.generativeai as genai

# This pulls your key from a hidden settings file we will create in Step 4
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key not found! Please add it to Streamlit Secrets.")

st.title("Kobby's Slide Generator")
st.write("Welcome! This app uses AI to help generate presentation content.")

# Your music/business logic goes here!
topic = st.text_input("What is your presentation about?")
if st.button("Generate"):
    st.write(f"Generating slides for: {topic}...")
