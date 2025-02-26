import streamlit as st
import base64
from PIL import Image
import numpy as np
import time

# Set page config as the first Streamlit command
st.set_page_config(page_title="MedSarthi: Pharmacist's Assistant", page_icon="💊", layout="centered")

def showGif():
    with open("./assets/the-simpsons-grampa.gif", "rb") as file_:
        contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Reading-medications">',
        unsafe_allow_html=True,
    )

st.title("MedSarthi: Pharmacist's Assistant")
st.write("This tool simulates the reading of handwritten prescriptions, converting them into structured orders, and checking for dosage errors.")
st.divider()
st.subheader("AIM 🎯")
st.markdown("This project aims to minimize human errors in prescription reading from doctor's messy handwriiten by implementing CNN + biLTSM model using model dataset")
st.divider()
showGif()
st.subheader("Problems in Prescription recognition 👨‍🚒")
st.markdown("**👉Incorrect prescription comprehension may lead to worsen patient condition**")
st.markdown("**👉Miscompreshension of dosages**")
st.markdown("**👉High chance to assign wrong medication**")
st.divider()
st.subheader("Solution 🔮")
st.image('./assets/solution.jpg')

