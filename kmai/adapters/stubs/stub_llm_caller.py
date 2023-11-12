import numpy as np

from kmai.ports.illm_caller import ILLMCaller


class StubLLMCaller(ILLMCaller):
    def get_embeddings(self, text_list: list[str]) -> list[list]:
        return np.random.normal(0, 1, (len(text_list), 512)).tolist()
