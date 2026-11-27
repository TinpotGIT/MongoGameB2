from player import Player
from vague import Vague
from pymongo import MongoClient

class Game():
    player: Player
    mongoClient: MongoClient
    vague: Vague