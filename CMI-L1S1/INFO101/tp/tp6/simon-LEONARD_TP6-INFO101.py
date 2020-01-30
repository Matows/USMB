#!/usr/bin/env python3
# coding: utf-8

### QUESTION 2
# [0,1,2,3] -> 3X^3 + 2X^2 + X
# [1,2,3] -> 3X^2 + 2X + 1
# [3,2,1] -> X^2 + 2X + 3
# [3,2,1,0] -> X^2 + 2X + 3
# X^2 + 2 -> [2,0,1]
# 2 + 2X + 2X^2 + 2X^3 -> [2,2,2,2]
# X^10 + X^20 -> [0]*10 + [1] + [0]*9 + [1]

def clear_poly(poly):
    """Enlève les puissance innutile du polynôme _poly_ (les 0 à droite du tableau)"""
    poly = poly[::-1]
    for value in poly:
        if value == 0:
            poly.remove(0)
        else:
            break
    return poly[::-1]


### QUESTION 3
def degre(poly):
    """Renvoie le degré du polynôme _poly_"""
    poly = clear_poly(poly)
    return len(poly)-1


### QUESTION 4
def calcule_polynome(poly, x):
    """Calcule le polynôme _poly_ pour la valeur de _x_"""
    return sum([coef*x**i for i,coef in enumerate(poly)])


### QUESTION 7
# >>> affiche_age("Louis Pasteur", 1822)
# 197


### QUESTION 9
def multiplication_scalaire(poly, nb):
    """Multiplie chanque coeficient du polynôme _poly_ par _nb_"""
    return [coef*nb for coef in poly]


### QUESTION 10
# oppose est une fonction à un seul paramètre (une liste) et renvoie une liste
def oppose(poly):
    """renvoie l'opposé du polynôme _poly_ (i.e. l'opposé de chaque coeficient)"""
    return [-coef for coef in poly]


### QUESTION 11
def symetrique(poly):
    """Renvoie le polynôme symétrique du polynôme _poly_"""
    return [-coef if i % 2 == 1 else coef for i,coef in enumerate(poly)]


### QUESTION 12
# somme_poly doit avoir deux paramètres (des liste) et renvoie une liste
def somme_poly(poly1, poly2):
    """Renvoie la somme des polynômes _poly1_ et _poly2_"""

    len_max = max(len(poly1),len(poly2))
    poly1 = poly1 + [0] * (len_max - len(poly1))
    poly2 = poly2 + [0] * (len_max - len(poly2))

    return [coef1+coef2 for coef1,coef2 in zip(poly1,poly2)]


### QUESTION 13
def derive_poly(poly):
    """Renvoie la dérivé du polynome _poly_"""
    poly = clear_poly(poly)
    # On décale tout les éléments de 1 vers la gauche
    poly.pop(0)

    return [coef*(i+1) for i,coef in enumerate(poly)]


### QUESTION 14
def chaine_polynome(poly):
    """Renvoie la représentation dy polynôme _poly_ (version simple)"""
    tab_str = [str(coef) + "*X^" + str(i) if i != 0 else str(coef) for i,coef in enumerate(poly)]
    return " + ".join(tab_str[::-1])


### QUESTION 15
def chaine_polynome(poly):
    """Renvoie la représentation du polynôme _poly_ (version avancée)"""
    tab_str = []
    for i,coef in enumerate(poly):
        # monome composé de : signe + coef, "*X^", puissance
        monome = ["", "*X^", ""]

        # Le coef
        if coef in (-1,1): # On ne veut pas afficher le coef
            if i != 0:
                monome[1] = monome[1][1:] # On enlève le signe multiplié
                monome[0] = "-" if coef == -1 else "" # Mais on garde le bon signe
            else:
                monome[0] = str(coef) # Par contre si c'est la constante il faut la garder
        elif coef == 0: # On ne veut pas l'afficher
            monome = ["", "", ""]
            continue
        else: # Dans le cas classique, on converti juste
            monome[0] = str(coef)

        # La puissance
        if i == 0: # On n'affiche pas X^0
            monome[1] = ""
        elif i == 1: # On n'affiche pas ^1
            monome[1] = monome[1][:-1]
        else: # On affiche tout
            monome[2] = str(i)

        tab_str.append("".join(monome))

    # J'aurai pu faire plus simple, mais c'était pour m'amuser
    return join(tab_str[::-1], \
                lambda x: " - " if x.startswith("-") else " + ", \
                lambda x: x[1:] if x.startswith("-") else x)

def join(liste, relier, transforme):
    """Join les éléments de liste avec le signe retourner par func(élément) et
        modifiant chaque élément de la liste avec transforme(élément).
    """
    chaine = str(liste[0])
    liste.pop(0)
    for elem in liste:
        chaine += relier(elem) + transforme(elem)
    return chaine


### QUESTION 16
def multiplication_polynomes(poly1, poly2):
    """Renvoie la multiplication de deux polynômes _poly1_ et _poly2_"""
    poly1, poly2 = clear_poly(poly1), clear_poly(poly2)
    result=[  [0] * (degre(poly1)+degre(poly2) + 1)  for _ in range(len(poly1))] # init tableau des résultats
    # On calcul successivement la multiplication d'un monome de poly1 avec tout poly2
    for i,coef1 in enumerate(poly1):
        for j,coef2 in enumerate(poly2):
            result[i][i+j] = coef1*coef2
    # Puis on somme tout les polynômes de result
    result_final = result[0]
    for i in range(1, len(result)):
        result_final = somme_poly(result_final, result[i])
    return result_final


### QUESTION 17
def puissance(poly, n):
    """Renvoie le polynôme _poly_ à la puissance _n_"""
    if n == 0: return [1]
    poly = clear_poly(poly)
    result = poly.copy()
    for i in range(n-1):
        result = mult_poly(result,poly)
    return result

def composition(poly1, poly2):
    """Renvoie le polynome "composé" poly1(poly2)"""
    poly1, poly2 = clear_poly(poly1), clear_poly(poly2)
    result = [[]]*len(poly1)
    for i,coef in enumerate(poly1):
        result[i] = multiplication_scalaire(puissance(poly2,i),coef)

    result_final = result[0]
    for i in range(1, len(result)):
        result_final = somme_poly(result_final, result[i])
    return result_final


########################################################################
### affichage graphique d'un polynôme
from tkinter import *
def graphe_polynome(x_min, x_max, *polynomes,
           largeur=600, hauteur=400):
    """affiche le graphe de polynômes passés en argument,
entre x_min et x_max"""

    if "calcule_polynome" not in globals():
        print("*** La fonction 'calcule_polynome(P, x)' n'est pas définie !")
        print("*** abandon")
        return

    if len(polynomes) == 0:
        print("Il faut donner au moins un polynôme à tracer !")
        print("*** abandon")
        return

    xs = [ x_min+(x*(x_max-x_min))/(largeur-1) for x in range(largeur) ]

    tmp = [ [calcule_polynome(p,x) for x in xs] for p in polynomes ]

    y_min = min(map(min,tmp))
    y_max = max(map(max,tmp))
    if y_min == y_max:
        y_min -= 1
        y_max += 1

    lines = []
    for ys in tmp:
        line = []
        for i in range(largeur):
            y = ys[i]
            y_pixel = int(((hauteur-1)*(y-y_min))/(y_max-y_min))
            line.extend((i, hauteur-1-y_pixel))
        lines.append(line)

    root = Tk()
    root.title("graphes de polynômes")
    root.resizable(width=False, height=False)
    root.bind("q", lambda _: root.destroy())
    graphe = Canvas(root, width=largeur, height=hauteur)
    graphe.pack()

    print("affichage des polynomes entre x={} et x={}".format(x_min, x_max))
    print("les valeurs varient  entre y={} et y={}".format(y_min, y_max))
    # les axes
    if x_min*x_max<0:
        x0 = int(((largeur-1)*(-x_min))/(x_max-x_min))
        graphe.create_line(x0,0, x0,hauteur-1)
    if y_min*y_max<0:
        y0 = hauteur-1-int(((hauteur-1)*(-y_min))/(y_max-y_min))
        graphe.create_line(0,y0, largeur-1,y0)

    # les polynômes
    couleurs = [("red", "rouge"), ("green", "vert"), ("blue", "bleu"),
                ("magenta", "magenta"), ("cyan", "cyan"), ("grey", "gris"),
                ("orange", "orange"), ("dark violet", "violet"),
                ("brown", "marron"), ("black", "noir")]
    for i in range(len(polynomes)):
        line = lines[i]
        p = polynomes[i]
        c = couleurs[0]
        graphe.create_line(*line, fill=c[0], width=2, smooth=True)
        if "chaine_polynome" in globals():
            print("   {:<7} : {}".format(c[1], chaine_polynome(p),  ":", c[1]))
        couleurs = couleurs[1:]+couleurs[0:1]

    print("Appuyez sur la touche 'q' pour quitter la fenêtre graphique.")
    root.mainloop()
