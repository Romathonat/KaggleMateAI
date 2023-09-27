import pandas as pd

from kmai.ports.ikaggle_downloader import IKaggleDownloader


class StubKaggleDownloader(IKaggleDownloader):
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        df_comp = pd.DataFrame(
            {
                "Id": [1] * 10,
                "Slug": ["Eurovision2010"] * 10,
                "ForumId": [1] * 10,
                "Title": ["Eurovision Prediction Competition"] * 10,
            }
        )

        df_topics = pd.DataFrame(
            {
                "Id": [1] * 10,
                "ForumId": [1] * 10,
                "Score": [12] * 10,
                "TotalMessages": [4] * 10,
                "TotalReplies": [3] * 10,
            }
        )

        return df_comp, df_topics
