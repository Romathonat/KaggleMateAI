import pandas as pd

from kmai.ports.icompetition_scrapper import ICompetitionScrapper
from kmai.ports.icsv_writer import ICSVWriter
from kmai.ports.icsv_reader import ICSVReader 
from kmai.ports.ikaggle_downloader import IKaggleDownloader
from kmai.ports.illm_caller import ILLMCaller
from kmai.config import settings

def create_competitions_embedding_csv(
    kaggle_downloader: IKaggleDownloader,
    competition_scrapper: ICompetitionScrapper,
    llm_caller: ILLMCaller,
    csv_writer: ICSVWriter,
) -> pd.DataFrame:
    comp_df, comp_forums = kaggle_downloader.download_data()
    comp_df["url"] = [f"https://www.kaggle.com/c/{slug}" for slug in comp_df["Slug"]]

    comp_df = comp_df.head(settings.INITIAL_COMPETITION_NUMBER)

    comp_df["description"] = [competition_scrapper.get_competition_text(url) for url in comp_df["url"]]
    comp_df["desc_embedding"] = llm_caller.get_embeddings(comp_df["description"].tolist())

    csv_writer.write_csv(comp_df, f"./data/{settings.COMPETITIONS_WITH_EMBEDDINGS}.csv")

    return comp_df
    
def update_competitions_embedding(
    competition_scrapper: ICompetitionScrapper,
    llm_caller: ILLMCaller,
    csv_reader: ICSVReader,
    csv_writer: ICSVWriter):
    # TODO: we read data, we filter lines having no embedding, we compute them for "batch" size.
    pass
