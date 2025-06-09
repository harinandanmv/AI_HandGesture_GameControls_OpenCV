# ---------------------------------------------
# Gesture-Based Controller for Blasphemous Game
# ---------------------------------------------
# This Python script uses computer vision (MediaPipe + OpenCV) and pyautogui
# to detect specific hand gestures through webcam input and map them to in-game
# keyboard actions in the *Blasphemous* game.
# 
# Recognized gestures trigger actions like:
# - Movement (left/right)
# - Jumping (single or directional)
# - Dodging
# - Attacking
# - Using abilities (like health and parry)
#
# Run this script and control your character using hand gestures!
# Press 'q' to quit the application.

import cv2
import mediapipe as mp
import pyautogui
import time

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

last_action_time = 0
action_cooldown = 0.5  # seconds

movement = {'left': False, 'right': False}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    fingers_up = []

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]
        lm_list = []

        h, w, _ = frame.shape
        for id, lm in enumerate(handLms.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        if len(lm_list) == 21:
            # Thumb (horizontal)
            if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                fingers_up.append(1)
            else:
                fingers_up.append(0)

            # Fingers (vertical)
            for i in range(1, 5):
                if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                    fingers_up.append(1)
                else:
                    fingers_up.append(0)

            now = time.time()

            # All fingers up → press Shift once per cooldown
            if fingers_up == [1, 1, 1, 1, 1]:
                if now - last_action_time > action_cooldown:
                    print("Dodge")
                    pyautogui.press('shift')
                    last_action_time = now

            # Move left: pinky only
            elif fingers_up == [0, 0, 0, 0, 1]:
                if not movement['left']:
                    print("Start moving left")
                    pyautogui.keyDown('a')
                    movement['left'] = True
                if movement['right']:
                    pyautogui.keyUp('d')
                    movement['right'] = False

            # Jump left: pinky + index
            elif fingers_up == [0, 1, 0, 0, 1]:
                if movement['left']:
                    if now - last_action_time > action_cooldown:
                        print("Jump Left")
                        pyautogui.keyUp('a')
                        pyautogui.hotkey('space', 'a')
                        pyautogui.keyDown('a')
                        last_action_time = now

            # Jump:
            elif fingers_up == [0, 1, 0, 0, 0]:
                if now - last_action_time > action_cooldown:
                    print("Jump")
                    pyautogui.press('space')
                    last_action_time = now

            # Move up:
            elif fingers_up == [0, 0, 1, 1, 1]:
                if now - last_action_time > action_cooldown:
                    print("Up")
                    pyautogui.press('w')
                    last_action_time = now

            # Move down:
            elif fingers_up == [0, 0, 0, 1, 1]:
                if now - last_action_time > action_cooldown:
                    print("Down")
                    pyautogui.press('s')
                    last_action_time = now

            # Move right: thumb only
            elif fingers_up == [1, 0, 0, 0, 0]:
                if not movement['right']:
                    print("Start moving right")
                    pyautogui.keyDown('d')
                    movement['right'] = True
                if movement['left']:
                    pyautogui.keyUp('a')
                    movement['left'] = False

            # Jump right: thumb + index
            elif fingers_up == [1, 1, 0, 0, 0]:
                if movement['right']:
                    if now - last_action_time > action_cooldown:
                        print("Jump Right")
                        pyautogui.keyUp('d')
                        pyautogui.hotkey('space', 'd')
                        pyautogui.keyDown('d')
                        last_action_time = now

            # New: Press F for [0, 1, 1, 1, 1]
            elif fingers_up == [0, 1, 1, 1, 1]:
                if now - last_action_time > action_cooldown:
                    print("Health")
                    pyautogui.press('f')
                    last_action_time = now

            # New: Press R for [0, 0, 1, 1, 0]
            elif fingers_up == [0, 0, 1, 1, 0]:
                if now - last_action_time > action_cooldown:
                    print("Parry")
                    pyautogui.press('r')
                    last_action_time = now

            # New: Press T for [0, 0, 0, 0, 0]
            elif fingers_up == [0, 0, 0, 0, 0]:
                if now - last_action_time > action_cooldown:
                    print("Attack")
                    pyautogui.press('t')
                    last_action_time = now

            else:
                # Stop all movement if no recognized gesture
                if movement['right']:
                    print("Stop moving right")
                    pyautogui.keyUp('d')
                    movement['right'] = False
                if movement['left']:
                    print("Stop moving left")
                    pyautogui.keyUp('a')
                    movement['left'] = False

    else:
        # No hand detected — stop all movement
        if movement['right']:
            pyautogui.keyUp('d')
            movement['right'] = False
        if movement['left']:
            pyautogui.keyUp('a')
            movement['left'] = False

    cv2.imshow("Blasphemous Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

