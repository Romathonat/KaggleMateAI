import random

import numpy as np

from kmai.ports.llm_caller import LLMCaller


class StubLLMCaller(LLMCaller):
    def get_embeding(self, text_list: list[str]) -> list[list]:
        return np.random.normal(0, 1, (len(text_list), 512)).tolist()
