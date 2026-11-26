from item import Item
from entity import Entity

from random import random

class Enemy(Entity):

    dropables: list[Item]

    def __init__(self, _name, _hp, _max_hp, _attack, _defense, _dropables):
        self.name = _name
        self.hp = _hp
        self.max_hp = _max_hp
        self.attack = _attack
        self.defense = _defense
        self.dropables = _dropables

    #drop_loot():
    #   crée une liste vide d'item
    #   pour chaque objet dans la liste de drops:
    #       si roll_chance(rarity):
    #           ajoute objet à la liste
    #   retourne liste
    def drop_loot(self):
        loot_list: list[Item] = []
        for drop in self.dropables:
            if random <= drop.drop_rate:
                loot_list.append(drop)
        return loot_list