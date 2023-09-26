import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from kmai.ports.ikaggle_downloader import IKaggleDownloader


class StubKaggleDownloader(IKaggleDownloader):
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_file(
            "kaggle/meta-kaggle/download?datasetVersionNumber=1131", file_name="Competitions.csv", path="./data"
        )

        api.dataset_download_file(
            "kaggle/meta-kaggle/download?datasetVersionNumber=1131", file_name="ForumTopics.csv", path="./data"
        )

        pd.read_csv("")

        return df_comp, df_topics
