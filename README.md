# 🧠 Emotion Intelligence System (EIS)

A real-time AI-powered Emotion Recognition System that detects human emotions from webcam feed using Deep Learning (CNN) and provides analytics through a live dashboard.

---

## 🚀 Demo Preview

> Real-time facial emotion detection with live webcam feed + emotion logging + analytics dashboard.

---

## 🎯 Features

- 🎥 Real-time webcam-based face detection (OpenCV)
- 😃 Emotion classification using CNN model (Keras/TensorFlow)
- 📊 Live emotion logging system (CSV-based tracking)
- 📈 Streamlit dashboard for emotion analytics
- ⏱️ Confidence scoring for predictions
- 🧠 Supports 7 emotions: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral

---

## 🧠 Tech Stack

- Python 🐍
- TensorFlow / Keras
- OpenCV
- NumPy & Pandas
- Streamlit (Dashboard)
- Haar Cascade (Face Detection)

---

## 🏗️ System Architecture

1. Webcam captures live video
2. OpenCV detects face regions
3. CNN model predicts emotion
4. Results logged every 5 seconds
5. Streamlit dashboard visualizes insights

---

## 📊 Emotion Classes

| Label | Emotion |
|------|--------|
| 0 | Angry 😡 |
| 1 | Disgust 🤢 |
| 2 | Fear 😨 |
| 3 | Happy 😄 |
| 4 | Sad 😢 |
| 5 | Surprise 😲 |
| 6 | Neutral 😐 |

---

## 📁 Project Structure
EIS/
├── models/
│ └── emotion_model_final.h5
│
├── src/
│ ├── webcam_detector.py
│ ├── dashboard.py
│ └── emotion_logger.py
│
├── logs/
│ └── emotion_log.csv
│
├── requirements.txt
└── README.md

# 🧠 Emotion Intelligence System (EIS)

> Real-time AI emotion detection using CNN + OpenCV + Streamlit

# install
git clone https://github.com/popcorngirl94/Emotion-Intelligence-System-EIS-.git
cd EIS

# create venv
python -m venv env
env\Scripts\activate   # Windows

# install dependencies
pip install -r requirements.txt

# run webcam emotion detector
python src/webcam_detector.py

# run dashboard
streamlit run src/dashboard.py

## 📥 Trained Model

Due to GitHub's file size limitations, the trained model files are not stored directly in this repository.

Download the models and place them inside the `models/` directory before running the application.

link: https://drive.google.com/drive/folders/1CS9GuffQndwrLNGK7Thg3RJGnR4Ed9T-?usp=sharing

# features
- emotion detection from webcam
- live face tracking
- emotion logging system
- analytics dashboard

# future
- real-time streaming dashboard
- better deep learning model (LSTM / Transformer)
- database instead of CSV
- mobile camera support

# author
Grishma Shrestha
AI/ML Enthusiast | Data Science Learner | Web Developer

# support
⭐ star the repo if you like it
