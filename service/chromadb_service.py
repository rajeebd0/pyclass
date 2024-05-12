import uuid
import chromadb
from core.config import Config
from chromadb.utils import embedding_functions


class ChromaDB:
    def __init__(self):
        db_path = Config.app_path + "\\data\\db"
        client = chromadb.PersistentClient(path=db_path)
        self.collection = client.get_or_create_collection("processmate")

    @staticmethod
    def embeddings(*args):
        default_ef = embedding_functions.DefaultEmbeddingFunction()
        val = default_ef([*args])
        return val

    def insert_or_update(self, bpmn, data):
        self.collection.upsert(
            documents=data,
            ids=bpmn
        )

    def get(self, bpmn=''):
        result = self.collection.get(ids=[bpmn])
        return result
