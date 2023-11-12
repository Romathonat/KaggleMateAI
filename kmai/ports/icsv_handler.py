from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class ICSVHandler(ABC):
    @abstractmethod
    def write_csv(self, df: pd.DataFrame, path: Path) -> bool:
        pass

    @abstractmethod
    def read_csv(self, path: Path) -> pd.DataFrame:
        pass

    @abstractmethod
    def exists(self, path: Path) -> bool:
        pass

    @abstractmethod
    def remove(self, path: Path) -> bool:
        pass
