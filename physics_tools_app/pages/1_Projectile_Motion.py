import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎯 Projectile Motion Simulator")

# Inputs
u = st.number_input("Initial velocity (m/s)", 1.0, 100.0, 20.0)
theta = st.slider("Launch angle (degrees)", 0, 90, 45)
g = st.number_input("Gravity (m/s²)", 1.0, 20.0, 9.81)

# Calculations
theta_rad = np.radians(theta)
t_flight = 2 * u * np.sin(theta_rad) / g
t = np.linspace(0, t_flight, num=500)
x = u * np.cos(theta_rad) * t
y = u * np.sin(theta_rad) * t - 0.5 * g * t**2

# Plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Height (m)")
ax.set_title("Projectile Trajectory")
ax.grid()

st.pyplot(fig)

st.markdown(f"**Time of Flight:** {t_flight:.2f} s")
st.markdown(f"**Max Height:** {np.max(y):.2f} m")
st.markdown(f"**Range:** {np.max(x):.2f} m")

#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")