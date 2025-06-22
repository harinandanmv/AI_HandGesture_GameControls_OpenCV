# 🎮 Gesture-Based Controller for Blasphemous (PC Game)

Control your *Blasphemous* game character using **hand gestures** via webcam!
This AI-powered controller leverages **MediaPipe**, **OpenCV**, and **PyAutoGUI** to detect real-time hand gestures and seamlessly convert them into keyboard actions, allowing a unique and immersive way to interact with the game — **no physical controller needed!**

---

## 🧠 Features

* 👋 Real-time **hand gesture recognition** powered by MediaPipe’s advanced hand tracking technology.
* 🎮 Smart gesture-to-keyboard mapping to perform various in-game actions such as:

  * Smooth movement in both directions (left and right)
  * Jump actions (vertical and directional)
  * Quick dodge using a single gesture
  * Melee or ranged attack triggering
  * Defensive maneuvers like parry
  * Instant use of healing abilities
* 🖥️ Lightweight and responsive system, capable of running on most PCs with a basic webcam and Python environment.

---

## 🔧 Tech Stack

* **Python** – Core scripting and logic
* **OpenCV** – Real-time video feed capture and processing
* **MediaPipe** – Hand landmark detection and tracking
* **PyAutoGUI** – Simulates keyboard input for gameplay control

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/harinandanmv/AI_HandGesture_GameControls_Using_OpenCV.git
cd AI_HandGesture_GameControls_Using_OpenCV
```

### 2. Install dependencies

Make sure you have Python installed. Then, run:

```bash
pip install opencv-python mediapipe pyautogui
```

### 3. Run the script

```bash
python app.py
```

> ⚠️ **Note:** Ensure your webcam is properly connected. Close any other application using the camera before running this script.

---

## ✋ Gesture Mappings

These are the hand gestures recognized by the system and the in-game actions they perform:

| Gesture                       | Mapped Action    |
| ----------------------------- | ---------------- |
| All fingers up                | Dodge (`Shift`)  |
| Pinky only                    | Move Left (`A`)  |
| Pinky + Index                 | Jump Left        |
| Thumb only                    | Move Right (`D`) |
| Thumb + Index                 | Jump Right       |
| Index only                    | Jump (`Space`)   |
| Middle + Ring + Pinky         | Move Up (`W`)    |
| Ring + Pinky                  | Move Down (`S`)  |
| Index + Middle + Ring + Pinky | Use Heal (`F`)   |
| Middle + Ring                 | Parry (`R`)      |
| Fist (no fingers extended)    | Attack (`T`)     |

> ⏱️ Each gesture is interpreted with a short cooldown to avoid repeated accidental triggers.

---

## 📁 Project Structure

```plaintext
AI_HandGesture_GameControls_Using_OpenCV/
│
├── app.py                  # Main Python script for gesture recognition and game control
├── README.md               # Project documentation
└── requirements.txt        # File listing all dependencies
```

---

## 🛑 Exit Instructions

To safely exit the application, press the **`q`** key in the camera window or close the display window directly.

---

## 🙌 Acknowledgements

Special thanks to the following tools and libraries that made this project possible:

* [**MediaPipe Hands**](https://google.github.io/mediapipe/solutions/hands.html) – For robust hand detection and tracking.
* [**PyAutoGUI**](https://pyautogui.readthedocs.io/en/latest/) – For simulating keyboard events programmatically.
* [**OpenCV**](https://opencv.org/) – For real-time image processing and webcam feed integration.

---

## 👤 Author

**M V Harinandan**
📧 [harinandanmv11@gmail.com](mailto:harinandanmv11@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/harinandanmv) | [GitHub](https://github.com/harinandanmv)
