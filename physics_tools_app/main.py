import streamlit as st

st.set_page_config(page_title="Physics Tools", layout="centered")

st.title("🧪 Physics Tools Dashboard")
st.markdown("""
Welcome to the **Physics Tools App**!  
Use the sidebar to access individual simulations:
- 🎯 Projectile Motion
- 🔍 Lens Simulator
- 🌊 Wave Interference
- ⚡ RC Circuit Visualizer
- 🧠 Quantum Wavefunction

Built with ❤️ using Streamlit.
""")
st.sidebar.title("Navigation")
st.sidebar.markdown("""
Select a simulation from the list above to get started:
 """)

#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")