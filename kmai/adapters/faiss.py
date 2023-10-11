from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

from kmai.ports.ivectorstore_helper import IVectorStoreHelper

class FAISS(IVectorStoreHelper):
    def create_vectorstore(self, docs):
        embeddings = OpenAIEmbeddings()
        return FAISS.from_documents(docs, embeddings)

    def read_vectorstore(self, path: str):
        embeddings = OpenAIEmbeddings()
        db = FAISS.load_local(path, embeddings)
        return db

    def write_vectorstore(self, db: FAISS, path: str):
        db.save_local(path)
        return True 

    def similarity_search(self, db: FAISS, text: str, k: int):
        return db.similarity_search(text, k)
    
    def add_doc_to_vectorstore(self, db, docs):
        pass