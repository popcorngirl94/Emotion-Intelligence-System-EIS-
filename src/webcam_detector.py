import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # force CPU mode (prevents GPU issues)

import cv2
import numpy as np
import time
from pathlib import Path
from tensorflow.keras.models import load_model
from emotion_logger import log_emotion

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "models" / "emotion_model_final.h5"

print("Loading model from:", model_path)

model = load_model(model_path)

print("Model loaded successfully!")

# -----------------------------
# Emotion Labels
# -----------------------------
emotion_labels = {
    0: "Angry",
    1: "Disgust",
    2: "Fear",
    3: "Happy",
    4: "Sad",
    5: "Surprise",
    6: "Neutral"
}

# -----------------------------
# Face Detector
# -----------------------------
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# Timer for logging
# -----------------------------
last_logged = 0

# -----------------------------
# Webcam (FIXED)
# -----------------------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("ERROR: Cannot access webcam.")
    exit()

print("Webcam started successfully!")

# -----------------------------
# Main Loop
# -----------------------------
while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("Warning: Failed to grab frame")
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        try:
            face = cv2.resize(face, (48, 48))
        except:
            continue

        face = face.astype("float32") / 255.0
        face = np.expand_dims(face, axis=-1)
        face = np.expand_dims(face, axis=0)

        prediction = model.predict(face, verbose=0)

        confidence = float(np.max(prediction))
        emotion_idx = int(np.argmax(prediction))
        emotion = emotion_labels.get(emotion_idx, "Unknown")

        # -----------------------------
        # Log emotion every 5 seconds
        # -----------------------------
        current_time = time.time()
        if current_time - last_logged > 5:
            log_emotion(emotion, confidence)
            last_logged = current_time
            print(f"Logged: {emotion} ({confidence:.2f})")

        # -----------------------------
        # Confidence filter
        # -----------------------------
        display_emotion = emotion
        if confidence < 0.50:
            display_emotion = "Uncertain"

        label = f"{display_emotion} ({confidence:.2f})"

        # Draw rectangle + label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Emotion Intelligence System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()