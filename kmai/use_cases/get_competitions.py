from kmai.ports.competition_scrapper import CompetitionScrapper
from kmai.ports.csv_writer import CSVWriter 
from kmai.ports.kaggle_downloader import KaggleDownloader 
from kmai.ports.llm_caller import LLMCaller 

def get_competitions_embedding_csv(kaggle_downloader: KaggleDownloader, competition_scrapper: CompetitionScrapper, llm_caller: LLMCaller, csv_writer: CSVWriter):
    comp_df, comp_forums = kaggle_downloader.download_data()
    