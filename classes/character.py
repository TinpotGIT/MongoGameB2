from entity import Entity
from item import Item
from equipable_item import Equipable

class Character(Entity):

    equipment: list[Item]

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
    def equip_item(self, equipable: Equipable):
        if self.is_slot_available(self, equipable.item_type):
            self.equipment.append(equipable)

    #unequip_item(Item)
    #enlève l'objet Item dans la liste d'equipement
    def unequip_item(self, item: Item):
        self.equipment.remove(item)

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

    def play_turn(self, enemy: Entity):
        if self.is_alive():
            self.attack_entity(enemy)