import os

from kmai.adapters.competition_scrapper import CompetitionScrapper
from kmai.adapters.csv_handler import CSVHandler 
from kmai.adapters.kaggle_downloader import KaggleDownloader
from kmai.adapters.llm_caller import LLMCaller
from kmai.config import settings
from kmai.use_cases.data_preprocessing import (
    update_competitions_csv,
    update_competitions_descriptions,
)

if __name__ == "__main__":
    update_competitions_csv(KaggleDownloader(), CSVHandler())
    update_competitions_descriptions(CompetitionScrapper(), CSVHandler())
