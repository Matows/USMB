##############################################
### INFO201 : algorithmes et programmation
###
### Fichier nécessaire pour le TP1
###

def syracuse(n):
    """Procédure affichant la suite de syracuse avec comme premier nombre _n_"""
    while n > 1:
        if n % 2 == 0: # Pair
            n /= 2
        else:
            n = n*3 + 1
        print(n)

def strategie_dicho():
    """implémentation de la stratégie naïve qui cherche un nombre entre
    et 100 choisi par l'utilisateur.
    """

    print("Pense à un nombre entre 0 et 100 puis appuie sur 'Enter'...")
    input()

    trouve = False  # variable qui passe à vrai quand on a trouvé le nombre
    nb_questions = 0

    inf = 0
    sup = 100

    while not trouve:
        milieu = (inf+sup)//2

        # on demande si le nombre est égal à nb :
        question = "Le nombre est-il inférieur/égal à %i ? (o/n) : " % milieu

        reponse = ""
        while reponse.lower() not in ["o", "n"]: # On attend une réponse valide
            reponse = input(question)

        if reponse == "o":
            sup = milieu

        elif reponse == "n":
            inf = milieu + 1

        if sup == inf: # Plus que une possibilité
            trouve = True

        nb_questions = nb_questions+1

    print("Ton nombre est égal à", inf,
          "et il m'a fallu", nb_questions, "questions pour le trouver.")

# Il faut 7 questions pour [0;100]
# Il faut 10 questions pour [0;1000]
# Il faut 14 questions pour [0;10000]

##############################################
### bibliothèques utilisées
from tkinter import *
from math import sin, cos, pi, sqrt, radians, degrees
import random

#############################################
### fonctions et procédures


###
# La fonction à écrire pour la question 2
def trajectoire_boulet(angle, masse, vitesse, dt=1, freq=100, display=True):
    """Cette fonction doit calculer des positions de la trajectoire d'un
    boulet de canon. Les arguments sont les suivants :
    - angle : angle, en degré, du canon par rapport à l'horizontal
    - masse : masse, en kilogrammes, du boulet de canon
    - vitesse : vitesse initiale, en mètres par seconde, du boulet de canon
    - dt : intervalle de temps utilisé pour les calculs (en secondes),
    - freq : fréquence des positions à afficher ; par défaut, on affiche
      qu'une position sur 100... Si freq <= 0, on affiche rien
La fonction retourne la valeur de x lorsque le boulet touche le sol.
"""
    x, y = 0, 0
    G = 9.81
    A = 0.003256 / masse

    vx = vitesse * cos(angle*pi/180)
    vy = vitesse * sin(angle*pi/180)

    cpt = 0
    while y >= 0:
        x += vx * dt
        y += vy * dt

        v = sqrt(vx*vx + vy*vy)
        vx -= A*vx*v*dt
        vy -= (G + A*vy*v)*dt

        cpt += 1
        if cpt % freq == 0 and display:
            dessine_boulet(x,y)

    return x


###
# La fonction à écrire pour la question 3
def dichotomie(cible, masse, vitesse, dt, freq):
    """Cette fonction doit calculer l'angle approprié pour envoyer un boulet
sur une cible donnée :
    - cible : distance entre le canon et la cible, en mètres
    - masse : masse du boulet de canon,
    - vitesse : vitesse initiale du boulet canon, en mètre / seconde
    - dt : intervalle de temps  utilisé pour les calculs (en secondes),
    - freq : fréquence des positions à afficher lors des appels à la fonction
      trajectoire_boulet.
La fonction renvoie la valeur de l'angle trouvé...
"""
    angle_inf = 45
    angle_sup = 90
    angle_milieu = -1

    # Longueur maximum atteignable
    point_impact = trajectoire_boulet(angle_inf, masse, vitesse, dt, freq)
    
    if point_impact >= cible: # On ne cherche que si s'est atteignable 
        trouve = False
        while not trouve:
            angle_milieu = (angle_inf + angle_sup)/2

            point_impact = trajectoire_boulet(angle_milieu, masse, vitesse, dt, freq)

            
            if cible-1 <= point_impact <= cible+1:
                trouve = True
            
            elif point_impact < cible:
                angle_sup = angle_milieu

            elif point_impact > cible:
                angle_inf = angle_milieu

    return angle_milieu

def distance_max(masse, vitesse, dt, freq):
    """Cette fonction doit calculer l'angle approprié pour envoyer un boulet
    le plus loin possible.
        - masse : masse du boulet de canon,
        - vitesse : vitesse initiale du boulet canon, en mètre / seconde
        - dt : intervalle de temps  utilisé pour les calculs (en secondes),
        - freq : fréquence des positions à afficher lors des appels à la fonction
          trajectoire_boulet.
    La fonction renvoie la valeur de l'angle trouvé...
    """
    angle_inf  = 0
    angle_sup  = 90
    angle_opti = -1

    trouve = False
    while not trouve:
        angle1 = angle_inf + (angle_sup - angle_inf)/3 # Premier tier
        angle2 = angle_inf + 2*(angle_sup - angle_inf)/3 # Second tier

        point_impact1 = trajectoire_boulet(angle1, masse, vitesse, dt, freq)
        point_impact2 = trajectoire_boulet(angle2, masse, vitesse, dt, freq)

        # Si le premier et le second tier sont suffisament proche, on a trouvé un bon angle
        if point_impact1-0.5 <= point_impact2 >= point_impact1 + 0.5:
            trouve = True
            angle_opti = angle1

        # Sinon, on réduit la zone de recherche et on recommence
        elif point_impact1 > point_impact2:
            angle_sup = angle2

        elif point_impact2 < point_impact1:
            angle_inf = angle1


    return angle_opti


###################################################################
##  Vous n'avez pas besoin de modifier la suite du programme...  ##
###################################################################


### variable globale : angle du canon par raport à l'horizontal
angle_canon = 75            # en degrés
vitesse_initiale = 250      # vitesse du boulet, en mètre par seconde
masse_boulet = 2            # en Kg
# Rappel : si vous souhaiter modifier une variable globale à l'intérieur
# d'une fonction, il faut mettre un "global nom_variable" au début de votre
# fonction


#####
# configuration
hauteur = 600       # hauteur, en pixels, de la fenêtre
largeur = 800       # largeur, en pixels, de la fenêtre
horizon = 100       # hauteur, en pixels, de l'horizon
marge_gauche = 75   # marge, en pixels, à gauche du canon

metre_x = .4     # nombre de pixels pour faire un mètre, en horizontal
metre_y = .4     # nombre de pixels pour faire un mètre, en vertical

position_cible = None   # position de la cible au sol

images_boulet = None    # tableau des différentes images possible pour le boulet
image_boulet = None     # image courante pour le boulet (tirée aléatoirement)
image_cible = None      # image pour la cible

#####
# La fonction qui dessine un boulet en position (i,j), en mètres
def dessine_boulet(i, j):
    """dessine un boulet en position (i,j), exprimés en mètres."""
    x = marge_gauche + i*metre_x
    y = hauteur - (horizon + j*metre_y)
    if image_boulet is None:
        fenetre.create_oval(x-6, y-6, x+6, y+6, fill='black', width=0)
    else:
        fenetre.create_image(x, y, image=image_boulet, anchor="center")


#####
# récupération des paramètres
def recupere_parametres():
    # on récupère les valeurs des différents paramètres
    global angle_canon, masse_boulet, vitesse_initiale, position_cible
    try:
        a = float(boite_angle.get())
        angle_canon = a
    except:
        boite_angle.delete(0, END)
        boite_angle.insert(0, angle_canon)
    try:
        a = float(boite_masse.get())
        masse_boulet = a
    except:
        boite_masse.delete(0, END)
        boite_masse.insert(0, masse_boulet)
    try:
        a = float(boite_vitesse.get())
        vitesse_initiale = a
    except:
        boite_vitesse.delete(0, END)
        boite_vitesse.insert(0, vitesse_initiale)
    try:
        a = float(boite_cible.get())
        position_cible = a
    except:
        boite_cible.delete(0, END)
        position_cible = None
    root.focus_set()

    # on récupère aussi une nouvelle image pour le boulet...
    global image_boulet
    if images_boulet is not None:
        image_boulet = images_boulet[random.randint(0, 6)]


#####
# La fonction qui est appelée quand on appuie sur le bouton "Tirer".
# Elle appelle la fonction "trajectoire_boulet" et dessine les boulets
# correspondants.
def tirer():
    recupere_parametres()

    # on affiche toutes les positions du boulet données par la fonction
    # "trajectoire_boulet(...)
    trajectoire_boulet(angle_canon, masse_boulet, vitesse_initiale,
                       dt=0.01, freq=100)


#####
def tirer_dichotomie():
    recupere_parametres()

    # on affiche toutes les positions du boulet données par la fonction
    # "trajectoire_boulet(...)
    dessine_arriere_plan()
    if position_cible is not None:
        dichotomie(position_cible, masse_boulet, vitesse_initiale,
                   dt=0.01, freq=100)

#####
def tirer_max():
    recupere_parametres()

    # on affiche toutes les positions du boulet données par la fonction
    # "trajectoire_boulet(...)
    dessine_arriere_plan()
    distance_max(masse_boulet, vitesse_initiale,
                   dt=0.01, freq=100)

###############################################
### code principal exécuté

#####
# création de la fenêtre
root = Tk()
root.title('boulet')
root.resizable(width=False, height=False)


#####
# fenêtre de dessin
fenetre = Canvas(root, width=largeur, height=hauteur, bg='white')
fenetre.pack()


#####
# arrière plan
def dessine_arriere_plan():
    try:
        a = float(boite_cible.get())
        position_cible = a
    except:
        boite_cible.delete(0, END)
        position_cible = None

    fenetre.create_rectangle(0, 0, largeur, hauteur-horizon+1,
                             fill='blue', width=0)
    fenetre.create_rectangle(0, hauteur-horizon+1, largeur, hauteur,
                             fill='darkgreen', width=0)
    fenetre.create_oval(largeur-80, 10, largeur-10, 80, width=0, fill='yellow')
    fenetre.create_polygon(largeur-40, hauteur-horizon+1,
                           largeur-200, hauteur-horizon+1,
                           largeur-120, hauteur-horizon-120,
                           width=0, fill='gray')
    fenetre.create_polygon(largeur-120, hauteur-horizon+1,
                           largeur-260, hauteur-horizon+1,
                           largeur-190, hauteur-horizon-80,
                           width=0, fill='gray')

    # axes
    fenetre.create_line(marge_gauche, 0, marge_gauche, hauteur-horizon+1,
                        fill='darkgreen')
    for i in range(hauteur-horizon-int(100*metre_y), 1, -int(100*metre_y)):
        fenetre.create_line(marge_gauche, i, marge_gauche+5, i, fill='darkgreen')
    for i in range(marge_gauche+int(100*metre_x), largeur, int(100*metre_x)):
        fenetre.create_line(i, hauteur-horizon-5, i, hauteur-horizon+1,
                            fill='darkgreen')

    if position_cible is not None:
        if image_cible is None:
            fenetre.create_arc(marge_gauche + position_cible*metre_x - 10,
                               hauteur-horizon - 9,
                               marge_gauche + position_cible*metre_x + 10,
                               hauteur-horizon + 11,
                               start=0,
                               extent=-180,
                               outline='red',
                               fill='red')
        else:
            fenetre.create_image(marge_gauche + position_cible*metre_x,
                                 hauteur-horizon+16,
                                 image=image_cible,
                                 anchor="center")

try:
    import images
    images_boulet = []
    for s in images.data_boulets:
        images_boulet.append(PhotoImage(data=s))
    image_boulet = None
    image_cible = PhotoImage(data=images.data_cible)
except:
    images_boulet = None
    image_boulet = None
    image_cible = None

#####
# boutons

fm1 = Frame(root)
bouton_quitter = Button(fm1, text='Quitter', command=lambda: root.destroy())
bouton_quitter.pack(side=RIGHT, padx=5, pady=10)

bouton_dessine = Button(fm1, text='Effacer trajectoires',
                        command=lambda: dessine_arriere_plan())
bouton_dessine.pack(side=RIGHT, padx=5, pady=10)

Label(fm1, text="    angle (deg) :").pack(side=LEFT, padx=5, pady=10)
boite_angle = Entry(fm1, width=3)
boite_angle.pack(side=LEFT, padx=0, pady=10)
boite_angle.insert(0, angle_canon)

Label(fm1, text="    masse (kg) :").pack(side=LEFT, padx=5, pady=10)
boite_masse = Entry(fm1, width=2)
boite_masse.pack(side=LEFT, padx=0, pady=10)
boite_masse.insert(0, masse_boulet)

Label(fm1, text="    vitesse (m/s) :").pack(side=LEFT, padx=5, pady=10)
boite_vitesse = Entry(fm1, width=4)
boite_vitesse.pack(side=LEFT, padx=0, pady=10)
boite_vitesse.insert(0, vitesse_initiale)

bouton_tirer = Button(fm1,  text='Tirer',  command=tirer)
bouton_tirer.pack(side=LEFT, padx=20, pady=10)
fm1.pack()


fm2 = Frame(root)
Label(fm2, text="    cible (m) :").pack(side=LEFT,  padx=5, pady=10)
boite_cible = Entry(fm2, width=4)
boite_cible.pack(side=LEFT, padx=0, pady=10)
if position_cible is not None:
    boite_cible.insert(0, position_cible)

bouton_dichotomie = Button(fm2,  text='Atteindre cible',
                           command=tirer_dichotomie)
bouton_dichotomie.pack(side=LEFT, padx=20, pady=10)

bouton_max = Button(fm2,  text='Distance max',
                           command=tirer_max)
bouton_max.pack(side=LEFT, padx=20, pady=10)

fm2.pack()

#####
# racourcis clavier
root.bind("q", lambda _: root.destroy())
root.bind("t", lambda _: tirer())


#####
# boucle d'intéraction
dessine_arriere_plan()
root.mainloop()


### fin du fichier
######################
