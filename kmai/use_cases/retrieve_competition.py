from langchain.vectorstores import Chroma
import pandas as pd
from datetime import datetime

from kmai.config import settings
from kmai.ports.icsv_handler import ICSVHandler 
from kmai.ports.ivectorstore_helper import IVectorStoreHelper

from langchain.schema import Document

class VectorStoreWrapper:
    def __init__(self, csv_handler: ICSVHandler, vectorstore_helper: IVectorStoreHelper):
        self.csv_handler = csv_handler
        self.vectorstore_helper = vectorstore_helper
        self.vectorstore = self.create_vector_store()

    def create_vector_store(self):
        df = self.csv_handler.read_csv(settings.DATA_DIR / settings.COMPETITIONS_WITH_DESCRIPTIONS)
        df_unseen = df[df['date_to_datastore'].isna()]
        doc_list = []
        current_date = datetime.now().date()

        for title, description, url  in zip(df_unseen["Title"], df_unseen["description"], df_unseen["url"]):
            doc_list.append(Document(page_content=description, metadata={"Title": title, "Url": url}))

        df_unseen['date_to_datastore'] = current_date
        df.update(df_unseen)

        self.csv_handler.write_csv(df, settings.DATA_DIR/settings.COMPETITIONS_WITH_DESCRIPTIONS)
        return self.vectorstore_helper.create_vectorstore(doc_list)


    def get_similar_competitions(self, description: str, k: int) -> pd.DataFrame:
        documents = self.vectorstore_helper.similarity_search(self.vectorstore, description, k)
        data = {
            "Title": [],
            "Description": [],
            "Url": []
        }

        for doc in documents:
            data["Description"].append(doc.page_content)
            data["Title"].append(doc.metadata["Title"])
            data["Url"].append(doc.metadata["Url"])

        return pd.DataFrame(data=data)

    

def create_vector_store(csv_handler: ICSVHandler, vectorstore: IVectorStoreHelper) -> VectorStoreWrapper:
    return VectorStoreWrapper(csv_handler, vectorstore)
