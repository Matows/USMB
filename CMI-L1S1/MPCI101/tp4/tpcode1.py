from tkinter import *

#taille du canevas
longueur= 400
hauteur = 300


#tableau de donnée
a=[0,-5,0,1,0,0.04]

#autre donné
xmin=-5
xmax=5
ymin=-5
ymax=5
tab = []

def draw():
    pasx = (xmax - xmin) / (longueur-1)
    pasy= (hauteur-1)/(ymax - ymin)
    for xpixel in range(0, longueur):
        x = xpixel * pasx + xmin
        y = a[0]+x*a[1]+a[2]*x**2+a[3]*x**3+a[4]*x**4+a[5]*x**5
        ypixel = hauteur/2-y*pasy
        tab.append(xpixel)
        tab.append(ypixel)


def main():
    """initialisation d'une fenêtre avec tkinter"""
    # creation de l'objet fenêtre en python
    # attention à ce stade, rien n'est affiché
    fenetre = Tk()

    # on fixe le titre de la fenêtre
    fenetre.title("graphes de polynômes")

    # création du canevas de dessin
    canvas = Canvas(fenetre,width=longueur, height=hauteur, background="white")

    # dé#finition de la grille
    canvas.grid(column=0,row=0)

    # label pour la définition du polynôme
    defP = "P(x) = a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 + a5*x^5"
    Label(fenetre, text=defP).grid(column=0, row=1)
    # On démarre la boucle de gestion des évènements de
    # la fenêtre. À partir de ce moment, la fenêtre s'ouvre
    # et python gère les évènements
    # création des absice
    canvas.create_line(0,150,399,150,fill='blue')
    # création des ordonné
    canvas.create_line(200,0,200,299,fill='blue')
    draw()
    canvas.create_line(*tab,fill='red')

    #creation caneva de dessin
    bou1 = Button(fenetre,text='Quitter',command=fenetre.quit)
    bou1.grid(column=0, row=2)
    fenetre.bind("q", lambda _: fenetre.destroy())

    fenetre.mainloop()


# on lance le programme
main()


