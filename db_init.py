import os
import pymongo

from models import *

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["Database"]

Characters = database["Characters"]
Monsters = database["Monsters"]
Scores = database["Scores"]

Characters.insert_many(Characters)