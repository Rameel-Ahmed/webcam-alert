import cv2
import streamlit as st
from datetime import datetime

# Streamlit app title
st.title("Motion Detector")

# Button to start camera stream
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])  # Placeholder for video frame
    camera = cv2.VideoCapture(0)  # Open webcam

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Streamlit

        # Get current timestamp
        now = datetime.now()

        # Overlay day on frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)

        # Overlay time on frame
        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)

        # Display the updated frame
        streamlit_image.image(frame)
