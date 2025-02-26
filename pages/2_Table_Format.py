import streamlit as st

st.set_page_config(page_title="Automatic Assistant", page_icon="🚨", layout="centered")

st.title("Solution2: Structured format for the prescription with dosages + ShortHand recognition") 
st.markdown("This solution aspires to provided a structured list of priscribed mediaction for patient/ pharmacist for easy access and faster medicine retrieval and also understtands medical Shorthands")

st.divider()

st.subheader("How ? ") 
st.markdown("👉 Image Preprocessing - Rescaling, Skew Correction, Slant Correction, Image Thresholding")
st.markdown("👉Page Segmentation - Segregate the handwritten text from the printed text ")
st.markdown("👉Line Segmentation - Segregate each line from the segmented handwritten text")
st.markdown("👉 Handwritten Text Recognition - Use Deep CNN and bi-LSTM to convert image text to characters.")
st.markdown("👉 Keyword Spotting - Using the predefined python repositories of medical terms, we will be spotting the medical keywords from the medical prescriptions")

st.markdown("Accuracy - 91.78%")

st.image('./assets/solution2.jpg')
st.markdown("CNN + BiLSTM model for medical shorthand recognition output:")
st.image('./assets/solution22.jpg')

st.markdown("Numerical confusion matrix for medical shorthand recognition")
st.image('./assets/solution23.jpg')