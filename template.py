# template.py
from pathlib import Path

print("🚀 Setting up Emotion Intelligence Project...")

# =========================
# Directories
# =========================
directories = [
    "Data_Sets",
    "env",  # optional (usually created via venv command)
    
    # Core project folders
    "ML_Model",
    "Evaluation_Metrics",

    # Scripts / App
    "src",
    
    # Notebooks
    "notebooks",

    # Outputs
    "artifacts/models",
    "artifacts/logs",
    "artifacts/reports",
]

# =========================
# Files
# =========================
files = [
    # Main files
    "Emotion_Detection.py",
    "Emotion_Intelligence.ipynb",
    "requirements.txt",
    "README.md",

    # ML files
    "ML_Model/model.py",
    "ML_Model/train.py",
    "ML_Model/predict.py",

    # Evaluation
    "Evaluation_Metrics/metrics.py",

    # Source structure
    "src/__init__.py",
    "src/utils.py",
    "src/logger.py",

    # Notebooks
    "notebooks/EDA.ipynb",

    # Config
    "config.yaml",

    # Optional deployment
    "app.py",
]

# =========================
# Functions
# =========================
def create_directories(dir_list):
    print("\n📁 Creating directories...\n")
    for dir_path in dir_list:
        try:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            print(f"✅ {dir_path}")
        except Exception as e:
            print(f"❌ Failed: {dir_path} | {e}")

def create_files(file_list):
    print("\n📄 Creating files...\n")
    for file_path in file_list:
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            if not path.exists():
                path.touch()
                print(f"✅ Created: {file_path}")
            else:
                print(f"⚡ Exists: {file_path}")
        except Exception as e:
            print(f"❌ Failed: {file_path} | {e}")

# =========================
# Main
# =========================
def main():
    print("🔥 Project Setup Started")
    create_directories(directories)
    create_files(files)
    print("\n🎉 Project Structure Ready!")

if __name__ == "__main__":
    main()