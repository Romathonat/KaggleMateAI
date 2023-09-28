from abc import ABC, abstractmethod

import pandas as pd


class IKaggleDownloader(ABC):
    @abstractmethod
    def download_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        pass
