from abc import ABC, abstractmethod

import pandas as pd


class ICSVHandler(ABC):
    @abstractmethod
    def write_csv(self, df: pd.DataFrame, path: str) -> bool:
        pass
    
    @abstractmethod
    def read_csv(self, path: str) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def exists(self, path: str) -> bool:
        pass

    @abstractmethod
    def remove(self, path: str) -> bool:
        pass
