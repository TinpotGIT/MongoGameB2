from item import Item
from entity import Entity

class Consumable(Item):

    def __init__(self, _name, _description, _drop_rate, _rarity, _item_type, _stats):
        self.name = _name
        self.description = _description
        self.drop_rate = _drop_rate
        self.rarity = _rarity
        self.item_type = _item_type
        self.stats = _stats

    #use(target: Entity):
    #   pour chaque stats dans le dict de stats
    #       ajoute la stat à celle de l'entité

    def use(self, target: Entity):
        target.hp += self.stats["hp"]
        target.max_hp += self.stats["hp"]
        target.attack += self.stats["attack"]
        target.defense += self.stats["defense"]