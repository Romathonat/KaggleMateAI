import pandas as pd

from kmai.config import settings
from kmai.ports.icompetition_scrapper import ICompetitionScrapper
from kmai.ports.icsv_reader import ICSVReader
from kmai.ports.icsv_writer import ICSVWriter
from kmai.ports.ikaggle_downloader import IKaggleDownloader
from kmai.ports.illm_caller import ILLMCaller


def create_competitions_embedding_csv(
    kaggle_downloader: IKaggleDownloader,
    competition_scrapper: ICompetitionScrapper,
    llm_caller: ILLMCaller,
    csv_writer: ICSVWriter,
) -> pd.DataFrame:
    """
    Download the competition file and create the COMPETITIONS_WITH_EMBEDDINGS file. Populate the first INITIAL_COMPETITION_NUMBER_TO_EMBED embeddings
    """
    comp_df, comp_forums = kaggle_downloader.download_data()
    comp_df["url"] = [url_builder(slug) for slug in comp_df["Slug"]]
    comp_df["description"] = None
    comp_df["desc_embedding"] = None

    comp_df_head = comp_df.head(settings.INITIAL_COMPETITION_NUMBER_TO_EMBED).copy()

    comp_df_head["description"] = [competition_scrapper.get_competition_text(url) for url in comp_df_head["url"]]
    comp_df_head["desc_embedding"] = llm_caller.get_embeddings(comp_df_head["description"].tolist())

    comp_df.update(comp_df_head)

    csv_writer.write_csv(comp_df, f"{settings.DATA_DIR / settings.COMPETITIONS_WITH_EMBEDDINGS}.csv")

    return comp_df


def url_builder(slug: str) -> str:
    return f"{settings.KAGGLE_URL}{slug}"


def update_competitions_embedding(
    competition_scrapper: ICompetitionScrapper, llm_caller: ILLMCaller, csv_reader: ICSVReader, csv_writer: ICSVWriter
):
    comp_with_embedding_df = csv_reader.read_csv(f"{settings.DATA_DIR / settings.COMPETITIONS_WITH_EMBEDDINGS}")
    comp_with_embedding_df_filtered = comp_with_embedding_df[comp_with_embedding_df["desc_embedding"].isna()]

    for i, (index, row) in enumerate(comp_with_embedding_df_filtered.iterrows()):
        url = url_builder(comp_with_embedding_df_filtered.at[index, "Slug"])
        comp_with_embedding_df.at[index, "description"] = competition_scrapper.get_competition_text(url)
        comp_with_embedding_df.at[index, "desc_embedding"] = llm_caller.get_embeddings(
            [comp_with_embedding_df.at[index, "description"]]
        )

        if i % settings.BATCH_SIZE == 0:
            csv_writer.write_csv(
                comp_with_embedding_df, f"{settings.DATA_DIR / settings.COMPETITIONS_WITH_EMBEDDINGS}.csv"
            )

    return comp_with_embedding_df
