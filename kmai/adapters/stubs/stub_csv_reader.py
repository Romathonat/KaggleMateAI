import pandas as pd

from kmai.ports.icsv_reader import ICSVReader


class StubCSVReader(ICSVReader):
    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "desc_embedding": [[1.3, 2.5, 0.2], None, None],
                "description": ["description", None, None],
                "Slug": ["slug1", "slug2", "slug3"],
            }
        )
