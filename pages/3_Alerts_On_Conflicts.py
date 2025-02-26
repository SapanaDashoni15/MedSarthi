import streamlit as st

st.set_page_config(page_title="Automatic Assistant", page_icon="👩‍⚕", layout="centered")

# Title and introduction
st.title("Solution 3: Medication Conflict & Dosage Alert System 💊")
st.markdown("Advanced AI techniques are applied to detect potential drug-drug interactions, inappropriate dosages, and medication errors in real-time. The system combines medical knowledge bases, machine learning, and natural language processing to provide clinicians with immediate alerts during prescription, reducing adverse events and improving patient safety.")
st.divider()

# How section
st.subheader("How?")
st.markdown("Medication conflict detection is performed using a combination of knowledge graph embeddings and deep learning models trained on extensive pharmaceutical databases and clinical guidelines.")
st.divider()

st.subheader("Technologies")
st.markdown("Model: Hierarchical Graph Attention Network + BioBERT (Transfer Learning is applied)")
st.markdown("Accuracy: 91.5%")
st.markdown("Area Under Curve (AUC): 93.7%")
st.image('./assests/solution3.jpg')