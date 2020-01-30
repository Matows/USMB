# INFO201 : Algorithmique


## Vocabulaire

Expressions : `"anthony"`, `true`, `4+2`, `t[3]+t[4]`.
Expression affectable : A gauche d'un signe `=` (`x`, mais PAS `4+2`).
Instruction : `estNbPremier(4)`, `x=x+1`.
procédure : fonction ne renvoyant rien.


## Complément sur les boucles for

- On connait le nombre d'itération.
- On peut changer le pas dans range : `range(10)`, `range(0,10,2) #Pas de 2`.

Ex : 
```py
t = [3,1,4,5,6,9,-2,-3,2,3,7,8,2,9,13]
sum = 0
for i in range(2, len(t), 5):
    sum += t[i]
print(sum) #=3
```
My way: `print(sum([x for x in t[2::5]))`


## Boucles while

- On ne connait pas le nombre d'itération (à l'avance)
- Syntax : 
```
while <<Condition>>:
    ...
```

Ex1 :
```py
def afficheNbPremier(n):
    nb = 0
    nbjour = 0
    while nbjour <= n:
        if estNbPremier(nb):
            print(nb, end=' ')
            nbjour += 1
        nb+=1
```

Ex2 :
```py
def nb_jour_avant_mort(nbHab):
    """Le nombre de personnes infecté est multiplié par deux chaque jour"""
    infecte = 1
    nbJour = 1
    while infecte < nbHab:
        infecte *= 2
        nbJour += 1
    return nbJour
```

## Tuples

Séquence d'éléments non modifiable.

```py
>>> rouge = (255, 0, 0)
```

Exercice :
Écrire une fonction qui renvoie la composante principale d'une fonction.
```py
def dominante(color: (int, int, int) ) -> str:
    m = max(color)
    return ["Rouge", "Vert", "Bleu"][color.index(m)]
```

## Tableaux à plusieurs dimensions

```py
prix_loc = [ [65, 80, 100], [55, 70, 90], [50, 60, 75] ]
def prix(nbjours, taille, tab=prix_loc):
    taille = {"petit":0, "moyen":1, "grand":2}[taille] # Conversion str -> int
    prix = -1
    if nbjours == 1:
        prix = prix_loc[0][taille]
    elif 1 < nbjours < 7:
        prix = prix_loc[1][taille]
    elif nbjours >= 7:
        prix = prix_loc[2][taille]
    return prix * nbjours
```

## Dictionnaires

