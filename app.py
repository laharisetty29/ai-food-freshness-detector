import streamlit as st
import requests

st.title("🍎 AI Food Detector")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

if uploaded_file:
    st.image(uploaded_file)
    
    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        files={"image": uploaded_file}
    )
    
    if response.status_code == 200:
        result = response.json()
        
        for item in result["results"]:
            st.write(item)