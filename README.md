# 🎮 Gesture-Based Controller for Blasphemous (PC Game)

Control your *Blasphemous* game character using **hand gestures** via webcam!
This AI-powered controller uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to detect specific hand gestures and map them to in-game keyboard actions.

---

## 🧠 Features

* 👋 Real-time **hand gesture recognition** using MediaPipe
* 🎮 In-game actions mapped to gestures:

  * Move left/right
  * Jump (standard + directional)
  * Dodge
  * Attack
  * Parry
  * Heal
* 🖥️ Lightweight and responsive — runs in real-time on most systems

---

## 🔧 Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/harinandanmv/AI_HandGesture_GameControls_Using_OpenCV.git
cd AI_HandGesture_GameControls_Using_OpenCV
```

### 2. Install dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

### 3. Run the script

```bash
python gesture_controller.py
```

> **Note:** Ensure your webcam is connected and accessible.

---

## ✋ Gesture Mappings

| Gesture                       | Action           |
| ----------------------------- | ---------------- |
| All fingers up                | Dodge (`Shift`)  |
| Pinky only                    | Move Left (`A`)  |
| Pinky + Index                 | Jump Left        |
| Thumb only                    | Move Right (`D`) |
| Thumb + Index                 | Jump Right       |
| Index only                    | Jump (`Space`)   |
| Middle + Ring + Pinky         | Move Up (`W`)    |
| Ring + Pinky                  | Move Down (`S`)  |
| Index + Middle + Ring + Pinky | Heal (`F`)       |
| Middle + Ring                 | Parry (`R`)      |
| Fist (all down)               | Attack (`T`)     |

---

## 🛑 Exit Instructions

Press **`q`** to exit the application window.

---

## 🙌 Acknowledgements

* [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) by Google
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* OpenCV for real-time video feed handling

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and share.

---

## 👤 Author

**M V Harinandan**
📧 [harinandanmv11@gmail.com](mailto:harinandanmv11@gmail.com)
🌐 [LinkedIn](https://linkedin.com/in/harinandanmv) | [GitHub](https://github.com/harinandanmv)
