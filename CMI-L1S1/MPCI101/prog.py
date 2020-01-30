from tkinter import *


def format(data: list,largeur: int,hauteur: int) -> list:
    xpas = largeur/len(data)

    ymax = max(data)
    ymin = min(data)

    distance = ymax-ymin
    ypas = hauteur/distance

    values = []
    for i, value in enumerate(data):
        values.append(i*xpas)
        values.append(value*ypas - distance/2)
    return values

def main(data,largeur,hauteur):
    """initialisation d'une fenêtre avec tkinter"""
    # creation de l'objet fenêtre en python
    # attention à ce stade, rien n'est affiché
    fenetre = Tk()

    # on fixe le titre de la fenêtre
    fenetre.title("graphes de polynômes")

    # On démarre la boucle de gestion des évènements de
    # la fenêtre. À partir de ce moment, la fenêtre s'ouvre
    # et python gère les évènements
    # création du canevas de dessin
    canvas = Canvas(fenetre,width=largeur, height=hauteur, background="white")

    # dé#finition de la grille
    canvas.grid(column=0,row=0)

    # label pour la définition du polynôme
   #defP = "P(x) = a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 + a5*x^5"
   #Label(fenetre, text=defP).grid(column=0, row=1)

  # création d'une ligne diagonale en rouge
    #canvas.create_line(0,0,longueur,largeur,fill='red')
    canvas.create_line(format(data, largeur, hauteur), fill='red')
    fenetre.mainloop()

# on lance le programme
if __name__ == "__main__":
    #taille du canevas
    largeur = 400
    hauteur = 300
