import os 

from kmai.adapters.competition_scrapper import CompetitionScrapper
from kmai.adapters.csv_writer import CSVWriter
from kmai.adapters.llm_caller import LLMCaller
from kmai.adapters.kaggle_downloader import KaggleDownloader 

from kmai.config import settings

from kmai.use_cases.get_competitions import create_competitions_embedding_csv 

if __name__ == "__main__":
    if not os.path.exists(f"./data/{settings.COMPETITIONS_WITH_EMBEDDINGS}"):
        create_competitions_embedding_csv(KaggleDownloader(), CompetitionScrapper(), LLMCaller(), CSVWriter())
    else:
        pass