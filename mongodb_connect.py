from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self,url='mongodb+srv://yunusemrek558:yunusemre302@cluster0.gj2kr.mongodb.net/'):
        self.client = MongoClient(url)

    
    def database_getir(self, db_name):
        return self.client[db_name]