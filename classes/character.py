from entity import Entity
from item import Item
from equipable_item import Equipable
from player import Player

from affichage import Affichage
from vue import *

class Character(Entity):

    equipment: list[Equipable] = []

    def set_attack(self, value):
        self.attack = value

    def get_attack(self):
        return self.attack

    attack = property(get_attack, set_attack)

    def set_defense(self, value):
        self.defense = value

    def get_defense(self):
        return self.defense

    defense = property(get_defense, set_defense)

    def __init__(self, _name, _hp, _max_hp, _attack, _defense, _equipment):
        self.name = _name
        self.hp = _hp
        self.max_hp = _max_hp
        self.attack = _attack
        self.defense = _defense
        self.equipment = _equipment

    #equip_item(Item)
    #ajouter l'objet Item dans la liste d'equipement
    def equip_item(self, item: Equipable, player: Player):
        if not self.is_slot_available(self, item.item_type):
            removed_item = self.get_equipment(self, item.item_type)
            self.unequip_item(self, item, player)
        self.equipment.append(item)

    #unequip_item(Item)
    #enlève l'objet Item dans la liste d'equipement
    def unequip_item(self, item: Equipable, player: Player):
        self.equipment.remove(item)
        player.inventory.append(item)

    #is_slot_available(slot_name):
    # cherche dans tous les equipable de la liste d'equipement:
    #   est-ce que cet equipable est d'item_type slot_name:
    #       si oui retourne fau
    #   sinon retourne vrai
    def is_slot_available(self, slot_name: str):
        for item in self.equipment:
            if item.item_type == slot_name:
                return False
        return True

    #get_equipment(slot_name):
    # cherche dans tous les equipable de la liste d'equipement:
    #   est-ce que cet equipable est d'item_type slot_name:
    #       retourne cet equipable
    # retourne equipable vide
    def get_equipment(self, slot_name: str):
        for item in self.equipment:
            if item.item_type == slot_name:
                return item
        return None
    
    #project_damage(target: Entity):
    #   si target.defense < attack
    #       retourne attack - target.defense
    #   retourne 0

    def project_damage(self, target: Entity):
        if target.defense < self.attack:
            return (self.attack - target.defense)
        return 0

    def play_turn(self, enemy: Entity, affichage: Affichage, player: Player):
        index = affichage.display_vue(vue_tour_joueur(player.team, self, [enemy]))
        match index:
            case 0:
                pass
            case 1:
                player.check_inventory(affichage)
            case 2:
                pass