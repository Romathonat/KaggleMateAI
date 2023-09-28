import os

from kmai.adapters.competition_scrapper import CompetitionScrapper
from kmai.adapters.csv_reader import CSVReader
from kmai.adapters.csv_writer import CSVWriter
from kmai.adapters.kaggle_downloader import KaggleDownloader
from kmai.adapters.llm_caller import LLMCaller
from kmai.config import settings
from kmai.use_cases.data_preprocessing import (
    create_competitions_embedding_csv,
    update_competion_csv,
    update_competitions_embedding,
)

if __name__ == "__main__":
    if not os.path.exists(f"./data/{settings.COMPETITIONS_WITH_EMBEDDINGS}"):
        create_competitions_embedding_csv(KaggleDownloader(), CompetitionScrapper(), LLMCaller(), CSVWriter())
    else:
        update_competion_csv(KaggleDownloader(), CSVReader(), CSVWriter())
        update_competitions_embedding(CompetitionScrapper(), LLMCaller(), CSVReader(), CSVWriter())
