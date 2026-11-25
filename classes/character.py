from entity import Entity

class Character(Entity):

    def __init__(self, _name, _hp, _max_hp, _attack, _defense):
        self.name = _name
        self.hp = _hp
        self.max_hp = _max_hp
        self.attack = _attack
        self.defense = _defense

    def play_turn():
        pass