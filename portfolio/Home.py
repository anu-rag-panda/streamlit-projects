import streamlit as st

st.set_page_config(page_title="Anurag Panda", page_icon="👋", layout="wide")

st.title("👋 Welcome to My Portfolio")

st.markdown("Hi, I'm **Anurag Panda**, a passionate Computer Science student and Developer.")

col1, col2 = st.columns([1, 2])

with col1:
    st.image('assets/profile.png', width=200)
    
with col2:
    st.markdown("""
                🚀 I build intelligent apps and hardware projects. <br>
                💡 Interested in AI, IoT, and Web Dev. <br>
                [contact me](./contact)
        """, unsafe_allow_html=True)
    
