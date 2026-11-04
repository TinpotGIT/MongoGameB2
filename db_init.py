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
Scores.insert_many(ScoreList)