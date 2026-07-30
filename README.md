# 📸 Caught – Auto Capture Smiling Face

An AI-powered Python application that automatically captures a photo when a smile is detected using **MediaPipe Face Mesh** and **OpenCV**.

---

## 🚀 Features

- 😀 Real-time webcam feed
- 👤 Face detection using MediaPipe Face Mesh
- 😊 Smile detection based on facial landmarks
- 📷 Automatically captures an image when a smile is detected
- ⚡ Fast and lightweight implementation
- 💻 Simple and easy-to-use interface

---

## 🛠️ Tech Stack

- Python 3.12
- OpenCV
- MediaPipe

---

## 📁 Project Structure

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

### 1. Clone the repository

```bash
git clone https://github.com/a-mishra27/Caught.git
cd Caught
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python smiling_selfie.py
```

---

## 🧠 How It Works

1. Opens the webcam.
2. Detects the user's face using MediaPipe Face Mesh.
3. Tracks facial landmarks around the mouth.
4. Measures the distance between selected mouth landmarks.
5. Detects a smile based on the landmark distance.
6. Automatically captures the image when the smile threshold is reached.

---

## 📚 Dependencies

```
opencv-python
mediapipe==0.10.21
```

Or install manually:

```bash
pip install opencv-python mediapipe==0.10.21
```

---

## 📈 Future Enhancements

- 📸 Save images with timestamps
- 😀 Smile confidence indicator
- 👥 Multiple face detection
- ⏳ Countdown before capture
- 🎨 Modern graphical user interface
- ☁️ Cloud image storage
- 📱 Mobile application support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Amisha Mishra**

GitHub: https://github.com/a-mishra27
