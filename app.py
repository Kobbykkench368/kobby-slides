import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# 1. Setup API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Using the Imagen model for image generation
    model = genai.GenerativeModel('gemini-1.5-flash') 
except Exception as e:
    st.error("Credential Error: Check your Streamlit Secrets.")

st.set_page_config(page_title="Kobby's AI Image Lab", page_icon="🎨")

st.title("Kobby's AI Image Lab 🎨")
st.write("Generate high-quality visuals for music covers or business presentations.")

prompt = st.text_area("Describe the image you want to create:", 
                     placeholder="e.g., A futuristic recording studio in Kumasi with neon lights")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("AI is painting your vision..."):
            try:
                # 2. Request Image Generation
                # Note: This requires your API key to have permission for Imagen
                response = model.generate_content(
                    f"Generate a detailed image description for: {prompt}",
                )
                
                # Displaying the text-based creative direction first
                st.subheader("Creative Concept:")
                st.write(response.text)
                
                st.info("Note: Standard Gemini API keys primarily generate text/code. For direct pixel-generation, ensure your Google Cloud project has Vertex AI Imagen enabled.")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please describe an image first!")

st.divider()
st.caption("Developed by Kobby Klench | KNUST Management Student")
