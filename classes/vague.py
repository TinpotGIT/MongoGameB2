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

    #def pick_enemies(vague, vague_list, enemy_list):
    #   parcourir les dict de vague_list:
    #       si la vague_actuel est entre le start_number et end_number de la dict:
    #           recuperer tout les monstres entre l'index de début et de fin des monstres de la vague

    def pick_enemies(self, vague_list, enemy_list):
        self.monsters = []
        vague = self.get_vague(self, vague_list)

    def get_vague(self, vague_list):
        for vague in vague_list:
            vague = dict(vague)
            if vague["start_number"] <= self.vague_actuel <= vague["end_number"]:
                return vague
    
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

    def play_vague(self, player: Player, affichage: Affichage, vague_list, enemy_list):
        monsters : Enemy = self.pick_enemies(self, vague_list, enemy_list)
        while are_monsters_alive(monsters) and player.is_team_alive:
            for char in player.team:
                if char.is_alive():
                    char.play_turn(monsters, affichage, player)

def apply_difficulty(difficulty_list: list):
    pass

def are_monsters_alive(monsters: list[Enemy]):
    for monster in monsters:
        if monster.is_alive():
            return True
    return False