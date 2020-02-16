#########################################
### Info201, TP3 : démineur en Python ###

import random
from tkinter import *
from tkinter import messagebox

__author__ = "Simon LÉONARD"
__email__  = "simon.leonard@etu.univ-smb.fr"

##### Questions Préliminaires ###########

# Question 1
#

def affiche(n):
    if n>0:
        print(n)
        affiche(n-1)
# Q1: Il ne se passe rien, car la condition revoie false pour un nomre négatif


# Question 2
#

def fonction_mystere(l):
    if l == "":
        return 0
    else:
        c = l[0]
        if c == 'a':
            resultat = 1
        else:
            resultat = 0
        s = l[1:] # on prend la sous-chaine sans le premier caractère
        resultat = resultat + fonction_mystere(s) # appel récursif
        return resultat
# Q2: Compte le nombre de 'a'



##################
### Plateau de jeu
### Le plateau est simplement représenté par une matrice (un tableau de
### tableaux).
### La case de coordonnées "(i,j)" est un dictionnaire à deux champs :
###   - "mine" qui est un booléen et qui indique si la case contient une mine
###   - "etat" qui indique l'état de la case :
###        - INCONNU quand le joueur n'a pas découvert la case
###        - un entier entre 0 et 8 qui indique le nombre de mines voisines,
###          quand le joueur a découvert la case
###        - DRAPEAU quand le joueur a mis un drapeau sur la case
###        - QUESTION quand le joueur n'est pas sûr.
###        - PERDU quand il s'agit d'une case avec une mine, sur laquelle le
###          joueur a cliqué
### Les 13 états possibles sont modélisés par des entiers, avec les
### déclarations suivantes :
INCONNU = -1
PERDU = -2
DRAPEAU = -3
QUESTION = -4


### QUESTION : à modifier
def genere_plateau(largeur, hauteur, probabilite_mine=0.25):
    """Génère un plateau de jeu de taille donnée."""
    plateau = []
    for i in range(hauteur):
        ligne = []
        for j in range(largeur):
            ligne.append({"mine": False if random.random() > probabilite_mine else True,
                          "etat": INCONNU})
        plateau.append(ligne)
    return(plateau)


### QUESTION : écrire les trois fonctions suivantes

def dans_plateau(plateau, i, j):
    """Teste si une case est sur le plateau."""
    hauteur = len(plateau)
    largeur = len(plateau[0])
    return 0 <= i < hauteur and 0 <= j < largeur


def cases_voisines(plateau, i, j):
    """Donne la liste des coordonnées (tableaux de 2 entiers) des cases
    voisines de la case "(i,j)".
    """
    cases = []
    for plus_i in [-1,0,1]:
        for plus_j in [-1,0,1]:
            if dans_plateau(plateau, i + plus_i, j + plus_j) and (plus_i,plus_j) != (0,0): # seconde partie pour éviter de renvoyer (i,j)
                cases.append((i + plus_i, j + plus_j))
    return cases


def compte_mines_voisines(plateau, i, j):
    """Compte le nombre de mines voisines de la case "(i,j)" sur le plateau
    "plateau".
    """
    mines = 0
    for x,y in cases_voisines(plateau, i, j):
        if plateau[x][y]['mine']:
            mines += 1
    return mines


### QUESTION : écrire la procédure récursive suivante
def composante_connexe(plateau, i, j):
    """Met le plateau à jour en ouvrant toutes les cases vides à partir de la
    case "(i,j)".
    Attention, c'est une procédure...
    """
    case = plateau[i][j]
    if case['etat'] == INCONNU:
        case['etat'] = compte_mines_voisines(plateau, i, j)
        if case['etat'] == 0:
            for x,y in cases_voisines(plateau, i, j):
                composante_connexe(plateau,x,y)

def clic_droit(clic):
    j = clic.x // (largeur_case+1)  # x et y contiennent les
    i = clic.y // (hauteur_case+1)  # coordonnées de la case
    if not dans_plateau(plateau_courant, i, j) or perdu(plateau_courant) or gagne(plateau_courant):
        return
    case = plateau_courant[i][j]
    if case['etat'] in (INCONNU,DRAPEAU,QUESTION):
        if case['etat'] == INCONNU:
            r = DRAPEAU
        elif case['etat'] == DRAPEAU:
            r = QUESTION
        else:
            r = INCONNU
        case['etat'] = r
    dessine_plateau(plateau_courant)

    # NOTE : On ne peut perdre qu'avec un clic gauche et gagné qu'avec un clic droit
    if gagne(plateau_courant):
        messagebox.showinfo("Winner", "Vous avez gagné !")

### QUESTION : écrire la fonction suivante
def perdu(plateau):
    """renvoie True lorsque que le plateau contient une case découverte avec une mine"""
    for ligne in plateau_courant:
        for case in ligne:
            if case['etat'] == PERDU:
                return True
    return False


### QUESTION : écrire la fonction suivante
def gagne(plateau):
    """renvoie True lorsque que le plateau contient les drapeaux exactement
    sur les cases minées"""
    g = True
    for ligne in plateau_courant:
        for case in ligne:
            if case['mine'] and case['etat'] != DRAPEAU or case['etat'] == DRAPEAU and not case['mine']:
                g = False
    return g


###############################
###############################

def decouvre_case(plateau, i, j):
    """Découvre une case sur le plateau. Le plateau est mis à jours en
    découvrant toute la composante connexe de la case "(i,j)", et la fonction
    renvoie un booléen pour dire si la case "(i,j)" était une mine ou pas.
    Attention, c'est à la fois une procédure (modification de l'argument "plateau"
    et une fonction (qui renvoie un booléen).
    """
    if plateau[i][j]["mine"]:
        plateau[i][j]["etat"] = PERDU
        #print("OUPS... La case ({},{}) contenait une mine !".format(i,j))
        return False
    composante_connexe(plateau, i, j)
    return True


def compte_mines_solution(plateau):
    """Met le plateau à jour en comptant le nombre de mines partout.
    Attention, ceci est une procédure.
    """
    largeur = len(plateau[0])
    hauteur = len(plateau)
    for i in range(hauteur):
        for j in range(largeur):
            if plateau[i][j]["etat"] == INCONNU and not plateau[i][j]["mine"]:
                plateau[i][j]["etat"] = compte_mines_voisines(plateau, i, j)


#######################################
### Fonctions d'affichage sur la grille
### La fonction "dessine_case" utilise une constante globale (définie plus
### bas) "grille" qui représente la grille.
### Cette grille est un objet de type "Canvas" et a des méthodes de dessin
### comme "create_rectangle" et autre

def dessine_case(plateau, i, j, solution=False):
    """Dessine la case "(i,j)" sur le plateau.
    Si "solution" est vraie, dessine aussi les mines qui sont dans des cases
    fermées.
    """
    x1 = j*(largeur_case+1)+2
    y1 = i*(hauteur_case+1)+2
    x2 = (j+1)*(largeur_case+1)
    y2 = (i+1)*(hauteur_case+1)
    etat = plateau[i][j]["etat"]
    if etat == 0:
        grille.create_rectangle(x1, y1, x2, y2,
                                outline='#c0c0c0', fill='#c0c0c0')
    elif 0 < etat < 9:
        grille.create_rectangle(x1, y1, x2, y2,
                                outline='#c0c0c0', fill='#c0c0c0')
        x1 = x1 + largeur_case//2
        y1 = y1 + hauteur_case//2
        grille.create_text(x1, y1, justify=CENTER, text=str(etat))
    elif etat == DRAPEAU:
        if not plateau[i][j]['mine'] and solution:
            grille.create_image(x1,y1, image=mauvais_drapeau_img, anchor=NW)
        else:
            grille.create_image(x1, y1, image=drapeau_img, anchor=NW)
    elif etat == QUESTION:
        grille.create_image(x1, y1, image=question_img, anchor=NW)
    elif etat == INCONNU:
        if plateau[i][j]["mine"] and solution:
            grille.create_image(x1, y1, image=mine_img, anchor=NW)
        else:
            grille.create_image(x1, y1, image=inconnu_img, anchor=NW)
    elif etat == PERDU:
        grille.create_image(x1, y1, image=perdu_img, anchor=NW)
    else:
        assert(False)


def dessine_plateau(plateau, solution=False):
    largeur = len(plateau[0])
    hauteur = len(plateau)
    grille.delete(ALL)
    for i in range(hauteur):
        for j in range(largeur):
            dessine_case(plateau, i, j, solution)


#######################################
### Fonctions pour gérer les évènements
### Dans ces fonctions,
###    - "plateau" est une variable globale qui contient le plateau courant,
###    - "grille" est une constante globale qui contient la fenêtre.
###

def __action_clic(clic):
    """Fonction appelée quand on fait un clic sur la fenêtre."""
    # clic.x et clic.y contiennent les coordonnées, en pixel,
    # du clic à l'intérieur de la fenêtre
    j = clic.x // (largeur_case+1)  # x et y contiennent les
    i = clic.y // (hauteur_case+1)  # coordonnées de la case
    if not dans_plateau(plateau_courant, i, j) or perdu(plateau_courant) or gagne(plateau_courant):
        return
    if plateau_courant[i][j]["etat"] != INCONNU:
        return

    ok = decouvre_case(plateau_courant, i, j)
    dessine_plateau(plateau_courant)

    if not ok:
        messagebox.showinfo("Looser", "Vous avez perdu")
    # NOTE : On ne peut perdre qu'avec un clic gauche et gagné qu'avec un clic droit



def __action_m(e):
    """Permet d'afficher la solution pendant 1 seconde."""
    import copy
    from time import sleep
    p = copy.deepcopy(plateau_courant)
    compte_mines_solution(p)
    dessine_plateau(p, True)
    grille.update_idletasks()
    sleep(1)
    dessine_plateau(plateau_courant)


def __action_q(e):
    """Permet de quitter le jeux."""
    root.destroy()


###############################################################
### initialisation de la fenêtre, et autres constantes globales
###

# quelques variables globales, modifiable par l'utilisateur
largeur = 15                # largeur du plateau, en nombre de cases
hauteur = 20               # hauteur du plateau, en nombre de cases
probabilite_mine = 0.15     # probabilité qu'une case contienne une mine

# fenêtre principale
root = Tk()
root.title("Démineur")
root.resizable(width=False, height=False)
Label(text="Info201 : démineur en Python").pack()

# les images utilisées pour les cases spéciales
#
# Vous pouvez supprimer les déclarations contenant data='...' et les remplacer
# par les lignes contenant file='...'
# Bien sûr, il faut disposer des fichiers images correspondants...
# Attention, si vous modifiez les fichiers images, il faut que toutes les
# images aient la même taille (15x15 pixels pour les images par défaut).
#
# Remarque : les données "data" sont obtenues par codage en base64 des
# fichiers binaires :
# import base64
# data = base64.b64encode(open("inconnu.gif", mode="rb").read())
#

#inconnu_img = PhotoImage(file="inconnu.gif")
inconnu_img = PhotoImage(data='R0lGODdhDwAPAKUvAG1tbX5+foGBgYODg4SEhIWFhZycnK'
                              'GhoaioqKmpqaurq6ysrK2srKytrKytra2trbS0tLm5ub6+'
                              'vr+/v87PztbW1tjY2NnZ2dva2tvb29vb3Nzb29zb3Nvc29'
                              'zc29zc3N3c3enp6e3t7e7u7vDw7/Ly8vX19fX19vb19vX2'
                              '9fX29vb29fb29vf39/j4+P////////////////////////'
                              '///////////////////////////////////////////ywA'
                              'AAAADwAPAAAGXMBNqaU6sVioVeroMiFClIplSqVeIIERRj'
                              'Lper2SxED0+Zq7i3HnbE6LMuyvmxP3usv1iVuT1489fXeB'
                              'Y3R5aSMgfQoEJBEJDgwPDw0LDpILBgQHAgSdnp8FBQBBAD'
                              's=')

#question_img = PhotoImage(file="question.gif")
question_img = PhotoImage(data='R0lGODdhDwAPAMZpAAAA/wEB/wYG/RMT+Bsb9iMj8y4u7'
                               'y4u8EJC6VFR5FlZ4Vxc4F1d4GBg32pqamJi3m1t2nx8e3'
                               'l51oCAgIGAgYCBgIODg4SEhIWFhYGB1IOD04SE04mJ0Yq'
                               'K0ZeYl5ycnJ6eyqKioqKiyaamx6mpqaenx6usq6ysrKqq'
                               'xq2srK2sraytrK2trK2trbCwq66uxbCwrLCwxLKyxLS0t'
                               'bS0w7W1wri4uLi4wbq6wLu7wby8wL6+vr6+v76+wL+/v8'
                               'C/v8DAv8HBv8LCvsPDvcPDvsTEvcXFvcjIvMjIvcrKu8z'
                               'Mu87OutDQ0NHR0dbW1tjY2NnY2NnZ19nZ2dra19vb19rb'
                               '29zc3N3c3dzd3N3d3N3d3d3e3d/f3+Pj4+Tk5OXl5fT09'
                               'PX19fX19vb19vX29fb29fb29vf39/j4+P////////////'
                               '/////////////////////////////////////////////'
                               '//////////////////////////////////ywAAAAADwAP'
                               'AAAHxYBNYGdmYmZmY2Vkh2hhIVxMTk9PUVNUU1CTUjMRX'
                               'lU7PERFODc8R0A+OyQTXVo+QyMIBAMGEkKoLKxXPkcbAQ'
                               'cFAAAdSD4nrK5CKCJEPgcAD0o+KaxYPj5CRksvBAAcxcd'
                               'd1j5APBAEAg23PiusVtdCNcIZSUHX7V1Z10E5CwkxQ675'
                               'aOEOngwGCkAUERjOlY8iJQQA0HCE4QQvW3b4+NGDBg0dq'
                               'K6ZoPDFBokWKVjAcMFCBYsWJz5U8GDhgs2bODFgcBAIAD'
                               's=')

#mine_img = PhotoImage(file="mine.gif")
mine_img = PhotoImage(data='R0lGODdhDwAPAMZQAAAAAAMDAwYGBhYWFhoaGhwcHB4eHiMjI'
                           'yQkIyYmJicnJygoKCoqKisrKy0tLS8vLzAwMDIyMzMzMzQ0ND'
                           'k5OUhIR1VVVVZWVl5eXl9fX2VlZWZmZmdnZ2hnZ2pqamtra3F'
                           'xcXR0dHZ2dnd3d3d3eH9/f4GAgIGBgYKCgoeHh4iIiI+Pj5OT'
                           'k6KioqOjo6SkpKampqenp6qqqqurq6+ur6+wsLKysrOzs7S0t'
                           'LW1tbe3t7i4uLm5ubq6uru7u7y8vL29vb6+vr+/v8DAwMHBwc'
                           'LCwsPDw8TExMXFxcbGxs7Ozs/Pz9HR0dPT09TU1PDw8P/////'
                           '/////////////////////////////////////////////////'
                           '/////////////////////////////////////////////////'
                           '/////////////////////////////////////////////////'
                           '///////////////////////////////////////ywAAAAADwA'
                           'PAAAHvIA+REOEhEWFhEQ+gohDPEKIRD2MSElGOxIzR0lJQ5KC'
                           'SCElSjUDLU4rHkZFk0RJKQYiHQ4PGgYhSayCRUsjHjQqDQAWT'
                           'EefRDs2Gy5PORUADDg7Qz1BPRMGCCQyJg4AAAYMNkA+QzMxEQ'
                           'UUCQIACzAyQq1HThzf9xhOxq1ILAcXDAIoyGDgBJJjSD6AYHK'
                           'DwIsmKDCsajXECJIjOyDMqGTEU48fRYgUCUmEhyeRIn3oAPKj'
                           'ZUshLlsC0REIADs=')

#drapeau_img = PhotoImage(file="drapeau.gif")
drapeau_img = PhotoImage(data='R0lGODdhDwAPAMZxAAAAAAUFBQYGBhERERYaGhoaGikWFo'
                              'MAAJEAAHwGBn4HB34ICIIHB9cAAOQAANQHB/8AAP4DA/wJ'
                              'CfsSEl5eXmBgYNdCQuo+PmNjY+4+PmZmZudGRmpqan19fI'
                              'GBgYKBgoKCgoODg4SEhIWFhZaWlpiYmJuam6qXl5ycnKOj'
                              'o7KiorWjo7ajo7WlpampqKmpqcikpKusrKysrK2srK6srK'
                              'ytrK2trK2trbqsrLCwsLGxsbKysrOzs7S0tbK2tsOysra2'
                              'tsOzs7i4uMK2trm5ubu7u8C9vb6+vr+/v7/AwMDAwL7Bwc'
                              'HBwb7Cwr/CwsHCwsLCwr3ExMPDw8DExMHExMTHx8vLy9LS'
                              '0tbW1tjY2NjY2dfZ2dfZ2tjZ2dnZ2dvb293d3d7d3d3e3t'
                              '7e3uLi4eXl5ebm5ujo6PPz8/X19fb19vX29fX29vb29fb2'
                              '9vf39/j4+P////////////////////////////////////'
                              '///////////////////////ywAAAAADwAPAAAHv4BXaG9u'
                              'bG5uam1rh3BpKWRXWFlcXVuWWllZXj0dZl9HSE2iTU9KSE'
                              'hHLx5lYktDGxcXGRY4Tqc2q2BNPxEQEA4IKlSnMrlNQRIQ'
                              'DQcKK8NIM8ZBEw8MCQvOxLlJRjAsLScGNFKnNbmnUVNVPg'
                              'Q35EjmZWCnp1BABTrvN+f1ViUDJawwQVKsTJhTTHhQCABA'
                              'AIciTIqZGQMKCokKGDRgwJACSowPZ4q4uCFjB5GTRITkkI'
                              'EChIkQImLKnDliBIdAADs=')

#mauvais_drapeau_img = PhotoImage(file="mauvais_drapeau.gif")
mauvais_drapeau_img = PhotoImage(data='R0lGODdhDwAPAMZdAP8AAP4BAf4CAv8CAvUdHf'
                                      'UfH/AtLfAuLulDQ+hEROdGRudHR2pqauNSUuNT'
                                      'U+JVVeJWVuJXV3x8e95jY91mZoCAgN1nZ4GAgY'
                                      'CBgISEhIWFhdSBgdSCgpycnM6RkaKioqCkpKmp'
                                      'qausq6ysrKysra2srK2sraytrK2trK2trbS0tb'
                                      'a2tsO0tMG4uMK4uMC7u7+8vMC8vMC9vb6+vr++'
                                      'vsC+vr+/v77AwL/AwL7Bwb/Bwb3Cwr7Cwr7Dw7'
                                      '3ExL7ExL3FxbzGxr3GxrzHx7zIyM7OztbW1tjY'
                                      '2NnZ2dra2tva2trb2tvb29vf3+js7ezw8ezx8O'
                                      'zx8e3y8u7y8vLy8vX19fX19vb19vX29fb29fb2'
                                      '9vf39/j4+P////////////////////////////'
                                      '//////////////////////////////////////'
                                      '//////////////////////////////////////'
                                      '///////////////////////////////////ywA'
                                      'AAAADwAPAAAHyoBNVFtaVlpaV1lYh1xVH05FRk'
                                      'eTlJRIKhJSRzM4QTk2oJ04MyEVT0s2MB4vOzQ5'
                                      'Nx4tOCgVUUlCHgANQD5EEwAcRCe1SjkxDgAPQh'
                                      'QACS45JaZJNjxADwAHAQs5PjYj0qBAQgYABDRD'
                                      'NDbDUNM5RBYCBQMRQDzq0jg3vwoyEAAONXSkkB'
                                      'YkF4IcQ4Ag20CERAV2OlpwcPHDRo8aHFjo+CaF'
                                      'CQ0dRD6BAqmDhogLU1aESFGiRIoTI0ygSDGiAw'
                                      'YQFzLo3MlTgwYGgQAAOw==')

#perdu_img = PhotoImage(file="perdu.gif")
perdu_img = PhotoImage(data='R0lGODdhDwAPAMZZAAAAAAABAQcBAQMDAx4AACAAACIAACYA'
                            'ACMBASUBAScBASsBATMAADsAAD0AAD4DAz8EBFAAAEcDA0sC'
                            'AioNDWoCAhQbG3ECAnsAAHYDA4ECAooAAIUDAx8fHx4gIJcA'
                            'AJgAAI4DA6kAAKoAAKwAACYmJroAALwAANIAANkAADAvMNwB'
                            'ASsxMeIAAN8BAeQAAOUAAOoAAOsAAOsBAfAAAPMAAPQAAPIB'
                            'AfcAADM2N/wAAP4AAP8AAP8BAZYeHvcEA/UFBfUFBoAlJPgF'
                            'BfUGBfYGBvkGBfYHB/oHB/cICPgICPoICO8ODmE4OENDQmtL'
                            'S29wb3d4d2yHiJGRkZ6enqGpqbOzs7nAwO7u7v//////////'
                            '////////////////////////////////////////////////'
                            '////////////////////////////////////////////////'
                            '////////////////////////////////////////////////'
                            '/ywAAAAADwAPAAAHnYBHPIOEhYRFgoU7MjqGQYmENQwthkCJ'
                            'GyA8LQQoPCMYOzxEiSYHQk85FBUKIoOWhD5SV1MsABc9rkc7'
                            'LylNVVhWTgALKy87REg4DgYeUFRRJQABBg04Rro0MRAWKh0D'
                            'AA8zNDuPhBoA6NIZhKODJAgcEwISIQmZookfJDw3BS48JzaE'
                            'KlfIRgQYjoYY4tHI0A8mSSJKXKJEYkQmgQAAOw==')


# on vérifie que les images ont toute les même dimensions
assert (mine_img.height() == perdu_img.height()
                          == drapeau_img.height()
                          == mauvais_drapeau_img.height()
                          == question_img.height()
                          == inconnu_img.height())
assert (mine_img.width() == perdu_img.width()
                         == drapeau_img.width()
                         == mauvais_drapeau_img.width()
                         == question_img.width()
                         == inconnu_img.width())
largeur_case = mine_img.width()
hauteur_case = mine_img.height()


# la grille : un objet de type "Canvas" pour pouvoir dessiner dedans.
grille = Canvas(root, width=largeur*(largeur_case+1)+1,
                height=hauteur*(hauteur_case+1)+1,
                bg="#7f7f7f")
grille.pack()

# les évènements à gérer
root.bind("q", __action_q)
root.bind("m", __action_m)
grille.bind("<Button-1>", __action_clic)
grille.bind("<Button-3>", clic_droit)


# création du plateau, et début du programme...
plateau_courant = genere_plateau(largeur, hauteur, probabilite_mine)
dessine_plateau(plateau_courant)
grille.mainloop()


### Fin du fichier ###
######################
