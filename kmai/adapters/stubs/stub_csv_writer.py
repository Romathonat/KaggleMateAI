import pandas as pd

from kmai.ports.icsv_writer import ICSVWriter

class StubCSVWriter(ICSVWriter):
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        return True
