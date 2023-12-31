from abc import ABC, abstractmethod

import pandas as pd


class ICompetitionScrapper(ABC):
    @abstractmethod
    def get_competition_text(self, url: str) -> str:
        pass
