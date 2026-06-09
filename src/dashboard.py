import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "logs" / "emotion_log.csv"

st.title("🧠 Emotional Intelligence Dashboard")

if not log_file.exists():
    st.warning("No emotion logs found yet.")
    st.stop()

# -----------------------------
# FIX: correct column structure
# -----------------------------
df = pd.read_csv(log_file, header=None)
df.columns = ["timestamp", "emotion", "confidence"]

# convert confidence to numeric (safe)
df["confidence"] = pd.to_numeric(df["confidence"], errors="coerce")

st.subheader("Recent Logs")
st.dataframe(df.tail(20))

st.subheader("Emotion Distribution")
emotion_counts = df["emotion"].value_counts()
st.bar_chart(emotion_counts)

st.subheader("Most Frequent Emotion")
st.success(emotion_counts.idxmax())

st.subheader("Average Confidence")
st.metric(
    "Confidence",
    f"{df['confidence'].mean() * 100:.2f}%"
)