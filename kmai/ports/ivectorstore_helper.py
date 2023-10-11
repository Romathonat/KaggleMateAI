from abc import ABC, abstractmethod



class IVectorStoreHelper(ABC):
    @abstractmethod
    def read_vectorstore(self, path: str):
        pass

    @abstractmethod
    def write_vectorstore(self, db, path: str):
        pass 

    @abstractmethod
    def similarity_search(self, text: str, k: int):
        pass