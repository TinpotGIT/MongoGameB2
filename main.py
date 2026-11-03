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
#   equipe = creer_equipe([])
#   score = jeu(equipe)
#   pseudo = demander_pseudo()
#   ajouter_score(score, pseudo)

# creer_equipe(equipe, max):
#   liste_personnages = recuperer_liste(Personnages)
#   afficher_personnages(liste_personnages)
#   Boucle tant que len(equipe) != max:
#       choix = demande un input 
#       si_nombre_valide(choix, 1, len(liste_personnages)):
#           ajouter liste_personnages[choix] à equipe
#   retourner equipe

# recuperer_liste(collection):
#   resultat = liste vide
#   pour tout document dans la collection:
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
#   Boucle infini:
#       pseudo = demander input
#       si_pseudo_valide(pseudo):
#           retourne pseudo

# jeu(equipe):
#   créer variables tours = 1 et score = 0
#   boucle tant que si_equipe_vivante():
#       afficher_info_tour(tours, score)
#       monstre = créer_monstre()
#       lancer_tour(equipe, monstre)
#       si_equipe_vivante():
#           score = recompenses_monstre(monstre)
#   retourner score

# lancer_tour(equipe, monstre):
#   boucle tant que si_monstre_vivant(monstre) et si_equipe_vivante(equipe):
#       equipe_attaque_monstre()
#           si_monstre_vivant(monstre):
#               monstre_attaque_equipe()

# si_pseudo_valide(pseudo):
#   si pseudo n'est pas un string vide:
#       retourne Vrai
#   sinon:
#       affiche que l'utilisateur doit écrire un pseudo
#       retourne Faux