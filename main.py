# main:
# choix_menu():

# choix_menu():
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
#   pseudo = demander_pseudo()
#   equipe = creer_equipe()
#   monstres = recuperer_liste(Monstres)
#   score = lancer_partie(equipe, monstres)
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
#   score = 0
#   boucle tant que si_equipe_vivante():
#       lancer_vague(equipe, monstres, score)
#       si_equipe_vivante:
#           score += 1
#       afficher_info_vague(score)

# lancer_vague(equipe, monstres, score):
#   monstre = recuperer_monstre(monstres)
#   lancer_combat(equipe, monstre)

# si_equipe_vivante():
#   pour tout membre dans équipe:
#       retourne si_vivant(member)

# si_vivant(personnage):
#   si hp de personnage > 0:
#       retourner Vrai
#   retourner Faux

# afficher_info_vague(score):
#   affiche f"Tour numéro : {score}"

# récuperer_monstre(monstres):
#   retourner un élement aléatoire dans la liste monstres

# lancer_combat(equipe, monstre):
#   boucle tant que si_vivant(monstre) et si_equipe_vivante(equipe):
#       equipe_attaque_monstre(equipe, monstre)
#       si_vivant(monstre):
#           monstre_attaque_equipe(monstre, equipe)

# equipe_attaque_monstre(equipe, monstre):
#   pour chaque personnage dans equipe:
#       attaque(personnage, equipe)

# monstre_attaque_equipe(monstre, equipe):
#   personnage = personnage_aléatoire(equipe)
#   attaque(monstre, personnage)

# personnage_aléatoire(equipe):
#   equipe_vivante = récuperer_personnages_vivants(equipe, [])
#   retourner personnage aléatoire dans equipe_vivante

# récuperer_personnages_vivants(equipe, equipe_vivante):
#   pour chaque personnage dans equipe:
#       si hp personnage > 0:
#           ajouter personnage dans equipe_vivante

# attaque(attaquant, cible):
#   hp de la cible - (attaque de l'attaquant - defense de la cible)

# classement():
#   score_list = recuperer_liste(Score)
#   pour i jusqu'à len(score_list):
#       Afficher f"{placement} -> {nom} : {score} \n" de score_list[i]

# ajouter_score(score, pseudo):
#   score_list = recuperer_liste(Score)
#   ajouter_place_correcte(score_list, score)

# ajouter_place_correcte(score_list, score):
#   de i jusqu'à len(score_list):
#       si le score au score_list[i] est < score:
#           insère score à score_list[i]
#           break