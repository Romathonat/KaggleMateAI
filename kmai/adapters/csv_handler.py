import pandas as pd
import os

from kmai.ports.icsv_handler import ICSVHandler


class CSVHandler(ICSVHandler):
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        df.to_csv(path, index=False)
        return True

    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)

    def exists(self, path: str) -> bool:
        return os.path.exists(path)
    
    def remove(self, path: str) -> None:
        os.remove(path)