import streamlit as st

st.title("📄 Resume")

with open("assets/resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📥 Download My Resume",
                   data=PDFbyte,
                   file_name="Anurag_Resume.pdf",
                   mime='application/octet-stream')