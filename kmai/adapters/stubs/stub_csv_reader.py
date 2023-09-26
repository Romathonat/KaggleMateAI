import pandas as pd

from kmai.ports.icsv_reader import ICSVReader 

class StubCSVReader(ICSVReader):
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        return True
