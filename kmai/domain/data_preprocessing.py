import logging

import pandas as pd
from selenium.common.exceptions import TimeoutException

from kmai.config import settings
from kmai.ports.icsv_handler import ICSVHandler
from kmai.ports.ikaggle_downloader import IKaggleDownloader


def url_builder(slug: str) -> str:
    return f"{settings.KAGGLE_URL}{slug}"


def get_description(competition_scrapper, url):
    try:
        return competition_scrapper.get_competition_text(url)
    except TimeoutException:
        return None


def update_competitions_descriptions(competition_scrapper, csv_handler):
    comp_df = csv_handler.read_csv(
        settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS
    )
    comp_df["description"] = comp_df["description"].astype("object")
    comp_df["url"] = comp_df["url"].astype("object")

    indices_to_update = [
        index
        for index, description in zip(comp_df.index, comp_df["description"])
        if pd.isna(description)
    ]

    for i, index in enumerate(indices_to_update):
        url = url_builder(comp_df.at[index, "Slug"])
        comp_df.at[index, "url"] = url

        description = get_description(competition_scrapper, url)
        if description is None:
            continue

        comp_df.at[index, "description"] = description

        if i % settings.BATCH_SIZE == 0:
            logging.info(f"Processing batch {i // settings.BATCH_SIZE + 1}")
            csv_handler.write_csv(
                comp_df, settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS
            )

    return comp_df


def update_competitions_csv(
    kaggle_downloader: IKaggleDownloader, csv_handler: ICSVHandler
):
    df_comp_new, df_topic_new = kaggle_downloader.download_data()
    if csv_handler.exists(settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS):
        df_comp_to_update = csv_handler.read_csv(
            settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS
        )
    else:
        df_comp_to_update = df_comp_new.copy()

    csv_handler.remove(settings.DATA_DIR / settings.COMPETITIONS_CSV)

    df_comp_new["description"] = ""
    df_comp_new["url"] = ""
    df_comp_new["date_to_datastore"] = ""

    df_out_comp = pd.concat([df_comp_to_update, df_comp_new])
    df_out_comp.drop_duplicates(subset=["Id"], keep="first", inplace=True)
    df_out_comp.reset_index(drop=True, inplace=True)

    csv_handler.write_csv(
        df_out_comp, settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS
    )
    csv_handler.write_csv(df_topic_new, settings.DATA_DIR / settings.FORUMS_CSV)

    return df_out_comp, df_topic_new
