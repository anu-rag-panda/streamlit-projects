import streamlit as st

st.title("📁 Projects")

projects = [
    {"title": "NeuroFit Band", "desc": "A smart headband for stress & mood tracking."},
    {"title": "Smart Attendance System", "desc": "Face detection-based real-time attendance tracker."},
    {"title": "WasteNot", "desc": "Food expiry and waste tracker using Python."},
]

for proj in projects:
    st.subheader(proj["title"])
    st.markdown(proj["desc"])
    st.markdown("---")