from abc import ABC, abstractmethod

import pandas as pd


class ICSVReader(ABC):
    @abstractmethod
    def read_csv(self, path: str) -> bool:
        pass
