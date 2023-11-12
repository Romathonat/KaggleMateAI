from kmai.adapters.competition_scrapper import CompetitionScrapper
from kmai.adapters.csv_handler import CSVHandler
from kmai.adapters.kaggle_downloader import KaggleDownloader
from kmai.domain.data_preprocessing import (
    update_competitions_csv,
    update_competitions_descriptions,
)

if __name__ == "__main__":
    update_competitions_csv(KaggleDownloader(), CSVHandler())
    update_competitions_descriptions(CompetitionScrapper(), CSVHandler())
