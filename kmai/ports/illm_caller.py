from abc import ABC, abstractmethod

import pandas as pd


class ILLMCaller(ABC):
    @abstractmethod
    def get_embeddings(self, text_list: list[str]) -> list[list]:
        pass
