import pandas as pd

from kmai.ports.icompetition_scrapper import ICompetitionScrapper
from kmai.ports.icsv_writer import ICSVWriter
from kmai.ports.ikaggle_downloader import IKaggleDownloader
from kmai.ports.illm_caller import ILLMCaller


def get_competitions_embedding_csv(
    kaggle_downloader: IKaggleDownloader,
    competition_scrapper: ICompetitionScrapper,
    llm_caller: ILLMCaller,
    csv_writer: ICSVWriter,
) -> pd.DataFrame:
    comp_df, comp_forums = kaggle_downloader.download_data()
    comp_df["url"] = [f"https://www.kaggle.com/c/{slug}" for slug in comp_df["Slug"]]
    comp_df["description"] = [competition_scrapper.get_competition_text(url) for url in comp_df["url"]]
    comp_df["desc_embedding"] = llm_caller.get_embeddings(comp_df["description"].tolist())

    return comp_df
