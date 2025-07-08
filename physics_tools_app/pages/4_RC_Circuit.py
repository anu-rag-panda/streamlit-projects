import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("⚡ RC Circuit Visualizer")

R = st.number_input("Resistance R (Ω)", value=1000.0)
C = st.number_input("Capacitance C (μF)", value=100.0)
V = st.number_input("Voltage Supply (V)", value=5.0)
action = st.radio("Action", ["Charging", "Discharging"])

RC = R * (C / 1e6)  # Convert μF to F
t = np.linspace(0, 5 * RC, 500)

if action == "Charging":
    voltage = V * (1 - np.exp(-t / RC))
else:
    voltage = V * np.exp(-t / RC)

fig, ax = plt.subplots()
ax.plot(t, voltage)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title(f"RC Circuit: {action}")
st.pyplot(fig)

st.markdown(f"**Time Constant (RC):** {RC:.2f} s")


#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")