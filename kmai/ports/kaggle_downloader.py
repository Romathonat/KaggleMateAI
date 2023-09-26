from abc import ABC, abstractmethod

import pandas as pd


class KaggleDownloader(ABC):
    @abstractmethod
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        pass
