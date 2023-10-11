from abc import ABC, abstractmethod


class IVectorStoreHelper(ABC):
    @abstractmethod
    def create_vectorstore(self, docs):
        pass

    @abstractmethod
    def read_vectorstore(self, path: str):
        pass

    @abstractmethod
    def write_vectorstore(self, db, path: str):
        pass 

    @abstractmethod
    def similarity_search(self, db, text: str, k: int):
        pass

    @abstractmethod
    def add_doc_to_vectorstore(self, db, docs):
        pass