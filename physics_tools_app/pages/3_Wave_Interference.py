import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🌊 Wave Interference Simulator")

λ = st.number_input("Wavelength (λ)", value=500.0, min_value=100.0, max_value=2000.0)
d = st.number_input("Source Separation (d)", value=1000.0)
L = st.number_input("Screen Distance (L)", value=1000.0)

y = np.linspace(-500, 500, 1000)
x = d * y / (2 * L)
I = (np.cos(np.pi * d * y / (λ * L)))**2  # Simplified interference pattern

fig, ax = plt.subplots()
ax.plot(y, I, 'b')
ax.set_title("Interference Pattern")
ax.set_xlabel("Screen Position (mm)")
ax.set_ylabel("Intensity")
st.pyplot(fig)


#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")