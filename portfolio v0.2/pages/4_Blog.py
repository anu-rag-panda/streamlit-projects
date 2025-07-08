import streamlit as st

st.title("📝 Blog")

blogs = [
    {
        "title": "How I Built a Smart Attendance System with Streamlit + OpenCV",
        "link": "https://dev.to/anurag_panda/face-attendance-maker-using-streamlit-and-opencv-3fh0"
    }
]

for blog in blogs:
    st.subheader(blog["title"])
    st.markdown(f"[Read More →]({blog['link']})")