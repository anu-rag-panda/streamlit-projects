import streamlit as st
from PIL import Image

st.set_page_config(page_title="Anurag's Portfolio", page_icon=":guardsman:", layout="centered")

st.title("Hi, I'm Anurag! :wave:")
st.write("B.Tech in CSE | Python Developer | IoT & AI Enthusiast")

image = Image.open("assets/profile.png")
st.image(image, width=150)

st.markdown("""
            I build educational tools and application that make learning fun and engaging.
            I am passionate about using technology to create innovative solutions that can help people learn and grow.
            I am building student platforms that provide personalized learning experiences and help students achieve their goals.
            
            - 🎓 2nd year B. Tech CSE @ MAKAUT
            - 💻 Python Developer
            - 🌱 Currently learning IoT and AI
            - 🔧 Tech Stack: Python, Arduino, C, JS, Streamlit, ESP8266, ML, SQL
            
            use the sidebar to navigate through my portfolio and explore my projects, skills.
            """)

st.markdown("## Connect with me:")
st.markdown("""
            - [LinkedIn](https://www.linkedin.com/in/anurag-panda-/)
            - [GitHub](https://github.com/anu-rag-panda)
            - [Github](https://github.com/anurag1818)
            """)

st.write("Made with ❤️ by Anurag Panda")









