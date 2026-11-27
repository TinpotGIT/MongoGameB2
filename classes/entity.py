class Entity:
    name: str
    hp: int
    max_hp: int
    attack: int
    defense: int

    def __init__(self, _name, _hp, _max_hp, _attack, _defense):
        self.name = _name
        self.hp = _hp
        self.max_hp = _max_hp
        self.attack = _attack
        self.defense = _defense

    def __str__(self):
        print(f"------------- {self.name} -------------")
        print(f"Hp : {self.hp}/{self.max_hp}")
        print(f"Attack : {self.attack}")
        print(f"Defense : {self.defense}")
    
    #is alive(self):
    #   si self.pv <= 0:
    #       retourne faux
    #   retourne vrai

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True

    #take_damage(self, amount):
    #si la vie apres degat est inferieur a 0:
    #   met la vie a 0
    #sinon
    #   retire amount a self.hp

    def take_damage(self, amount: int):
        if self.hp - amount < 0:
            self.hp = 0
        else:
            self.hp -= amount

    #heal(self, amount):
    #si self.hp + amount <= maxHp:
    #   ajoute amount a self.hp
    #sinon
    #   self.hp = maxHp

    def heal(self, amount):
        if self.hp + amount < self.max_hp:
            self.hp += amount
        else:
            self.hp = self.max_hp

    #attack(self, entity)
    #appel take_damage de l'entity pour les degats

    def attack_entity(self, enemy: Entity):
        enemy.take_damage(self.attack)

    def play_turn():
        pass