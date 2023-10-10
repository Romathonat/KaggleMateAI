from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

INITIAL_COMPETITION_NUMBER_TO_DESCRIBE = 10
BATCH_SIZE = 20
COMPETITIONS_WITH_DESCRIPTIONS = "competitions_with_embeddings"
KAGGLE_URL = "https://www.kaggle.com/c/"
COMPETITIONS_CSV = "Competitions.csv"
FORUMS_CSV = "Forums.csv"
