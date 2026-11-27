from enemy import Enemy
from random import choice

class Vague():
    vague_actuel : int
    monsters: list[Enemy]

    def __init__(self, _vague, _monsters):
        self.vague_actuel = _vague
        self.monsters = _monsters

    #def pick_enemies(vague):
    #   prends une liste d'enemie au hasard dans 
    #   la liste monsters de vague

    def pick_enemies(self):
        return choice(self.monsters)

    #def get_difficulty():
    #   renvoie le lap, donc 1 + le modulo de vague_actuel sur 30

    def get_difficulty(self, difficulty_list):
        return difficulty_list[1 + (self.vague_actuel % 30)]

    #def play_vague(player: Player):
    #   monster = pick_enemies(self)
    #   tant que le monstre est en vie:
    #       index = affiche la vue du tour du joueur
    #       si index == 0:
    #           player check inventory