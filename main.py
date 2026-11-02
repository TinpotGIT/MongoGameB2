# Affiche le titre du jeu
# choix_menu()

# choix_menu():
#   Affiche les options du menu principal avec un chiffre correspondant a chaque
#   Boucle tant que l'on a pas choisi une des options
#       demande un input au joueur 
#       Si l'input est valide (chiffre correct):
#           lancer la méthode lié a l'option:
#               Pour 1 lancer new_game()
#               Pour 2 lancer leaderboard()
#               Pour 3 ne rien faire, ce qui quitte la boucle
#       Sinon afficher que l'input est invalide

# new_game():
#   équipe = créer_equipe()
#   score = lancer_combat(equipe)
#   Afficher au joueur qu'il doit écrire son pseudo
#   Boucle Demander un input au joueur
#       tant que l'input est vide, redemander
#   ajouter_score(score, pseudo)

# leaderboard():
#   créer une liste qui récupère les groupes scores/pseudos dans la DB
#   parcours la liste:
#       Affiche position dans le leaderboard -> Pseudo : Score

# ajouter_score(score):
#   créer une liste qui récupère les groupes scores/pseudos dans la DB
#   parcours la liste:
#       si le score du joueur est plus grand que le score du joueur dans la liste au point i:
#           insérer le joueur et son score a sa place dans la collection de la DB



# créer_equipe():
#   créer une liste d'équipe vide
#   créer une liste qui recupere tout les personnages dans la DB 
#   afficher la liste des personnages avec un chiffre correspondant a chaque personnage
#   Boucle tant qu'on a pas choisi un certain nombre de personnages
#       demander un input au joueur
#       Si l'input se trouve dans la liste de personnage, et qu'il n'a pas été choisi avant :
#           ajoute le personnage a l'equipe que l'on va utiliser
#       Sinon
#           affiche au joueur que l'input est invalide
#   retourner l'équipe

# lancer_combat(equipe):
#   crée une variable de tours
#   crée une variable de score
#   boucle tant que si_equipe_vivante(equipe) est Vrai
#       affiche le tour actuel et le score actuel au joueur
#       monstre = créer_monstre()
#       affiche le nom du monstre a battre
#       boucle tant que le monstre est vivant
#           affiche les statistiques des personnages et du monstre
#           les personnages attaquent le monstre
#           affiche les dégats infligés par le personnage et les hp du monstre
#           le monstre attaque les personnages
#           affiche les dégats infligés par le monstre et les hp des personnages
#       le monstre est mort, on ajoute 1 au tour et le score du monstre au score total
#   les personnages sont tous mort, affiche le nombre de tour final et le score final
#   retourner le score final

# créer_monstre():
# créer une liste qui recupere la liste de monstres dans la DB
# renvoyer un monstre aléatoire dans la liste

# si_equipe_vivante(equipe):
#   pour chaque personnage dans l'equipe:
#       si la vie du personnage > 0:
#           retourne True
#   retourn False