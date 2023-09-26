import pandas as pd

from kmai.ports.csv_writer import CSVWriter


class StubCSVWriter(CSVWriter):
    def write_csv(self, df: pd.DataFrame) -> bool:
        return True
