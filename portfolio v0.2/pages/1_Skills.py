import streamlit as st

st.title("🛠 Skills & Technologies")

skills = {
    "Languages": ["Python", "JavaScript", "C", "HTML/CSS", "Arduino"],
    "Frameworks": ["Streamlit", "Firebase", "Supabase", "Ursina", "OpenCV"],
    "Hardware & IoT": ["ESP32", "Arduino", "NRF24L01", "DHT11", "HCSR04"],
    "Tools": ["GitHub", "Arduino", "VS Code", "Tinkercad", "Jupyter"],
    "Domains": ["EdTech", "IoT", "AI/ML", "Health", "Hackathon Projects"]
}

for category, items in skills.items():
    st.subheader(category)
    st.write(", ".join(items))