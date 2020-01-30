#!/usr/bin/env python3
# NOM : Simon LÉONARD
# FILIÈRE : CMI-INFO L1

from image import Image
from math import sqrt
from itertools import filterfalse


##############
# Question 1 #
##############
def jeDecouvreLaBibliothequeImage(fichier):
    """
    Cette fonction a pour but d'illustrer les différentes fonctions de la
    bibliothèque que nous allons utiliser, à savoir:
        - Image
        - width
        - height
        - getPixel
        - setPixel
        - save
    """
    # Décommentez les lignes pertinentes pour découvrir le fonctionnement de
    # la bibliothèque.
    #
    # N'hésitez pas à modifier ces lignes et à réexécuter la fonction pour bien
    # comprendre le fonctionnement.

    # Pour charger une image, on appelle le 'constructeur' ``Image(fichier)``
    # où ``fichier`` est le nom d'une image au format PPM.
    im = Image(fichier)

    # Les attributs ``.width`` et ``.height`` permettent de récupérer,
    # respectivement, le nombre de colonnes et le nombre de lignes.
    l = im.width
    h = im.height
    print("Cette image est formée de {} colonnes et {} lignes".format(l, h))

    # La fonction ``.getPixel(x,y)`` retourne la couleur du pixel situé à
    # la colonne ``x`` et la ligne ``y``.
    #
    # Ainsi, l'image est vu comme un plan cartésien dont l'axe des y pointe
    # vers le bas:
    #
    #      | 1 2 3 4 5 6 7 8 9 ...
    #     -+--------------------------> x
    #    1 |
    #    2 |               p
    #    3 |
    #    4 |
    #      V
    #      y
    #
    #    Coordonnées (x,y) du point p: (8,2)
    #
    # Note: les couleurs sont représentées par des triplets (r,g,b) (càd des
    #       tableaux à 3 éléments) où r, g et b sont des entiers dans
    #       l'intervalle de 0 à 255 (inclusivement) désignant, respectivement,
    #       l'intensité de rouge (r), de vert (g) et de bleu (b). Ainsi,
    #       (255,0,0) représente la couleur rouge, (0,255,0) le vert et
    #       (0,0,255) le bleu. On note que (255,255,255) est blanc et (0,0,0)
    #       est noir.
    #
    c = im.getPixel(0, 0)
    print("Le pixel en (0,0) est de couleur: {}".format(c))

    # Récupérer les couleurs une par une:
    r = c[0]
    g = c[1]
    b = c[2]
    print("L'intensité de rouge du pixel (0,0) est: {}".format(r))
    print("L'intensité de vert  du pixel (0,0) est: {}".format(g))
    print("L'intensité de bleu  du pixel (0,0) est: {}".format(b))

    # La fonction ``.setPixel(x, y, c)`` affecte la couleur ``c`` au
    # pixel ``(x,y)``.
    # On met le pixel (1,0) en rouge.
    im.setPixel(1, 0, (255,0,0))

    # On trace une ligne noire horizontale sur toute la.width de l'image.
    y = im.height // 2
    for x in range(im.width):
        im.setPixel(x, y, (0,0,0))

    # On trace une ligne blanche verticale sur toute la.height de l'image.
    x = im.width // 2
    for y in range(im.height):
        im.setPixel(x, y, (255,255,255))

    # La fonction ``.save(fichier)`` écrit l'image dans un fichier.
    # L'extension de ce fichier doit être ".ppm"
    im.save("question-1.ppm")
    # Vous pouvez visualiser les trois modification apportées en visualisant
    # l'image "question-1.ppm".


##############
# Question 2 #
##############
def ImageBinaire(fichierIn, fichierOut):
    """
    Charge l'image ``fichierIn`` et remplace la couleur de chaque pixel par du
    blanc ou du noir.
    Paramètes:
        fichierIn  --> Nom du fichier où lire l'image à traiter.
        fichierOut --> Nom du fichier où écrire l'image finale.

    Si le pixel est 'clair' alors il devient blanc.
    Si le pixel est 'foncé' alors il devient noir.

    Un pixel est 'clair' si la somme de ses canaux r, g et b est SUPÉRIEUR OU
    ÉGALE à 382.

    Un pixel est 'foncé' si la somme de ses canaux r, g et b est INFÉRIEURE à
    382.

    L'image résultante est sauvegardée dans le fichier ``fichierOut``.
    """

    filein = Image(fichierIn)
    fileout = Image(filein.width,filein.height)

    # Pour chaque pixel
    for x in range(filein.width):
        for y in range(filein.height):
            fileout.setPixel(x, y,
                            ( (255,255,255) if sum(filein.getPixel(x,y)) >= 382 else (0,0,0) ))
    fileout.save(fichierOut)


##############
# Question 3 #
##############
def couleurDiff(c1, c2):
    """
    Retourne la 'différence' entre les couleurs ``c1`` et ``c2``.

    Paramètres:
        c1: Première couleur
        c2: Deuxième couleur
    On définit cette 'différence' comme étant la somme des carrés des
    différences d'intensité pour les trois canaux rouge, vert et bleu.

    De manière équivalente, si on voit les tuples (r,g,b) comme étant des
    points dans R^3, cette 'différence' est le carré de la distance (calculée
    par Pythagore) entre les points c1 et c2.
    """
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    return (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2


##############
# Question 4 #
##############
def troisNuancesDeGris(fichierIn, fichierOut):
    """
    Charge l'image ``fichierIn`` et remplace la couleur de chaque pixel par du
    blanc, du gris ou du noir.

    Paramètres:
        fichierIn  --> Nom du fichier où lire l'image à traiter.
        fichierOut --> Nom du fichier où écrire l'image finale.
    Chaque pixel est remplacé par la couleur lui 'ressemblant' le plus parmi
    blanc (255,255,255), gris (127,127,127) et noir (0,0,0).

    Autrement dit, on cherche quelle couleur parmi blanc, gris et noir minimise
    la valeur de ``couleurDiff``.

    L'image résultante est sauvegardée dans le fichier ``fichierOut``.
    """

    filein = Image(fichierIn)
    fileout = Image(filein.width,filein.height)

    black, grey, white = (255,255,255), (127,127,127), (0,0,0) # Raccourci

    # Pour chanque pixel
    for x in range(filein.width):
        for y in range(filein.height):
            px = filein.getPixel(x,y)
            # diff de la forme {différence_couleurs : couleur_référence,...}
            diff = {
                couleurDiff(px, black): black,
                couleurDiff(px, grey): grey, 
                couleurDiff(px, white): white
            }
            # Remplace par la couleur de référence ayant le meilleur résultat
            fileout.setPixel(x, y, diff[min(diff.keys())] ) 
    fileout.save(fichierOut)



##############
# Question 5 #
##############
def plusSemblable(c, l):
    """
    Détermine la couleur qui 'ressemble' le plus à ``c`` parmi celles de ``l``.

    Paramètres:
        c --> une couleur, c'est-à-dire un tuple (r,g,b).
        l --> une liste de couleurs, c'est-à-dire une liste de tuples (r,g,b).

    Recherche quelle couleur parmi celles contenues dans ``l`` minimise la
    valeur de ``couleurDiff`` avec ``c``.
    """
    # diff de la forme {différence_couleurs : couleur_référence,...}
    diff = {couleurDiff(c, color): color for color in l}
    return diff[min(diff.keys())] # Renvoie la couleur de référence ayant le meilleur résultat


##############
# Question 6 #
##############
def repeindre(im, l):
    """
    Repeint une image.

    Paramètres:
        im --> image à repeindre,
        l  --> liste de couleurs.

    Remplace la couleur de chaque pixel de ``im`` par la couleur de ``l`` qui
    lui ressemble le plus.
    """
    # pour chaque pixel
    for x in range(im.width):
        for y in range(im.height):
            new_color = plusSemblable(im.getPixel(x,y), l)
            im.setPixel(x, y, new_color)
    return im

##############
# Question 7 #
##############
def genKgris(k):
    """
    Calcule une liste de ``k`` teintes de gris allant du noir au blanc.

    Paramètre:
        k --> nombre de teintes (>=2)

    La liste génére doit nécessairement commencer par la couleur noir (0,0,0)
    et nécessairement terminer par la couleur blanc (255,255,255).

    Les autres valeurs doivent être des teintes de gris uniformément réparties
    entre le noir et le blanc.

   :: EXEMPLES::

    >>> genKgris(2)
    [(0, 0, 0), (255, 255, 255)]
    >>> genKgris(3)
    [(0, 0, 0), (127, 127, 127), (255, 255, 255)]
    >>> genKgris(4)
    [(0, 0, 0), (85, 85, 85), (170, 170, 170), (255, 255, 255)]
    """
    coef = 255//(k-2+1) # -2 (blanc et noir) +1 (1 élément minimum)
    # teintes contient les valeurs de chaque pixel pour éviter la répétition
    # teintes commence et fini par du blanc...
    teintes = [0]
    teintes += [n*coef for n in range(1, k-1)] # valeurs intermédiaires
    # et se fini par du noir.
    teintes += [255]

    return [(v,v,v) for v in teintes] # On traduit en pixels


##############
# Question 8 #
##############
def dansCercle(x,y, cx,cy, r):
    """
    Teste l'appartenance à un cercle.

    Paramètres:
        (x,y)   --> point à tester,
        (cx,cy) --> centre du cercle,
        r       --> rayon du cercle.

    Retourne ``Vrai`` si le point est dans le cercle, ``Faux`` sinon.
    """
    return (x-cx)**2 + (y-cy)**2 <= r**2


def dansRectangle(x,y, cx,cy, L, H):
    """
    Test l'appartenance à un rectangle.

    Paramètres:
        (x,y)   --> point à tester,
        (cx,cy) --> coin supérieur gauche du rectangle,
        L       -->.width du rectangle,
        H       -->.height du rectangle.

    Retourne ``Vrai`` si le point est dans le rectangle, ``Faux`` sinon.
    """
    return cx <= x <= cx+L and cy <= y <= cy+H


def repeindreSi(im, l, pred):
    """
    Repeint une image avec une condition sur les pixels.

    Paramètres:
        im   --> image à repeindre,
        l    --> liste de couleurs,
        pred --> prédicat sur les coordonnées des pixels.

    Chaque pixel de l'image dont les coordonnées (x,y) satisfont prédicat
    ``pred`` voit sa couleur remplacée par celle de ``l`` qui lui ressemble le
    plus.

    """
    # pour chaque pixel
    for x in range(im.width):
        for y in range(im.height):
            if pred(x,y):
                im.setPixel(x,y, plusSemblable(im.getPixel(x,y), l))
    return im



##############
# Question 9 #
##############
def faireNBandes(im, n):
    """
    Repeint une image en ``n`` bandes verticales comportant de plus en plus de
    niveaux de gris.

    Paramètres:
        im --> image à repeindre,
        n  --> nombre de bandes verticales.

    Votre fonction doit obligatoirement utiliser les fonctions:
        repeindreSi, genKgris et dansRectangle.

    Les bandes doivent être de.width égales. La première contient 2 niveaux
    de gris, la deuxième en contient 3 et ainsi de suite, jusqu'à la n-ième qui
    contient n+1 niveaux de gris.

    Note: pour chaque bande, vous devez définir un nouveau prédicat.
    """
    coef = (im.width-1)//n # Chaque point d'origine de rectangle/bande est un muptiple de coef
    points = [k*coef for k in range(n)] # abscisses des points de début de bande
    bande_width = points[1] - points[0] - 1

    for i, point in enumerate(points):
        # Prend en charge la dernière bande
        bande_width = im.height if point == points[-1] else bande_width 

        # On défini les paramètres immuable pour la bande en cours
        pred = lambda l,h: dansRectangle(l,h, point,0, bande_width,im.height) 

        repeindreSi(im,genKgris(i+2),pred)
    return im


###############################################################
# ########################################################### #
# #     ___  ___________________   ________________  __  __ # #
# #    /   |/_  __/_  __/ ____/ | / /_  __/  _/ __ \/ | / / # #
# #   / /| | / /   / / / __/ /  |/ / / /  / // / / /  |/ /  # #
# #  / ___ |/ /   / / / /___/ /|  / / / _/ // /_/ / /|  /   # #
# # /_/  |_/_/   /_/ /_____/_/ |_/ /_/ /___/\____/_/ |_/    # #
# #                                                         # #
# ########################################################### #
###############################################################

# Toutes les modifications effectuées au code ci-dessous seront ignorées lors
# de la correction.


def testKgris(lesGris, k):
    """
    Fonction pour tester le résultat de la fonctio ``genKgris`` (question 7).
    --> NE PAS MODIFIER ! <--
    """
    if tuple(lesGris[0]) != (0,0,0):
        print("[testKgris] ERREUR: Doit commencer par (0,0,0).")
        return False
    if tuple(lesGris[-1]) != (255,255,255):
        print("[testKgris] ERREUR: doit terminer par (255,255,255).")
        return False
    if len(lesGris) != k:
        print("[testKgris] ERREUR: ne contient pas k (={}) teintes différentes.".format(k))
        return False
    if list(filterfalse(lambda x: x[0] == x[1] == x[2], lesGris)) != []:
        print("[testKgris] ERREUR: ne contient pas que des gris.".format(k))
        return False
    if list(filterfalse(lambda x: isinstance(x,int), [x for c in lesGris for x in c])) != []:
        print("[testKgris] ERREUR: couleurs non définie sur des entiers.")
        return False
    diff = [lesGris[i][0] - lesGris[i-1][0] for i in range(1, len(lesGris))]
    if max(diff) - min(diff) > 1:
        print("[testKgris] ERREUR: gradation des teintes non régulière.".format(k))
        return False
    return True


def testTP1(n):
    """
    n est le numéro de la question à tester
    """

    # Les exemples d'images...
    image1 = "moulin.ppm"
    # image1 = "neige.ppm"
    image2 = "fruits.ppm"
    # image2 = "sushis.ppm"
    image3 = "vague.ppm"

    # On définit quelques couleurs
    blanc = (255, 255, 255)
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    bleu = (0, 0, 255)
    jaune = (255, 255, 0)
    gris = (127, 127, 127)
    vertpomme = (91, 194, 54)

    # Et quelques listes de couleurs
    bgn = [blanc, gris, noir]
    couleurs = [blanc, noir, rouge, vert, bleu, jaune, gris, vertpomme]

    # Question 1
    if n == 1:
        print('# Question 1: voir fichier "question-1.ppm"')
        jeDecouvreLaBibliothequeImage(image1)

    # Question 2
    if n == 2:
        ImageBinaire(image1, "question-2.ppm")
        print('# question 2: voir fichier "question-2.ppm"')

    # Question 3
    # On définit quelques couleurs.
    if n == 3:
        if couleurDiff(blanc, noir) != 195075:
            print("[ERREUR] question 2, mauvaise diff pour blanc et noir")
        elif couleurDiff(blanc, rouge) != 130050:
            print("[ERREUR] question 2, mauvaise diff pour blanc et rouge")
        elif couleurDiff(blanc, vert) != 130050:
            print("[ERREUR] question 2, mauvaise diff pour blanc et vert")
        elif couleurDiff(blanc, jaune) != 65025:
            print("[ERREUR] question 2, mauvaise diff pour blanc et jaune")
        elif couleurDiff(vertpomme, jaune) != 33533:
            print("[ERREUR] question 2, mauvaise diff pour vertpomme et jaune")
        elif couleurDiff(vertpomme, blanc) != 71018:
            print("[ERREUR] question 2, mauvaise diff pour vertpomme et blanc")
        elif couleurDiff(vertpomme, noir) != 48833:
            print("[ERREUR] question 2, mauvaise diff pour vertpomme et noir")
        elif couleurDiff(vertpomme, vertpomme) != 0:
            print("[ERREUR] question 2, mauvaise diff pour vertpomme et vertpomme")
        else:
            print("# Question 3: couleurDiff --> OK")

    # Question 4
    if n == 4:
        troisNuancesDeGris(image1, "question-4.ppm")
        print('# Question 4: voir fichier "question-4.ppm"')

    # Question 5
    if n == 5:
        if plusSemblable((199, 84, 16), couleurs) != rouge:
            print("[ERREUR] question 5, (199, 84, 16) devrait trouver rouge")
        elif plusSemblable((225, 230, 43),  couleurs) != jaune:
            print("[ERREUR] question 4, (225, 230, 43) devrait trouver jaune")
        elif plusSemblable((246, 162, 84),  couleurs) != jaune:
            print("[ERREUR] question 4, (246, 162, 84) devrait trouver jaune")
        elif plusSemblable((240, 185, 136), couleurs) != gris:
            print("[ERREUR] question 4, (240, 185, 136) devrait trouver gris")
        elif plusSemblable((189, 132, 10),  couleurs) != vertpomme:
            print("[ERREUR] question 4, (189, 132, 10) devrait trouver vertpomme")
        elif plusSemblable((112, 126, 55),  couleurs) != vertpomme:
            print("[ERREUR] question 4, (112, 126, 55) devrait trouver vertpomme")
        elif plusSemblable((133, 73, 213),  couleurs) != gris:
            print("[ERREUR] question 4, (133, 73, 213) devrait trouver gris")
        elif plusSemblable((246, 68, 114),  couleurs) != rouge:
            print("[ERREUR] question 4, (246, 68, 114) devrait trouver rouge")
        elif plusSemblable((64, 27, 0),     couleurs) != noir:
            print("[ERREUR] question 4, (64, 27, 0) devrait trouver noir")
        elif plusSemblable((134, 238, 190), couleurs) != gris:
            print("[ERREUR] question 4, (134, 238, 190) devrait trouver gris")
        else:
            print("# Question 5: plusSemblable --> OK")

    # Question 6
    if n == 6:
        im = Image(image1)
        repeindre(im, bgn)
        im.save("question-6a.ppm")
        print("# Question 6: l'image \"question-6a.ppm\" doit être identique à \"question-4.ppm\"")

        im = Image(image2)
        repeindre(im, couleurs)
        im.save("question-6b.ppm")
        print('# Question 6: voir fichier "question-6b.ppm"')

    # Question 7
    if n == 7:
        for k in range(2, 20):
            l = genKgris(k)
            testKgris(l, k)

        im = Image(image1)
        l = genKgris(16)
        repeindre(im, l)
        im.save("question-7.ppm")
        print('# Question 7: voir fichier "question-7.ppm"')

    # Question 8
    if n == 8:
        # Définition de prédicats à partir des fonction ``dansCercle`` et
        # ``dansRectangle``
        def predicatCercle1 (x,y):
            return dansCercle(x,y, 200,125, 95)

        def predicatCercle2 (x,y):
            return dansCercle(x,y, 30,150, 150)
        def predicatRectangle1 (x,y):
            return dansRectangle(x,y, 280, 30, 80, 200)

        im = Image(image2)
        repeindreSi(im, couleurs, predicatCercle1)
        im.save("question-8a.ppm")
        print('# Question 8: voir fichier "question-8a.ppm"')

        im = Image(image1)
        repeindreSi(im, couleurs, predicatCercle2)
        l = genKgris(16)
        repeindreSi(im, l, predicatRectangle1)
        im.save("question-8b.ppm")
        print('# Question 8: voir fichier "question-8b.ppm"')

    # Question 9
    if n == 9:
        im = Image(image3)
        faireNBandes(im, 3)
        im.save("question-9a.ppm")
        print('# Question 9: voir fichier "question-9a.ppm"')

        im = Image(image3)
        faireNBandes(im, 10)
        im.save("question-9b.ppm")
        print('# Question 9: voir fichier "question-9b.ppm"')


if __name__ == '__main__':
    # On vérifie que vous êtes capable de suivre des instruction simple
    import sys
    import os.path
    if os.path.basename(sys.argv[0]) == "tp1-rantanplan.py":
        raise AssertionError("""
+-------------------------------------------------------+
| ERREUR: vous n'avez pas renommé le fichier !!         |
|         Fermez vite l'éditeur et renommez-le          |
|         avant que l'intervenant ne s'en rende compte. |
+-------------------------------------------------------+""")
    # On teste le TP !
    # testTP1(1)      # pour tester la question 1
    # testTP1(2)      # pour tester la question 2
    # testTP1(3)
    # testTP1(4)
    # testTP1(5)
    # testTP1(6)
    # testTP1(7)
    # testTP1(8)
    # testTP1(9)

