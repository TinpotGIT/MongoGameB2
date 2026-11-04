import os
import pymongo

from models import *

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["Database"]

Characters = database["Characters"]
Enemies = database["Enemies"]
Scores = database["Scores"]

Characters.drop()
Enemies.drop()

Characters.insert_many(CharacterList)
Enemies.insert_many(CharacterList)

def get_list(collection):
    list = []
    for doc in collection.find():
        list.append(doc)
    return list