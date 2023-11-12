from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
FAISS_DIR = DATA_DIR / "faiss_index"
INITIAL_COMPETITION_NUMBER_TO_DESCRIBE = 10
BATCH_SIZE = 20
COMPETITIONS_WITH_DESCRIPTIONS = "competitions_with_descriptions.csv"
KAGGLE_URL = "https://www.kaggle.com/c/"
COMPETITIONS_CSV = "Competitions.csv"
FORUMS_CSV = "Forums.csv"
