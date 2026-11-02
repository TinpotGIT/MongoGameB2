import os
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Database"]
characters = db["Characters"]

testdict = {"a": "truc", "b": "autre_truc"}

textinsert = characters.insert_one(testdict)