import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "emotion_log.csv"


def log_emotion(emotion, confidence):

    row = {
        "timestamp": datetime.now(),
        "emotion": emotion,
        "confidence": float(confidence)
    }

    df = pd.DataFrame([row])

    if LOG_FILE.exists():
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(LOG_FILE, index=False)

    print(f"Logged: {emotion} ({confidence:.2f})")