import pymongo
from pymongo import MongoClient


class dataBase:
    def prepareDB(self):
        client = MongoClient(
            'mongodb+srv://<renansouzzzz>:<password>@cluster0.i6q18po.mongodb.net/?retryWrites=true&w=majority')
        db = client['results']
        self.collection = db['results']

    def insert(self):
        self.collection.insert_one({"username": f"{self}"})
