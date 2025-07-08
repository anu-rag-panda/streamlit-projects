import streamlit as st
import matplotlib.pyplot as plt

st.title("🔍 Lens Simulator")

f = st.number_input("Focal Length (cm)", value=10.0)
u = st.number_input("Object Distance (cm, negative if in front of lens)", value=-20.0)

try:
    v = 1 / (1/f - 1/u)
    m = v / u
    image_type = "Real" if v > 0 else "Virtual"

    st.markdown(f"**Image Distance:** {v:.2f} cm")
    st.markdown(f"**Magnification:** {m:.2f}x ({'Inverted' if m < 0 else 'Upright'})")
    st.markdown(f"**Image Type:** {image_type}")

    # Simple ray diagram
    fig, ax = plt.subplots()
    ax.axvline(x=0, color='black')  # Lens
    ax.plot([u, 0], [0, 0], 'bo-', label='Object')
    ax.plot([0, v], [0, 0], 'ro-', label='Image')
    ax.set_xlim(min(u, v) - 10, max(u, v) + 10)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("Position (cm)")
    ax.legend()
    st.pyplot(fig)

except ZeroDivisionError:
    st.error("Object distance cannot equal focal length (infinite image).")


#footer
st.write("---")
st.markdown("Made with ❤️ by [Anurag Panda](https://linkedin.com/in/anurag-panda-)")