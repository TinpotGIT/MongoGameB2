from db_init import *
import random

# main:
# choix = choix_menu():
# lance_fonction(choix)

def main():
    choice = menu_choice()
    choose_option(choice)

# choix_menu():
#   Boucle infini:
#       afficher_menu()
#       si_choix_valide(1, 3)
#           return choix

def menu_choice():
    while True:
        print_menu()
        choice = input("Choose an option : ")
        if is_valid_number(choice, 1, 3):
            return choice

# afficher_menu():
#   affiche 1. Jouer
#   affiche 2. Classement
#   affiche 3. Quitter

def print_menu():
    print("1. Jouer")
    print("2. Classement")
    print("3. Quitter")

# si_nombre_valide(nombre, min, max):
#   si nombre est un nombre et int(nombre) se trouve entre min et max:
#       retourne Vrai
#   retourne Faux

def is_valid_number(number, min, max):
    if number.isdigit() and (number > min and number < max):
        return True
    return False

# lancer_fonction(choix):
#   si choix inférieur à 3:
#       score_list = recuperer_liste(Score)
#       si choix 1 -> charger_partie(score_list)
#       si choix 2 -> classement(score_list)

def choose_option(choice):
    if choice < 3:
        score_list = get_list(Scores)
        if choice == 1:
            load_game(score_list)
        else:
            leaderboard(score_list)

# recuperer_liste(collection)
#   crée une liste vide
#   pour tout document dans la collection.find():
#       ajouter le document à la liste
#   retourner la liste

def get_list(collection):
    list = []
    for doc in collection.find():
        list.append(doc)
    return list

# charger_partie(score_list):
#   pseudo = demander_pseudo()
#   equipe = creer_equipe()
#   enemies = recuperer_liste(Monstres)
#   score = lancer_partie(equipe, enemies)
#   ajouter_score(score, pseudo, score_list)
#   afficher_ecran_fin(pseudo, score, equipe)

def load_game(score_list):
    username = ask_username()
    team = create_team()
    enemies = get_list(Enemies)
    score = start_game(team, enemies)
    save_score(score, username, score_list)
    show_end_screen(username, score, team)

# demander_pseudo():
#   afficher "Ecris ton pseudo : "
#   pseudo = demander input
#   retourner pseudo

def ask_username():
    username = input("What is your username? : ")
    return username

# creer_equipe():
#   liste_personnages = recuperer_liste(Personnages)
#   afficher_personnages(liste_personnages)
#   equipe = ajouter_personnages(liste_personnages)
#   retourner equipe

def create_team():
    character_list = get_list(Characters)
    print_characters(character_list)
    team = add_characters(character_list)
    return team

# afficher_personnages(liste):
#   pour tout personnage dans la liste:
#       afficher_personnage(personnage)

def print_characters(list):
    for character in list:
        print_character(character)

# afficher_personnage(personnage):
#   affiche le nom du personnage
#   affiche les points de vie du personnage
#   affiche la force du personnage
#   affiche la defense du personnage

def print_character(character):
    print(character)

# ajouter_personnages(liste_personnages):
#   equipe = []
#   Boucle tant que si_equipe_incomplete(equipe, 3):
#       choix = demande un input pour le menu
#       si_nombre_valide(choix, 1, len(liste_personnages)):
#           ajouter liste_personnages[choix - 1] à equipe

def add_characters(character_list):
    team = []
    while is_team_incomplete(team, 3):
        choice = input("Enter the character ID of the one you want : ")
        if is_valid_number(choice, 1, len(character_list)):
            team.append(character_list[choice - 1])

# si_equipe_incomplete(equipe, max):
#   si len(equipe) != max:
#       retourne Vrai
#   retourne Faux

def is_team_incomplete(team, max):
    if len(team) != max:
        return True
    return False

# lancer_partie(equipe, enemies):
#   score = 0
#   boucle tant que si_equipe_vivante(equipe):
#       lancer_vague(equipe, enemies, score)
#       si_equipe_vivante(equipe):
#           score += 1
#       afficher_info_vague(score)
#   retourne score

def start_game(team, enemies):
    score = 0
    while is_team_alive(team):
        start_wave(team, enemies, score)
        if is_team_alive(team):
            score += 1
        print_wave_info()
    return score

# si_equipe_vivante(equipe):
#   pour tout membre dans equipe:
#       si_vivant(member):
#           retourner Vrai

def is_team_alive(team):
    for member in team:
        if is_alive(member):
            return True

# lancer_vague(equipe, enemies, score):
#   enemi = recuperer_enemi(enemies)
#   lancer_combat(equipe, enemi)

def start_wave(team, enemies, score):
    enemy = get_enemy(enemies)
    start_combat(team, enemy)

# si_vivant(personnage):
#   si hp de personnage > 0:
#       retourner Vrai
#   retourner Faux

def is_alive(entity : dict):
    if entity[1] > 0:
        return True
    return False

# afficher_info_vague(score):
#   affiche f"Tour numéro : {score}"

def print_wave_info(score):
    print(f"Tour numéro : {score}")

# recuperer_enemi(enemi):
#   retourner un élement aléatoire dans la liste des enemies 

def get_enemy(enemies):
    return random.choice(enemies)

# lancer_combat(equipe, enemi):
#   boucle tant que si_vivant(enemi) et si_equipe_vivante(equipe):
#       equipe_attaque_monstre(equipe, enemi)
#       si_vivant(enemi):
#           monstre_attaque_equipe(enemi, equipe)

def start_combat(team, enemy):
    while is_alive(enemy) and is_team_alive(team):
        team_attack(team, enemy)
        if is_alive(enemy):
            monster_attack(enemy, team)

# equipe_attaque_monstre(equipe, enemi):
#   pour chaque personnage dans equipe:
#       attaque(personnage, enemi)

def team_attack(team, enemy):
    for member in team:
        attack(member, enemy)

# monstre_attaque_equipe(enemi, equipe):
#   personnage = personnage_aléatoire(equipe)
#   attaque(enemi, personnage)

def monster_attack(enemy, team):
    member = random_member(team)
    attack(enemy, member)

# personnage_aléatoire(equipe):
#   equipe_vivante = récuperer_personnages_vivants(equipe, [])
#   retourner personnage aléatoire dans equipe_vivante

def random_member(team):
    alive_members = get_alive_members(team, [])
    return random.choice(alive_members)

# récuperer_personnages_vivants(equipe, equipe_vivante):
#   pour chaque personnage dans equipe:
#       si hp personnage > 0:
#           ajouter personnage dans equipe_vivante

def get_alive_members(team, alive_members):
    for member in team:
        if member[2] > 0:
            alive_members.append(member)

# attaque(attaquant, cible):
#   hp de la cible - (attaque de l'attaquant - defense de la cible)

def attack(attacker, target):
    damage = (attacker[4] - target[3])
    if damage <= 0:
        damage = 0
    target[2] -= damage

# classement(score_list):
#   pour i jusqu'à len(score_list):
#       Afficher f"{placement} -> {nom} : {score} \n" de score_list[i]

def leaderboard(score_list):
    for i in range(len(score_list)):
        print(f"{i} -> {score_list[i][1] : {score_list[i][2]}}")

# ajouter_score(score, pseudo, score_list):
#   update_score_list(score_list, score)
#   update_collection(Scores, score_list)

def save_score(score, username, score_list):
    update_score_list(score_list, score)
    update_collection(Scores, score_list)

# update_score_list(score_list, score):
#   de i jusqu'à len(score_list):
#       si le score au score_list[i] est < score:
#           insère score à score_list[i]

def update_score_list(score_list, score):
    for i in range(len(score_list)):
        if score_list[i][2] < score:
            score_list.insert(i, score)
            
# update_collection(collection, list):
#   collection.update_many({}, list)

def update_collection(collection, list):
    collection.update_many({}, list)

# afficher_ecran_fin(score, pseudo):
#   affiche un message qui donne le pseudo du joueur, son equipe et le score final qu'elle a eu. 

def show_end_screen(score, username):
    print("The end, will be finished after.")