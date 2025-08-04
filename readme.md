# 🕵️ Motion Detection with Email Alerts and Streamlit Interface

This project is a Python-based **Motion Detection System** using **OpenCV** that detects motion through a webcam, captures an image when motion is detected, and sends an **email alert with the captured image**. A **Streamlit dashboard** is also included for live camera viewing with date and time overlays.

---

## 📸 Features

- ✅ Real-time motion detection using a webcam.
- 📧 Sends email alerts with captured images when motion is detected.
- 🧹 Automatically cleans up saved images.
- 🌐 Live video feed with time and day displayed using **Streamlit**.
- 💻 Multi-threaded emailing and cleanup to avoid freezing the main video feed.

---

## 🛠️ Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```text
opencv-python
streamlit
```

📌 You will also need a custom `emailing.py` module that handles sending email via SMTP.

---


## 📬 Notes

- Make sure the `images/` directory exists. Create it manually if needed.
- Motion is detected based on frame differencing and contour size.
- Tune the contour area threshold (`5000`) and blur size if needed.

---

## 🧹 Cleanup

Old images are automatically deleted after motion ends, using a background thread.

---

## 📧 Troubleshooting Email

- If using Gmail, enable **"Allow less secure apps"** (or use **App Passwords**).
- Check your firewall or antivirus if emails or camera feed doesn't work.

---

## 📄 License

This project is open-source and free to use under the MIT License.
