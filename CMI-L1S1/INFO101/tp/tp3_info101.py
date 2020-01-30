#!/usr/env python3
# coding: utf-8

### ASSIETTES
def test_piles(*assiettes):
    """
    Retourne s'il est possible d'obtenir des piles d'assiettes de même hauteur.
    En paramètre, un nombre d'assiette par pile doit être fourni.
    """
    return sum(assiettes) % len(assiettes) == 0

def nb_assiettes(*assiettes):
    """Renvoie le nombre d'assiette qu'il doit y avoir par pile pour équilibrer, si c'est possible."""
    return int(sum(assiettes) / len(assiettes)) if test_piles(*assiettes) else -1

def instruction_piles(no_pile, *assiettes):
    """Pour la pile numéro no_pile, la fonction renvoie le nombre d'assiettes à ajouter (chiffre positif) ou à enlever (nombre négatif)"""
    return nb_assiettes(*assiettes) - assiettes[no_pile-1]

### DENTS
def chiffre1(nb):
    """
    Renvoie le chiffre des dizaines
    Prend en paramètre un numéro de dent nb
    """
    return nb // 10 if nb >= 11 and nb <= 48 else -1

def chiffre2(nb):
    return nb % 10 if nb >= 11 and nb <= 48 else -1

def quadrant(no_dent):
    quad = chiffre1(no_dent)
    haut = "en haut"
    bas = "en bas"
    gauche = " à gauche"
    droite  = " à droite"
    return [haut + gauche, haut + droite, bas + droite, bas + gauche][quad-1]

def type_dent(no_dent):
    dent = chiffre2(no_dent)
    r = ""
    if dent == 1 or dent == 2:
        r = "incisive"
    elif dent == 3:
        r = "canine"
    elif dent == 4 or dent == 5:
        r = "pré-molaire"
    elif dent >= 6 and dent <= 8:
        r = "molaire"
    else:
        raise ValueError

    return r

def designation_dent(no_dent):
    return "C'est une {} située {}.".format(type_dent(no_dent), quadrant(no_dent))

def est_dent(no_dent, type_suppose):
    return type_dent(no_dent) == type_suppose

def verif_nodent(no_dent):
    return type(no_dent) == int and no_dent >= 11 and no_dent <= 48
