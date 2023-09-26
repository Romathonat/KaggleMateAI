from abc import ABC, abstractmethod

import pandas as pd


class LLMCaller(ABC):
    @abstractmethod
    def get_embeding(self, text_list: list[str]) -> list[list]:
        pass
