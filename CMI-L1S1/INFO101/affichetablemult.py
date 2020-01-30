def affiche_table(liste):
    ...

def construit_table(largeur, hauteur):
    tab = [[],[]]

    for nb in range(largeur):
        tab[0].append(nb+1)

    for nb in range(hauteur):
        tab[1].append(nb+1)

    for line in hauteur:
        tab.append([])
    return tab
