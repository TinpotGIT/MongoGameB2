# Afficher le titre du jeu
# Demander au joueur son pseudo
# Choix des personnages
# Lancement de la boucle de jeu

# -------------------

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
#               Pour 3 lancer quit()
#       Sinon afficher que l'input est invalide

# new_game():
#   Afficher au joueur qu'on doit récuperer son pseudo
#   Boucle Demander un input au joueur
#       tant que l'input est vide, redemander
#   équipe = créer_equipe()
#   lancer_combat()

# créer_equipe():
#   créer une liste d'équipe
#   Recupere tout les personnages dans la DB
#   affiche la liste des personnages avec un chiffre correspondant a chaque
#   Boucle tant qu'on a pas choisi un certain nombre de personnages
#       demande un input au joueur
#       Si l'input se trouve dans la liste de personnage, et qu'il n'a pas été choisi avant :
#           ajoute le personnage a l'equipe que l'on va utiliser
#       Sinon
#           affiche au joueur que l'input est invalide
#   retourner l'équipe

# lancer_combat():
# crée une variable de tours
# crée une variable de score
# recupere la liste de monstres dans la DB
# boucle tant que tout les personnages de l'equipe sont vivants
#   affiche le tour actuel et le score actuel au joueur
#   crée un nouveau monstre aléatoirement
#   boucle tant que le monstre est vivant
#       affiche le nom du nouveau monstre a battre
#       affiche les statistiques des personnages et du monstre
#       les personnages attaquent le monstre
#       affiche les dégats infligés par le personnage et les hp du monstre
#       le monstre attaque les personnages
#       affiche les dégats infligés par le monstre et les hp des personnages
#   le monstre est mort, on ajoute 1 au tour et le score du monstre au score total
# les personnages sont tous mort, affiche le nombre de tour final et le score final
