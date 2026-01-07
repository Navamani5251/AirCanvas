import streamlit as st
import cv2
import numpy as np
from canvas import DrawingCanvas
from Gesture_detector import GestureDetector
from utils import blend_frames

st.set_page_config(page_title="Air Canvas Web", layout="centered")
st.title("🖐️ Air Canvas Web")

start = st.checkbox("Start Camera")
download = st.button("Download Drawing")

frame_placeholder = st.empty()
canvas_placeholder = st.empty()

if start:
    cap = cv2.VideoCapture(0)
    detector = GestureDetector()
    canvas = None
    prev_point = None

    while start:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]

        if canvas is None:
            canvas = DrawingCanvas(w, h)

        result = detector.process(frame)
        cursor = result.cursor

        if result.gesture == "draw" and cursor:
            if prev_point is None:
                prev_point = cursor
            canvas.draw_line(prev_point, cursor)
            prev_point = cursor
        else:
            prev_point = None

        output = blend_frames(frame, canvas.get_image())
        frame_placeholder.image(output, channels="BGR")

        if download:
            cv2.imwrite("drawing.png", canvas.get_image())
            st.download_button(
                "Download",
                open("drawing.png", "rb"),
                file_name="air_canvas.png"
            )

