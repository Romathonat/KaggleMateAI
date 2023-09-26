from kmai.ports.competition_scrapper import CompetitionScrapper
from kmai.ports.csv_writer import CSVWriter 
from kmai.ports.kaggle_downloader import KaggleDownloader 
from kmai.ports.llm_caller import LLMCaller 

import pandas as pd

def get_competitions_embedding_csv(kaggle_downloader: KaggleDownloader, competition_scrapper: CompetitionScrapper, llm_caller: LLMCaller, csv_writer: CSVWriter) -> pd.DataFrame:
    comp_df, comp_forums = kaggle_downloader.download_data()
    comp_df["url"] = [f"https://www.kaggle.com/c/{slug}" for slug in comp_df["Slug"]]
    comp_df["description"] = [competition_scrapper.get_competition_text(url) for url in comp_df["url"]]
    comp_df["desc_embedding"] = llm_caller.get_embedings(comp_df["description"].tolist())

    return comp_df