from enemy import Enemy
from random import choice

from player import Player
from affichage import Affichage
from vue import * 

class Vague():
    vague_actuel : int
    monsters: list[Enemy]

    def __init__(self, _vague, _monsters):
        self.vague_actuel = _vague
        self.monsters = _monsters

    #def pick_enemies(vague):
    #   prends un ennemi au hasard dans 
    #   la liste monsters de vague

    def pick_enemies(self):
        return choice(self.monsters)

    #def get_difficulty():
    #   renvoie le lap, donc 1 + le modulo de vague_actuel sur 30

    def get_difficulty(self, difficulty_list):
        return difficulty_list[1 + (self.vague_actuel % 30)]

    #def play_vague(player: Player):
    #   monster = pick_enemies(self)
    #   tant que le monstre est en vie et equipe en vie:
    #       pour chaque personnage en vie dans l'equipe:
    #           index = vue du tour du personnage
    #           si index == 0:
    #           lancer tour du personnage
    #       si index == 1:
    #           lancer le menu d'inventaire
    #       si index == 2:
    #           passer le tour

    def play_vague(self, player: Player, affichage: Affichage):
        monster : Enemy = self.pick_enemies(self)
        while monster.is_alive() and player.is_team_alive:
            for char in player.team:
                if char.is_alive():
                    char.play_turn(monster, affichage, player)

def apply_difficulty(difficulty_list: list):
    pass