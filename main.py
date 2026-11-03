# main:
#   Boucle infini:
#       afficher_menu()
#       choix = demande un input pour le menu
#       si_nombre_valide(choix, 1, 3):
#           lance_fonction(choix)

# afficher_menu():
#   print le menu complet

# si_nombre_valide(choix, min, max):
#   si choix n'est pas un nombre:
#       retourne Faux
#   si int(choix) se trouve entre min et max:
#       retourne Vrai
#   retourne Faux

# lance_fonction(choix):
#   pour choix:
#       si 1 -> charger_partie()
#       si 2 -> classement()
#       si 3 -> quitte la boucle

# charger_partie():
#   equipe = creer_equipe([])
#   score = jeu(equipe)
#   pseudo = demander_pseudo()
#   ajouter_score(score, pseudo)

# creer_equipe(equipe):
#   liste_personnages = recuperer_liste(Personnages)
#   afficher_personnages(liste_personnages)
#   Boucle infini:
#       choix = demande un input 
#       si_personnage_valide(choix, equipe):
#           ajouter_personnage_equipe(choix, equipe)
#   retourner equipe

# recuperer_liste(collection):
#   resultat = liste vide
#   pour tout les documents dans la collection:
#       ajouter le document 