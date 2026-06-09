from pathlib import Path
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "models" / "emotion_model_final.h5"

print("Loading model from:", model_path)

model = load_model(model_path)

print("Model loaded successfully!")

print(model.input_shape)
print(model.output_shape)