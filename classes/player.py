from character import Character
from item import Item
from affichage import Affichage
import vue 

from consumable_item import Consumable
from equipable_item import Equipable

class Player():

    name: str
    score: int
    team: list[Character]
    inventory: list[Item]

    def __init__(self, _name, _score, _team, _inventory):
        self.name = _name
        self.score = _score
        self.team = _team
        self.inventory = _inventory

    def __str__(self):
        print(f"------------- {self.name} -------------")
        print(f"Score : {self.score}")
        print(f"Team : {self.team}")
        print(f"Inventory : {self.inventory}")
        
    def create_team(self, character_list: list[Character], affichage: Affichage):
        for i in range(3):
            chosen_character = self.pick_character(self, character_list, affichage)
            self.team.append(chosen_character)
            character_list.remove(chosen_character)

    def pick_character(self, character_list, affichage: Affichage):
        index = affichage.display_vue(vue.VueSelectionEquipe(self.team, character_list))
        return character_list[index]

    # is_team_alive():
    #   parcours tout les joueurs de la team:
    #       si le joueur à plus de 0 pv:
    #           retourne vrai
    #   retourne faux
    def is_team_alive(self):
        for char in self.team:
            if char.hp > 0:
                return True
        return False

    # check_inventory(affichage, inventory):
    #   affiche la vue de la liste d'objets inventaire
    #   recupere l'index choisi
    #   on utilise l'objet
    def check_inventory(self, affichage: Affichage):
        index = affichage.display_vue(vue.vue_inventaire(self.inventory, self.team))
        item = self.inventory[index]
        self.use_item(item, affichage)
            
    # def use_item(item: Item):
    #   choisi un objet dans l'inventaire
    #   choisi une cible dans l'equipe
    #   si l'objet est un consumable:
    #       le personnage consume l'objet
    #   sinon si l'objet est un equipement:
    #       le personnage equipe l'objet
    def use_item(self, item: Item, affichage: Affichage):
        character : Character = affichage.display_vue(vue.vue_choix_cible_equipe(self.inventory, self.team))
        if item is Consumable:
            item.use(Character)
        elif item is Equipable:
            character.equip_item(item)