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
// you know how it works


## Fonctions : rappels

Une fonction est composé de :
- Paramètres
- Entrées
- Sortie (ou pas!)
- Du code (suite d'insctruction)
- Docstring

La première ligne (la ligne de déclaration de la fonction) s'appelle le **prototype** ou **signature** de la fonction.

Syntax : 
```py
def nomFonction(paramètres): #Prototype
    ...
```

### Utilité

- Évite les répétition et la duplication
- Structurer le code
- Gagner en clareté
- Tester le code en plusieurs parties

### Variables locales
Varaibles définie à l'intérieur d'une fonction et qui ne peut être utilisé que dans cette fonction

### Importer des fonctions

`from random import randint`
- À faire en début de fichier
- On peut importer une unique fonction ou toutes les fonctions du fichier (\*)
    * `from Image import *`

## Parapètres (de fonction)

### Définition et exemple

- Variables particulières qui permettent de recevoir des données, elles sont déjà initialisées au début de la fonction
- Une fonction peut ne pas avoir de paramètres

### Paramètres par défaut

Les paramètres par défaut doivent être après les paramètres obligatoires.

### Peut-on modifier les paramètres ?
Dépend si les paramètres sont passé par valeur ou par référence.

## Sorties/Valeurs de retour

- Fonctions sans valeur de retour : les procédures
- Avec valeur de retour

## Décomposition en sous-fonctions

Diviseurs stricts de 6 : 1, 2, 3

- écrire un programme qui affiche les 5 premiers entiers parfaits
```py
def isPerfect(n):
    diviseurs = [nb for nb in range(1,n) if (n / nb).is_integer()]
    return sum(diviseurs) == n

def display5FirstPerfect():
    n = 1
    cpt = 0
    while cpt = 0 < 5:
        if isPerfect(n):
            print(n)
            cpt += 1
        n += 1
```
