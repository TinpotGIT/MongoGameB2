import os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["Database"]

Personnages = database["Personnages"]
Monstres = database["Monstres"]

# S'il y a déja des héros ou des monstres
#   Charger les données des héros et des monstres
# Sinon
#   Ajouter les dictionnaires des héros et des monstres

# Méthode (collection, dict)
# Parcourir une collection
# Si la collection est vide 
#   Ajouter un dictionnaire a la collection