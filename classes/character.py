from entity import Entity
from item import Item
from equipable_item import Equipable

class Character(Entity):

    equipment: list[Item]

    @attack.setter
    def attack(self, value):
        self.attack = value   

    @defense.setter
    def defense(self, value):
        self.defense = value

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

    def play_turn(self, enemy):
        self.attack_entity(enemy)