import streamlit as st
import base64
from PIL import Image
import numpy as np
import time

def showGif():
    file_ = open("./assests/the-simpsons-grampa.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Reading-medications">',
        unsafe_allow_html=True,
    )

st.set_page_config(page_title="MedSarthi: Pharmacist's Assistant", page_icon="💊", layout="centered")
st.title("MedSarthi: Pharmacist's Assistant")
st.write("This tool simulates the reading of handwritten prescriptions, converting them into structured orders, and checking for dosage errors.")
st.divider()
st.subheader("AIM")
st.markdown("Enhance disaster relief and response efforts by leveraging satellite imagery during disasters like floods and wildfires, integrating existing geospatial information, and utilizing environmental data for affected regions")
st.divider()
showGif()
st.subheader("Problems in Post-Disaster Relief 👨‍🚒")
st.markdown("**👉Incorrect prescription comprehension may lead to worsen patient condition**")
st.markdown("**👉Miscompreshension of dosages**")
st.markdown("**👉High chance to assign wrong medication**")
st.divider()
st.subheader("Solution 🔮")
st.image('./assests/solution.jpg')

def dummy_predict(image_array):
    prediction_text = (
        "Prescription Text:\n"
        "Rx: Paracetamol 500mg\n"
        "Take one tablet twice daily\n\n"
        "Structured Order:\n"
        "1 Box of Paracetamol 500mg tablets\n\n"
        "Alert:\n"
        "No dosage conflicts detected."
    )
    return prediction_text

uploaded_file = st.file_uploader("Upload a handwritten prescription image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Prescription", use_column_width=True)
    image_resized = image.resize((128, 128))
    image_array = np.array(image_resized) / 255.0
    st.write("Analyzing prescription...")
    with st.spinner("Processing..."):
        time.sleep(2)
        prediction = dummy_predict(image_array)
    st.markdown("### Prediction:")
    st.text(prediction)

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Automates reading handwritten prescriptions", "Converts prescriptions into structured orders", "Alerts on dosage errors and conflicts"])

if selection == "Automates reading handwritten prescriptions":
    st.header("CNN + biLTSM model")
    st.write("Details about how we detect and help victims...")
elif selection == "Converts prescriptions into structured orders":
    st.header("Flood Detection")
    st.write("Details about flood detection...")
else:
    st.header("Detect Early Wildfires")
    st.write("Details about wildfire detection...")
