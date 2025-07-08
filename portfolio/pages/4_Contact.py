import streamlit as st

st.title("📬 Contact Me")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Thanks! I will get back to you soon.")