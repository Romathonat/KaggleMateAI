from abc import ABC, abstractmethod
from pathlib import Path


class IVectorStoreHelper(ABC):
    @abstractmethod
    def create_vectorstore(self, docs):
        pass

    @abstractmethod
    def read_vectorstore(self, path: Path):
        pass

    @abstractmethod
    def write_vectorstore(self, db, path: Path):
        pass

    @abstractmethod
    def similarity_search(self, db, text: str, k: int) -> list:
        pass

    @abstractmethod
    def add_doc_to_vectorstore(self, db, docs):
        pass
