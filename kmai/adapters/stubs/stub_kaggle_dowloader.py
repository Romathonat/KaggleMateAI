import pandas as pd

from kmai.ports.kaggle_downloader import KaggleDownloader


class StubKaggleDownloader(KaggleDownloader):
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        df_comp = pd.DataFrame(
            {"Id": [1], "Slug": ["Eurovision2010"], "ForumId": [1], "Title": ["Eurovision Prediction Competition"]}
        )

        df_topics = pd.DataFrame({"Id": [1], "ForumId": [1], "Score": [12], "TotalMessages": [4], "TotalReplies": [3]})

        return df_comp, df_topics
