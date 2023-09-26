from abc import ABC, abstractmethod

import pandas as pd


class LLMCaller(ABC):
    @abstractmethod
    def get_embedings(self, text_list: list[str]) -> list[list]:
        pass
