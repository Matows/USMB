#!/usr/bin/env python3
# coding: utf-8


def position(T, s):
    """renvoie la position de la chaine s dans la liste T
    Si s n'appartient pas à la liste T, la fonction renvoie -1 à la place.

    T: liste de chaine de caractères
    s: chaine de caractère
    résultat: nombre entier
    """
    try:
        return T.index(s)
    except ValueError:
        return -1


def lz78_compresse(texte):
    """applique l'algorithme de compression LZ78 sur la chaine ``texte``

    Le résultat est une liste [entier, caractère, entier, caractère, ...] se
    terminant soit sur un caractère, soit sur un entier.

    texte: chaine de caractères
    résultat: liste alternée d'entiers et caractères
    """
    resultat = []        # liste alternée de nombres / lettres
    dico = [""]
    mot_courant = ""     # initialisation des variables dico, et mot_courant
    for i in range(0, len(texte)):
        c = texte[i]
        pos = position(dico, mot_courant + c)
        if not (pos == -1):  # on teste si mot_courant+c est dans la liste dico
            mot_courant = mot_courant + c
        else:
            resultat.append(position(dico, mot_courant))
            resultat.append(c)
            dico.append(mot_courant + c)
            mot_courant = ""
    # gestion dernier mot_courant 
    pos = position(dico, mot_courant)
    if pos != 0:
        resultat.append(pos)
    return resultat

def lz78_decompresse(code):
    """applique l'algorithme de décompression LZ78 sur la liste ``code``

    code: liste alternée d'entiers et caractères
    résultat: chaine de caractères
    """
    dico = [""]
    resultat = ""
    last = 0
    for i, case in enumerate(code): # case : entier ou chaine
        if i % 2 == 0:
            resultat += dico[case]
            last = case
        else:
            resultat += case
            dico.append( dico[last] + case)

    return resultat

def test_lz78(texte):
    compressed = lz78_compresse(texte)
    decompressed = lz78_decompresse(compressed)
    print(f"\nchaine de départ : '{texte}'\n-----\nrésultat compressé : {compressed}\n-----\nrésultat décompressé : '{decompressed}'\n-----")
    if texte == decompressed:
        print("OK")
    else:
        print("PROBLÈME : le résultat décompressé est différent de la chaine de départ !")

def octets(T):
    """transforme une liste alternée d'entiers et caractères en tableau d'octets"""
    r = bytearray()
    for e in T:
        if isinstance(e, int):
            if not 0 <= e < 256:
                raise RuntimeError("*** Problème, l'entier {} n'est pas compris entre 0 et 255 !".format(e))
            r.append(e)
        elif isinstance(e, str):
            if len(e) != 1:
                raise RuntimeError("*** Problème, les caractères doivent être donnés un par un !")
            try:
                r.extend(e.encode("ASCII"))
            except UnicodeEncodeError:
                raise RuntimeError("*** Problème, '{}' n'est pas un caractère ASCII !".format(repr(e)))
        else:
            raise RuntimeError("*** Problème, '{}' n'est ni un entier, ni un caractère !".format(repr(e)))
            sys.exit(-1)
    return r

def lz78_compresse_bin(texte):
    """applique l'algorithme de compression sur la chaine ``texte``

    texte: chaine de caractères
    résultat: liste d'octets.
    """
    return octets(lz78_compresse(texte))

def ascii(T):
    """transforme une liste d'octet en caractère ASCII"""
    r = []
    for i,e in enumerate(T):
        try:
            if i % 2 == 0:
                r.append(e)
            else:
                r.append(bytes([e]).decode(encoding="ASCII"))
        except UnicodeDecodeError:
            raise RuntimeError("*** Problème, '{}' ne correspond pas à un caractère ASCII !".format(n))
    return r

def lz78_decompresse_bin(code):
    """applique l'algorithme de décompression LZ78 sur ``code``

    code: liste d'octets
    résultat: chaine de caractères
    """
    return lz78_decompresse(ascii(code))

def test_lz78_bin(texte):
    compressed = lz78_compresse_bin(texte)
    decompressed = lz78_decompresse_bin(compressed)
    print(f"\nchaine de départ : '{texte}'\n-----\nrésultat compressé : {compressed}\n-----\nrésultat décompressé : '{decompressed}'\n-----")
    if texte == decompressed:
        print("OK")
    else:
        print("PROBLÈME : le résultat décompressé est différent de la chaine de départ !")
