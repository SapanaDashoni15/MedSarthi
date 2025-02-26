import streamlit as st
from PIL import Image

st.set_page_config(page_title="Automatic Assistant", page_icon="👽", layout="centered")


st.title("Solution 1: Automatic Prescription Comprehension via ML model")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.subheader("Possible Medications present in prescription : Azomac, Fexofast")
