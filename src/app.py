import streamlit as st

st.set_page_config(page_title="Air Canvas", layout="centered")

st.title("🎨 Air Canvas – Gesture Based Drawing")

st.markdown("""
Air Canvas is a computer vision project that allows users to draw in the air
using hand gestures detected through a webcam.

⚠️ **Note:**  
Live webcam drawing works only in local execution due to cloud limitations.
""")

st.header("📸 Demo")
st.video("https://your-demo-video-link")

st.header("⬇️ Download Sample Drawing")
with open("sample.png", "rb") as f:
    st.download_button("Download Drawing", f, "drawing.png")
