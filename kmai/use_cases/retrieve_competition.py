from langchain.vectorstores import Chroma

from kmai.config import settings
from kmai.ports.icsv_reader import ICSVReader
from kmai.ports.illm_caller import ILLMCaller


class VectorStore:
    def __init__(self, csv_reader: ICSVReader, llm_caller: ILLMCaller):
        self.csv_reader = csv_reader
        self.llm_caller = llm_caller
        self.db = self.load_db()

    def load_db(self):
        embeddings_dict = self.csv_reader.read_csv(f"{settings.DATA_DIR} / {settings.COMPETITIONS_WITH_EMBEDDINGS}")
        db = Chroma. ("vector_store.chroma")
        db.insert_many(embeddings_dict)
        return db

    def get_similar_competitions(self, description, n):
        vector = self.llm_caller.get_embeddings(description)
        similar_items = self.db.query(vector, topn=n)

        result = {
            "Title": [item["Title"] for item in similar_items],
            "Description": [item["Description"] for item in similar_items],
            "Url": [item["Url"] for item in similar_items],
        }
        return result


def create_vector_store(csv_reader, llm_caller):
    return VectorStore(csv_reader, llm_caller)
