import cv2
import time
import glob
import os
from emailing import send_email
from threading import Thread

# Start video capture from webcam
video = cv2.VideoCapture(0)
time.sleep(1)  # Wait for camera to initialize

first_frame = None  # Reference frame for motion detection
status_list = []  # Track object presence status over time
count = 1  # Counter for saving images

# Function to delete all saved images
def clean_folder():
    print("clean_folder function started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("clean_folder function ended")

# Main loop to process video frames
while True:
    status = 0  # Default: no motion
    check, frame = video.read()

    # Convert frame to grayscale and apply Gaussian blur to reduce noise
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Set first frame as reference for motion comparison
    if first_frame is None:
        first_frame = gray_frame_gau

    # Get difference between current and reference frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # Threshold and dilate to highlight motion areas
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Show the processed frame
    cv2.imshow("My video", dil_frame)

    # Find contours to detect moving objects
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:  # Ignore small movements
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():  # If object is detected
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)  # Save the frame
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]  # Pick middle image for email

    # Update status list (latest 2 states)
    status_list.append(status)
    status_list = status_list[-2:]

    # If motion just ended (1 -> 0), send email with image
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        clean_thread = Thread(target=clean_folder)
        email_thread.daemon = True
        clean_thread.daemon = True
        email_thread.start()

    print(status_list)

    # Display the frame with rectangles
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):  # Press 'q' to exit
        break

video.release()

# Clean up images after stopping
clean_thread.start_
