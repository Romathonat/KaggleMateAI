import os

from kmai.adapters.competition_scrapper import CompetitionScrapper
from kmai.adapters.csv_reader import CSVReader
from kmai.adapters.csv_writer import CSVWriter
from kmai.adapters.kaggle_downloader import KaggleDownloader
from kmai.adapters.llm_caller import LLMCaller
from kmai.config import settings
from kmai.use_cases.data_preprocessing import (
    update_competitions_csv,
    update_competitions_descriptions,
)

if __name__ == "__main__":
    update_competitions_csv(KaggleDownloader(), CSVReader(), CSVWriter())
    update_competitions_descriptions(CompetitionScrapper(), CSVReader(), CSVWriter())
