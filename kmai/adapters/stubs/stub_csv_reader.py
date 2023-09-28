import pandas as pd

from kmai.config import settings
from kmai.ports.icsv_reader import ICSVReader


class StubCSVReader(ICSVReader):
    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "Id": [1, 2, 3],
                "ForumId": [1, 2, 3],
                "Title": ["Title 1", "Title 2", "Title 3"],
                "desc_embedding": [[1.3, 2.5, 0.2], None, None],
                "description": ["description", None, None],
                "Slug": ["slug1", "slug2", "slug3"],
                "url": ["my_url", None, None],
            }
        )
