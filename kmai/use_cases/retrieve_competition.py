from langchain.vectorstores import Chroma
import pandas as pd

from kmai.config import settings
from kmai.ports.icsv_reader import ICSVReader
from kmai.ports.icsv_writer import ICSVWriter
from kmai.ports.ivectorstore import IVectorStore

class VectorStoreWrapper:
    def __init__(self, csv_reader: ICSVReader, csv_writer: ICSVWriter, vectorstore: IVectorStore):
        self.csv_reader = csv_reader
        self.csv_writer = csv_writer
        self.vectorstore = vectorstore

    def get_similar_competitions(self, description: str, k: int) -> pd.DataFrame:
        documents = self.vectorstore.similarity_search(self.vectorstore, description, k)
        data = {
            "Title": [],
            "Description": [],
            "Url": []
        }

        for doc in documents:
            data["Title"].append(doc.metadata["Title"])
            data["Description"].append(doc.metadata["Description"])
            data["Url"].append(doc.metadata["Url"])

        return pd.DataFrame(data=data)

def create_vector_store(csv_reader: ICSVReader, csv_writer: ICSVWriter, vectorstore: IVectorStore) -> VectorStoreWrapper:
    return VectorStoreWrapper(csv_reader, csv_writer, vectorstore)
