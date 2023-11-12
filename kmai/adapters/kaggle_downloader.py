import os
import zipfile

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from kmai.config import settings
from kmai.ports.ikaggle_downloader import IKaggleDownloader


class KaggleDownloader(IKaggleDownloader):
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_file(
            "kaggle/meta-kaggle",
            file_name=f"{settings.COMPETITIONS_CSV}",
            path=settings.DATA_DIR,
        )
        api.dataset_download_file(
            "kaggle/meta-kaggle",
            file_name=f"{settings.FORUMS_CSV}",
            path=settings.DATA_DIR,
        )

        self.extract_zip(settings.COMPETITIONS_CSV)
        self.extract_zip(settings.FORUMS_CSV)

        os.remove(f"{settings.DATA_DIR / settings.COMPETITIONS_CSV}.zip")
        os.remove(f"{settings.DATA_DIR / settings.FORUMS_CSV}.zip")

        df_comp = pd.read_csv(f"{settings.DATA_DIR / settings.COMPETITIONS_CSV}")
        df_topics = pd.read_csv(f"{settings.DATA_DIR / settings.FORUMS_CSV}")

        return df_comp, df_topics

    def extract_zip(self, name):
        zip_path = f"./data/{name}.zip"
        extract_path = "./data"

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
