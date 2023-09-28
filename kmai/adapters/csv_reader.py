import pandas as pd

from kmai.config import settings
from kmai.ports.icsv_reader import ICSVReader


class CSVReader(ICSVReader):
    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)
