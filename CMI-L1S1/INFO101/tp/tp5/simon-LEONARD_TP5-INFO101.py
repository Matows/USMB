#!/usr/bin/env python3
# coding: utf-8
__author__ = "Simon LEONARD"
__email__  = "simon.leonard@etu.univ-smb.fr"


def dictionnaire(fichier):
    """
    renvoie la liste de tous les mots contenus dans le fichier dont le nom est passé en argument

    argument : fichier, de type chaine de caractères. C'est le nom du fichier compressé contenant le dictionnaire
    résultat : de type liste de chaines de caractères. Chaque élément de la liste correspond à une ligne du fichier"""
    import zipfile
    import sys
    with zipfile.ZipFile(fichier, 'r') as f:
        l = f.namelist()
        if len(l) != 1:
            raise ValueError("L'archive devrait contenir exactement 1 fichier mais en contient {}".format(len(l)))
        r = f.read(l[0]).decode(encoding="UTF-8", errors="strict").split("\n")
    return [m for m in r if len(m) != 0]

### DICTIONNAIRES
littre = dictionnaire("littre.zip")
dico = dictionnaire("dico.zip")


### QUESTION 1
nb_mots_littre = len(dictionnaire("littre.zip"))
# 73192
nb_mots_dico = len(dictionnaire("dico.zip"))
# 336531


### QUESTION 2
def mots_de_n_lettres(dico, n):
    return [mot for mot in dico if len(mot) == n]

# >>> mots_de_n_lettres(littre, 22)
# ['cristallographiquement', 'disproportionnellement']

# >>> len(mots_de_n_lettres(dico, 10))
# 51402


### QUESTION 3
def mot_commence_par(mot, prefixe):
    return mot.startswith(prefixe)


### QUESTION 4
def liste_mots_commencent_par(dico, prefixe):
    return [mot for mot in dico if mot_commence_par(mot, prefixe)]
# >>> len(liste_mots_commencent_par(littre, "chou"))
# 17


### QUESTION 5
def mot_fini_par(mot, suffixe):
    return mot.endswith(suffixe)

def liste_mots_fini_par(dico, suffixe):
    return [mot for mot in dico if mot_fini_par(mot, suffixe)]
# >>> list_mots_fini_par(littre, "chou")
# ['bachou', 'cachou', 'chabichou', 'chou']


### QUESTION 6
def mots_debut_fin_n(dico, prefixe, suffixe, n):
    return liste_mots_fini_par(liste_mots_commencent_par(mots_de_n_lettres(dico, n), prefixe), suffixe)
# >>> len(mots_debut_fin_n(dico, 'cas', 'ns', 12))
# 7


### QUESTION 7
def mot_correspond(mot, motif):
    if len(mot) != len(motif):
        return False
    else:
        translation_table = {"à":"a", "ä":"a", "â":"a", "ç":"c", "ê":"e", "è":"e", "é":"e", "ë":"e", "î":"i", "ï":"i", "ô":"o", "ö":"o", "ù":"u", "ü":"u", "û":"u"}
        correspond = True

        for char, lettre in zip(motif, mot):
            lettre = translation_table[lettre] if lettre in translation_table else lettre

            if not (char == "." or char == lettre):
                correspond = False
    return correspond

### QUESTION 8
def liste_mots_motif(dico, motif):
    return [mot for mot in dico if mot_correspond(mot, motif)]
# >>> len(liste_mots_motif(dico, "p..h.s"))
# 12


### QUESTION 9 inclu dans la question 7


### QUESTION 10
# apparait() -> innutile : `char in lettres`

def mot_possible(mot, lettres):
    for char in mot:
        if char not in lettres:
            return False # Comme ça, on ne continue pas à vérifié toute les autres lettres
    return True
    # Ancienne solution, pas opti
    #return all([True if char in lettres else False for char in mot])


### QUESTION 11
def mot_optimal(dico, lettres):
    mot_opti = ""
    for mot in dico:
        if mot_possible(mot, lettres) and len(mot) > len(mot_opti):
            mot_opti = mot
    return mot_opti


### QUESTION 12

def mot_possible_scrabble(mot, lettres):
    lettres = list(lettres)
    for char in mot:
        if char in lettres:
            lettres.remove(char)
        else:
            return False # Comme ça, on ne continue pas à vérifié toute les autres lettres
    return True
    # Ancienne solution, pas opti
    #return all([True if char in lettres else False for char in mot])

def mot_optimal_scrabble(dico, lettres):
    mot_opti = ""
    for mot in dico:
        if mot_possible_scrabble(mot, lettres) and len(mot) > len(mot_opti):
            mot_opti = mot
    return mot_opti


### AMUSEMENT ###
fulldico = set(dico + littre)
# Renvoie les mots les plus optimaux de même longeur
# Pour une raison inconnue, le mot "ramie" n'apparait pas avec les lettres "aimer".
def mot_optimal_scrabble_tt_possibilite(dico, lettres):
    mot_opti = []

    for mot in dico:
        if mot_possible_scrabble(mot, lettres):
            mot_opti.append(mot)

    maximum = max([len(mot) for mot in mot_opti])

    return [mot for mot in mot_opti if len(mot) == maximum]


def main(d=fulldico):
    print("\nSCRABBLE WORD FINDER\n")

    while True:
        user = input("Mettre vos lettres : ").lower()
        try:
            print(mot_optimal_scrabble_tt_possibilite(d, user))
        except KeyboardInterrupt:
            break
        except:
            pass

if __name__  == '__main__':
    main()
