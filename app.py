import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image
from io import BytesIO

st.title("🖐️ Air Drawing with Thumb-to-Index-Base Click Gesture")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

# Canvas size
canvas_height, canvas_width = 480, 640

# Session state initialization
if "canvas" not in st.session_state:
    st.session_state.canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
if "history" not in st.session_state:
    st.session_state.history = []
if "drawing_done" not in st.session_state:
    st.session_state.drawing_done = False

# Buttons
col1, col2, col3, col4 = st.columns(4)
if col1.button("🧼 Clear Canvas"):
    st.session_state.canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    st.session_state.history = []
    st.session_state.drawing_done = False

if col2.button("↩️ Undo"):
    if st.session_state.history:
        st.session_state.canvas = st.session_state.history.pop()

if col3.button("✅ Done Drawing"):
    st.session_state.drawing_done = True

# Webcam display
frame_placeholder = st.empty()

# Start webcam
cap = cv2.VideoCapture(0)
prev_x, prev_y = None, None

if not cap.isOpened():
    st.error("Cannot open webcam")
else:
    try:
        while not st.session_state.drawing_done:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to read from webcam")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    h, w, _ = frame.shape

                    # Get landmark positions
                    index_tip = hand_landmarks.landmark[8]  # Drawing point
                    thumb_tip = hand_landmarks.landmark[4]
                    index_base = hand_landmarks.landmark[5]

                    # Convert to pixels
                    ix, iy = int(index_tip.x * w), int(index_tip.y * h)
                    tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
                    ibx, iby = int(index_base.x * w), int(index_base.y * h)

                    # Show fingertip marker
                    cv2.circle(frame, (ix, iy), 10, (0, 255, 255), -1)

                    # Distance between thumb tip and index base
                    touch_distance = np.hypot(tx - ibx, ty - iby)

                    # If touching, start drawing
                    if touch_distance < 30:
                        if prev_x is not None and prev_y is not None:
                            st.session_state.history.append(st.session_state.canvas.copy())
                            cv2.line(st.session_state.canvas, (prev_x, prev_y), (ix, iy), (255, 255, 255), 5)
                        prev_x, prev_y = ix, iy
                    else:
                        prev_x, prev_y = None, None  # stop drawing

                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            else:
                prev_x, prev_y = None, None

            # Combine webcam and drawing
            combined = cv2.addWeighted(frame, 0.5, st.session_state.canvas, 0.5, 0)
            combined_rgb = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(combined_rgb, channels="RGB")

    except KeyboardInterrupt:
        cap.release()
    finally:
        cap.release()

# After drawing is done
if st.session_state.drawing_done:
    st.subheader("🎨 Drawing Complete")
    canvas_image = Image.fromarray(cv2.cvtColor(st.session_state.canvas, cv2.COLOR_BGR2RGB))
    st.image(canvas_image, caption="Your Drawing", use_column_width=True)

    # Download option
    buf = BytesIO()
    canvas_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="💾 Download Drawing",
        data=byte_im,
        file_name="drawing.png",
        mime="image/png"
    )
