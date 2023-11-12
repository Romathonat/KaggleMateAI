import pandas as pd

from kmai.ports.icsv_handler import ICSVHandler


class StubCSVHandler(ICSVHandler):
    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "Id": [1, 2, 3],
                "ForumId": [1, 2, 3],
                "Title": ["Title 1", "Title 2", "Title 3"],
                "description": ["description", None, None],
                "Slug": ["slug1", "slug2", "slug3"],
                "url": ["my_url", None, None],
                "date_to_datastore": [None, None, None],
            }
        )

    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        return True

    def exists(self, path: str) -> bool:
        return True

    def remove(self, path: str) -> None:
        pass


class StubCSVHandler2(ICSVHandler):
    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "Id": [1, 2, 3],
                "ForumId": [1, 2, 3],
                "Title": ["Title 1", "Title 2", "Title 3"],
                "description": ["description", "description", "description"],
                "Slug": ["slug1", "slug2", "slug3"],
                "url": ["my_url", None, None],
                "date_to_datastore": [None, None, None],
            }
        )

    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        return True

    def exists(self, path: str) -> bool:
        return True

    def remove(self, path: str) -> None:
        pass
