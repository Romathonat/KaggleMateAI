import pandas as pd

from kmai.ports.icsv_writer import ICSVWriter


class CSVWriter(ICSVWriter):
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        df.to_csv(path, index=False)
        return True
