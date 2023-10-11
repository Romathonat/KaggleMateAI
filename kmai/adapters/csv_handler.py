import pandas as pd

from kmai.ports.icsv_handler import ICSVHandler


class CSVHandler(ICSVHandler):
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        df.to_csv(path, index=False)
        return True

    def read_csv(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)