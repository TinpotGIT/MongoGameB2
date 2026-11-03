# main:
#   Boucle infini:
#       afficher_menu()
#       choix = demande un input pour le menu
#       si_nombre_valide(choix, 1, 3):
#           lance_fonction(choix)

# afficher_menu():
#   affiche 1. Jouer
#   affiche 2. Classement
#   affiche 3. Quitter

# si_nombre_valide(choix, min, max):
#   si choix n'est pas un nombre:
#       retourne Faux
#   si int(choix) se trouve entre min et max:
#       retourne Vrai
#   retourne Faux

# lancer_fonction(choix):
#   pour choix:
#       si 1 -> charger_partie()
#       si 2 -> classement()
#       si 3 -> quitte la boucle

# charger_partie():
#   equipe = creer_equipe()
#   monstres = recuperer_liste(Monstres)
#   score = lancer_partie(equipe, monstres)
#   pseudo = demander_pseudo()
#   ajouter_score(score, pseudo)

# creer_equipe():
#   liste_personnages = recuperer_liste(Personnages)
#   afficher_personnages(liste_personnages)
#   equipe = ajouter_personnages(liste_personnages, [], 3)
#   retourner equipe

# ajouter_personnages(liste_personnages, equipe, max):
#   Boucle tant que len(equipe) != max:
#       choix = demande un input 
#       si_nombre_valide(choix, 1, len(liste_personnages)):
#           ajouter liste_personnages[choix] à equipe

# recuperer_liste(collection)
#   resultat = []
#   pour tout document dans la collection.find():
#       ajouter le document à la liste
#   retourne résultat

# afficher_personnages(liste):
#   pour tout personnage dans la liste:
#       afficher_personnage(personnage)

# afficher_personnage(personnage):
#   affiche le nom du personnage
#   affiche les points de vie du personnage
#   affiche la force du personnage
#   affiche la defense du personnage

# demander_pseudo():
#   afficher "Ecris ton pseudo : "
#   pseudo = demander input
#   retourner pseudo

# lancer_partie(equipe, monstres):
#   créer variables tours = 0 et score = 0
#   boucle tant que si_equipe_vivante():
#       score = lancer_tour(equipe, monstres, tours, score)

# lancer_tour(equipe, monstres, tours, score):
#   afficher_info_tour(tours, score)
#   monstre = recuperer_monstre(monstres)
#   lancer_combat(equipe, monstre)
#   si_equipe_vivante:
#       score += 1
#   tours += 1
#   retourner score

# si_equipe_vivante():
#   pour tout membre dans équipe:
#       si hp de member > 0:
#           retourne Vrai
#   retourne Faux

# afficher_info_tour(tours, score):
#   affiche f"Tour numéro : {tours}"
#   affiche f"Score actuel de : {score}"

# récuperer_monstre(monstres):
#   retourner un élement aléatoire dans la liste monstres

# lancer_combat(equipe, monstre):
#   boucle tant que si_monstre_vivant(monstre) et si_equipe_vivante(equipe):
#       equipe_attaque_monstre()
#       si_monstre_vivant(monstre):
#           monstre_attaque_equipe()