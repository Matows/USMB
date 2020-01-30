#!/usr/bin/env python3
# coding: utf-8

__author__ = "Simon LÉONARD"
__email__  = "simon.leonard@etu.univ-smb.fr"

def nb_jours(months: list) -> int:
    """Retourne la somme du nombre de jours des mois de _months_
        months: liste de mois valide (e.g.: mars, avril)
    """

    jours = {
        'janvier':    31,
        'février':    28,
        'févrierB':   29,
        'mars':       31,
        'avril':      30,
        'mai':        31,
        'juin':       30,
        'juillet':    31,
        'aout':       31,
        'septembre':  30,
        'octobre':    31,
        'novembre':   30,
        'decembre':   31
    }

    return sum([jours.get(month, 0) for month in months])

def lire_mots(nom_fichier):
    """fonction qui récupère la liste des mots dans un fichier

    paramètre
      - nom_fichier, de type chaine de caractère : nom du fichier contenant les mots
        (un par ligne)

    retour : liste de chaine de caractères
    """
    liste_mots = []                             # le tableau qui contiendra les lignes
    with open(nom_fichier, encoding="UTF-8") as f: # on ouvre le fichier
        ligne = f.readline()                    # une variable temporaire pour récupérer la ligne courante dans le fichier f
        while ligne != "":
            liste_mots.append(ligne.strip())    # on rajoute la ligne courante dans le tableau
            ligne = f.readline()                # on récupère la ligne suivante
    return liste_mots

# >>>len(lire_mots("littre.txt"))
# 

def nouvel_etat(mot, etat, c):
    """fonction qui renvoie le nouvel état après proposition d'une lettre c

    paramètres :
      - mot, de type chaine de caractères,
      - etat, de type chaine de caractères : les lettres inconnues sont
        représentées par des '_'. Cette chaine a la même longueur que le paramètre
        mot,
      - c, de type caractère : la lettre proposée.

    retour : chaine de caractère où les "_" correspondant au paramètre c ont été remplacés par c
    """
    nouvel_etat = ""
    c = c.upper()
    for i, lettre in enumerate(mot):
        if lettre.upper() != c:
            nouvel_etat += etat[i]
        else:
            nouvel_etat += c
    return nouvel_etat

def test3():
    mot = "CANARI"                              # mot secret
    etat = "C___RI"                             # état : le joueur a déjà trouvé les lettres "C", "R" et "I"
    etat2 = nouvel_etat(mot, etat, "a")     # mise à jours de l'état avec une nouvelle lettre
    print("mot :", etat2)                       # affichage du nouvel etat


from random import choice # choisi un élément au hasard dans une liste

def pendu_version1(nb_erreur_max: int, new_stat=nouvel_etat):
    """Procédure affichant le jeu du pendu version 1
        Le paramètre new_stat contient la fonction nouvel_etat, pour éviter de recopier tout le code quand on passe à nouvel_etat_version2 
    """
    # Init
    mot = choice(lire_mots("littre.txt")) 
    etat = "_" * len(mot)
    nb_erreur = nb_erreur_max

    # Jeu
    while nb_erreur > 0 and etat != mot:

        print('\n', affiche_etat(etat))
        print(f"Vous pouvez encore faire {nb_erreur} erreurs.")
        lettre = input("Entrez une lettre suivie d'un saut de ligne : ").strip()

        etat_nouveau = new_stat(mot, etat, lettre)

        if etat != etat_nouveau:
            print("Bravo !")
            etat = etat_nouveau

        else:
            print("Dommage...")
            nb_erreur -= 1

    # Conclusion
    print("\n")
    if etat == mot:
       print(f"Gagné !\nLe mot était bien \'{mot}\'") 

    elif nb_erreur == 0:
        print(f"Perdu...\nLe mot était \'{mot}\'")

    else:
        print("Ninja !")

def affiche_etat(etat):
    """Retourne _etat_ avec des espaces entre chaque lettre
        e.g.: "E_AN" => "E _ A N"
    """
    return " ".join(etat)


def nouvel_etat_version2(mot, etat, c):
    """fonction qui renvoie le nouvel état après proposition d'une lettre c

    paramètres :
      - mot, de type chaine de caractères,
      - etat, de type chaine de caractères : les lettres inconnues sont
        représentées par des '_'. Cette chaine a la même longueur que le paramètre
        mot,
      - c, de type caractère : la lettre proposée.

    retour : chaine de caractère où les "_" correspondant au paramètre c ont été remplacés par c
    """

    variantes = {
        'A': 'AÀÄÂÆ',
        'C': 'CÇ',
        'E': 'EÊÈÉËÆŒ',
        'I': 'IÎÏ',
        'O': 'OÔÖOEŒ',
        'U': 'UÙÜÛ'
    }

    nouvel_etat = ""
    c = c.upper()
    for i, lettre in enumerate(mot):
        if lettre in variantes.get(c, c): # Si la lettre est présente
            nouvel_etat += lettre
        else:
            nouvel_etat += etat[i]
    return nouvel_etat

def test5():
    mot = "ÉPIQUE"
    etat = "_P_Q__"
    etat2 = nouvel_etat_version2(mot, etat, "e")
    print("mot :", etat2)

# On utilise juste nouvel_etat_version2 au lieu de nouvel_etat
pendu_version2 = lambda nb_erreur_max: pendu_version1(nb_erreur_max, nouvel_etat_version2)

def mots_longueur(liste_mots: list, n: int) -> list:
    """fonction qui renvoie la liste des chaines d'une longueur donnée dans une
    liste

    paramètres :
      - liste_mots, de type liste de chaines de caractères
      - n, de type entier

    retour : liste de chaines de caractères: tous les éléments de mots qui ont la
    longueur n
    """
    return [mot for mot in lire_mots("littre.txt") if len(mot) == n]


## REPRIS DU PREMIER SEMESTRE ##
def mot_correspond(mot: str, motif: str) -> bool:
    """Retourne True si le motif correspont au mot
        e.g.:  mot_correspond("evan", "e__n") => True
               mot_correspond("Simon", "s_m") => False
    """
    if len(mot) != len(motif):
        return False
    else:
        correspond = True

        for char, lettre in zip(motif, mot):
            if not (char == "_" or char == lettre):
                correspond = False
    return correspond
def liste_mots_motif(dico, motif):
    """Retourne la liste des mots correspondant au motif"""
    return [mot for mot in dico if mot_correspond(mot, motif)]
## FIN ##


def pendu_version3(nb_erreur_max: int):
    """Procédure affichant le jeu du pendu version 3"""
    # Init
    mot = choice(lire_mots("littre.txt")) 
    etat = "_" * len(mot)
    nb_erreur = nb_erreur_max
    littre = lire_mots("littre.txt") #dico
    lettres = [] # lettres déjà utilisé

    # Jeu
    while nb_erreur > 0 and etat != mot:

        print('\n', affiche_etat(etat))
        print(f"Vous pouvez encore faire {nb_erreur} erreurs.")
        print("Il y a encore %i mot possible" % len(liste_mots_motif(littre, etat)))

        lettre = input("Entrez une lettre suivie d'un saut de ligne : ").strip()
        if lettre in lettres:
            continue
        lettres.append(lettre)

        etat_nouveau = nouvel_etat_version2(mot, etat, lettres[-1])

        if etat != etat_nouveau:
            print("Bravo !")
            etat = etat_nouveau

        else:
            print("Dommage...")
            nb_erreur -= 1

    # Conclusion
    print("\n")
    if etat == mot:
       print(f"Gagné !\nLe mot était bien \'{mot}\'") 

    elif nb_erreur == 0:
        print(f"Perdu...\nLe mot était \'{mot}\'")

    else:
        print("Ninja !")

def affiche_pendu(n):
    """procédure qui affiche le pendu en fonction du nombre d'erreurs

    paramètre :
      - n, de type entier (compris entre 0 et 7 inclus)
    """
    pendu_final = r"""
  --------------
    |        |
    |        |
    |       / \
    |       \_/
    |      __|__
    |        |
    |        |
    |       / \
   /|\     /   \
  / | \
 /  |  \
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
    pendu_numero = r"""
  --------------
    |        1
    |        1
    |       2 2
    |       222
    |      55344
    |        3
    |        3
    |       6 7
   /|\     6   7
  / | \
 /  |  \
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
    for nb in range(1,8): # Pour chaque partie du pendu
        occurance = pendu_numero.count(str(nb)) # Nombre de chiffre _nb_ dans pendu_numero

        for i in range(occurance): # Pour chacun des chiffres _nb_, on remplace par le caractère correspondant
            position = pendu_numero.index(str(nb))
            pendu_numero = pendu_numero.replace(str(nb), (pendu_final[position] if n >= nb else " "), 1)
    print(pendu_numero, end="")

def pendu_version4(dico: dict):
    """Procédure affichant le jeu du pendu version 4"""
    # Init
    mot = choice(dico) 
    etat = "_" * len(mot)
    nb_erreur = 7
    lettres = [] # Lettres déjà utilisé

    # Jeu
    while nb_erreur > 0 and etat != mot:

        affiche_pendu(7 - nb_erreur)
        print(affiche_etat(etat))
        print(f"Vous pouvez encore faire {nb_erreur} erreurs.")
        print("Il y a encore %i mot possible" % len(liste_mots_motif(dico, etat)))
        lettre = input("Entrez une lettre suivie d'un saut de ligne : ").strip()
        if lettre in lettres:
            continue
        lettres.append(lettre)

        etat_nouveau = nouvel_etat_version2(mot, etat, lettres[-1])

        if etat != etat_nouveau:
            print("Bravo !")
            etat = etat_nouveau

        else:
            print("Dommage...")
            nb_erreur -= 1

    # Conclusion
    print("\n")
    if etat == mot:
       print(f"Gagné !\nLe mot était bien \'{mot}\'") 

    elif nb_erreur == 0:
        print(f"Perdu...\nLe mot était \'{mot}\'")

    else:
        print("Ninja !")

def affiche_pendu_version2(n: int, nb_erreur_max: int):
    """procédure qui affiche le pendu en fonction du nombre d'erreurs

    paramètres :
      - n, de type entier (compris entre 0 et nb_erreur_max inclus)
      - nb_erreur_max, de type entier (compris entre 7 et 11 inclus)
    """
    pendu_final = r"""
  --------------
    |        |
    |        |
    |       / \
    |       \_/
    |      __|__
    |        |
    |        |
    |       / \
   /|\     /   \
  / | \
 /  |  \
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
    pendu_numero = r"""
  DDDDDDDDDDDDDD
    A        1
    A        1
    A       2 2
    A       222
    A      55344
    A        3
    A        3
    A       6 7
   BAC     6   7
  B A C
 B  A  C
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~
"""
    ## Construction de la liste des parties à afficher en fonction de nb_erreur_max
    base = [str(nb) for nb in range(1,8)] # Liste des entiers [1;7]

    # dictionnaire des étapes d'évolution en fonction de nb_erreur_max
    etapes = {  # ABCD à l'étape 0, puis 1, puis 2...
                7: ["ABCD"] + base,
                # rien à étape 0, puis ABCD, puis 1, puis 2...
                8: [""] + ["ABCD"] + base,
                # rien à étape 0, puis A, puis BCD, 1, 2...
                9: [""] + ["A"] + ["BCD"] + base,
                # rien à l'étape 0, puis A, puis BC, puis D, puis 1...
                10: [""] + ["A"] + ["BC"] + ["D"] + base,
                # A, B, C, D, 1, 2...
                11: list("ABCD") + base
              }
    etapes = etapes[nb_erreur_max]


    ## Affichage par étapes (en fonction de n)
    nouveau_pendu = ""
    # Pour chaque caractère on détermine si il doit...
    for i,char in enumerate(pendu_numero):
        # ...être affiché...
        if char in "".join(etapes[:n+1]):
            nouveau_pendu += pendu_final[i]
        # ... ou ignoré.
        elif char in "ABCD1234567":
            nouveau_pendu += " "
        # On ne touche pas au reste ('\n', '~'...)
        else:
            nouveau_pendu += pendu_final[i]

    print(nouveau_pendu)

def pendu_version5(dico: dict, nb_erreur_max:int):
    """Procédure affichant le jeu du pendu version 5"""
    # Init
    mot = choice(dico) 
    etat = "_" * len(mot)
    nb_erreur = nb_erreur_max
    lettres = [] # Lettres déjà utilisé

    # Jeu
    while nb_erreur > 0 and etat != mot:

        affiche_pendu_version2(nb_erreur_max - nb_erreur, nb_erreur_max)
        print(affiche_etat(etat))
        print(f"Vous pouvez encore faire {nb_erreur} erreurs.")
        print("Il y a encore %i mot possible" % len(liste_mots_motif(dico, etat)))
        
        lettre = input("Entrez une lettre suivie d'un saut de ligne : ").strip()
        if lettre in lettres:
            continue
        lettres.append(lettre)

        etat_nouveau = nouvel_etat_version2(mot, etat, lettres[-1])

        if etat != etat_nouveau:
            print("Bravo !")
            etat = etat_nouveau

        else:
            print("Dommage...")
            nb_erreur -= 1

    # Conclusion
    print("\n")
    if etat == mot:
       print(f"Gagné !\nLe mot était bien \'{mot}\'") 

    elif nb_erreur == 0:
        print(f"Perdu...\nLe mot était \'{mot}\'")

    else:
        print("Ninja !")
