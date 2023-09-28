from abc import ABC, abstractmethod

import pandas as pd


class ICSVWriter(ABC):
    @abstractmethod
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        pass
