import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
from kmai.ports.ikaggle_downloader import IKaggleDownloader


class KaggleDownloader(IKaggleDownloader):
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        COMPETITION = "Competitions"
        FORUMS = "ForumTopics"

        api = KaggleApi()
        api.authenticate()

        api.dataset_download_file(
            "kaggle/meta-kaggle", file_name=f"{COMPETITION}.csv", path="./data"
        )
        api.dataset_download_file(
            "kaggle/meta-kaggle", file_name=f"{FORUMS}.csv", path="./data"
        )

        self.extract_zip(COMPETITION)
        self.extract_zip(FORUMS)

        df_comp = pd.read_csv(f"./data/{COMPETITION}.csv")
        df_topics = pd.read_csv(f"./data/{FORUMS}.csv")

        return df_comp, df_topics

    def extract_zip(self, name):
        zip_path = f'./data/{name}.csv.zip'  
        extract_path = './data'  

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

KaggleDownloader().download_data()