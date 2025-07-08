import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 Quantum Wavefunction Visualizer")

L = st.number_input("Well Width (L)", value=1.0)
n = st.slider("Energy Level (n)", 1, 10, 1)

x = np.linspace(0, L, 1000)
ψ = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
prob = ψ**2

fig, ax = plt.subplots()
ax.plot(x, ψ, label="Wavefunction ψ(x)")
ax.plot(x, prob, label="Probability Density |ψ|²", linestyle='--')
ax.set_xlabel("x (m)")
ax.set_title(f"Infinite Potential Well: n = {n}")
ax.legend()
st.pyplot(fig)


#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")