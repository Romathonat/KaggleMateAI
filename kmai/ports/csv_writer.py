from abc import ABC, abstractmethod

import pandas as pd


class CSVWriter(ABC):
    @abstractmethod
    def write_csv(self, df: pd.DataFrame) -> bool:
        pass
