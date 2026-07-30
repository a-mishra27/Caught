# 📸 Caught – Auto Capture Smiling Face

Automatically captures a photo whenever the user smiles using **Python**, **OpenCV**, and **MediaPipe Face Mesh**.

## ✨ Features

- 😀 Real-time face detection
- 😊 Smile detection using MediaPipe Face Mesh landmarks
- 📷 Automatic image capture on smile
- 🔔 Camera shutter sound after capture
- ⚡ Fast and lightweight
- 🖥️ Real-time webcam preview

---

## 🛠️ Tech Stack

- Python 3.12
- OpenCV
- MediaPipe

---

## 📂 Project Structure

```
Caught/
│── smiling_selfie.py
│── camera_test.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/a-mishra27/Caught.git
cd Caught
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python smiling_selfie.py
```

---

## 📸 How It Works

1. Opens the webcam.
2. Detects the user's face using MediaPipe Face Mesh.
3. Tracks facial landmarks around the mouth.
4. Measures the distance between mouth landmarks.
5. Detects a smile when the distance exceeds a threshold.
6. Automatically captures and saves the image.

---

## 📚 Dependencies

- OpenCV
- MediaPipe


Install manually if needed:

```bash
pip install opencv-python mediapipe pyautogui
```

---

## 🎯 Future Improvements

- Multiple face detection
- Smile confidence score
- Countdown before capture
- Automatic image enhancement
- GUI using Tkinter or PyQt
- Save captured images with timestamps
- Live smile percentage indicator

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Amisha Mishra**

GitHub: https://github.com/a-mishra27
