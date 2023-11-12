import os
from pathlib import Path

import pandas as pd

from kmai.ports.icsv_handler import ICSVHandler


class CSVHandler(ICSVHandler):
    def write_csv(self, df: pd.DataFrame, path: Path) -> bool:
        df.to_csv(path, index=False)
        return True

    def read_csv(self, path: Path) -> pd.DataFrame:
        return pd.read_csv(path)

    def exists(self, path: Path) -> bool:
        return os.path.exists(path)

    def remove(self, path: Path) -> None:
        os.remove(path)
