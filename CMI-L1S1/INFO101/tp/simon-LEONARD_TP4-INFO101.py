import pickle

def cree_date(jour, mois, annee):
    """créé une nouvelle date à partir de trois nombres entiers : un numéro de jour,
    un numéro de mois et un numéro d'année.
    """
    return pickle.dumps((jour, mois, annee))

def no_jour(date):
    """renvoie le numéro du jour correspondant à la date donnée en argument
    """
    return pickle.loads(date)[0]

def no_mois(date):
    """renvoie le numéro du mois correspondant à la date donnée en argument
    """
    return pickle.loads(date)[1]

def no_annee(date):
    """renvoie le numéro de l'année correspondant à la date donnée en argument
    """
    return pickle.loads(date)[2]


### QUESTION 1
date_aujourdhui = cree_date(6, 11, 2019)
date_noel = cree_date(25, 12, 2019)
date_anniv = cree_date(1, 1, 2020)
date_fin_annee = cree_date(31,12,2019)
date_fin_de_mois = cree_date(30,11,2019)
date_fin_fevrier_bis = cree_date(29, 2, 2020)
date_fin_fevrier_nonbis = cree_date(28, 2, 2019)

Dref = cree_date(1, 1, 1582) # vendredi


### QUESTION 2
def affiche_date(date):
    print(no_jour(date), no_mois(date), no_annee(date), sep="-")


### QUESTION 3
def lendemain(date):
    """Fonction prenant un date et renvoyant la date du lendemain.
        C'est une fonction simplifié incorrect.
    """
    return cree_date(no_jour(date) + 1, no_mois(date), no_annee(date))
#>>> affiche_date(lendemain(cree_date(31, 11, 2019)))
#32-11-2019
#>>> affiche_date(lendemain(cree_date(31, 12, 2019)))
#32-12-2019


### QUESTION 4
def decale_date(date, shift):
    for i in range(shift):
        # Nous n'avons pas besoin de la date original donc je réutilise la variable locale date.
        date = lendemain(date)
    return date
#>>> affiche_date(date_aujourdhui)
#6-11-2019
#>>> affiche_date(decale_date(date_aujourdhui, 3))
#9-11-2019


### QUESTION 5
fin_annee = lambda date: no_mois(date) == 12 and no_jour(date) == 31


### QUESTION 6
def lendemain(date):
    if fin_annee(date):
        return cree_date(1, 1, no_annee(date) + 1)
    return cree_date(no_jour(date) + 1, no_mois(date), no_annee(date))


### QUESTION 7
#>>> affiche_date(lendemain(date_aujourdhui))
#7-11-2019
#>>> affiche_date(lendemain(date_fin_annee))
#1-1-2020


### QUESTION 8
est_bissextile = lambda annee: annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0


### QUESTION 9
def nb_jours_ds_mois(mois, annee):
    if mois == 2:
        return 28 + est_bissextile(annee)
    elif (mois % 2 == 0 and mois <= 7) or (mois % 2 != 0 and mois >= 8):
        return 30
    else:
        return 31


### QUESTION 10
def fin_de_mois(date):
    return no_jour(date) == nb_jours_ds_mois(no_mois(date), no_annee(date))


### QUESTION 11
def lendemain(date):
    if fin_annee(date):
        return cree_date(1, 1, no_annee(date) + 1)
    elif fin_de_mois(date):
        return cree_date(1, no_mois(date) + 1, no_annee(date))
    else:
        return cree_date(no_jour(date) + 1, no_mois(date), no_annee(date))
#>>> affiche_date(lendemain(date_fin_de_mois))
#1-12-2019
#>>> affiche_date(lendemain(date_fin_fevrier_bis))
#1-3-2020
#>>> affiche_date(lendemain(date_fin_fevrier_nonbis))
#1-3-2019


### QUESTION 12
#>>> affiche_date(decale_date(date_aujourdhui, 28))
#4-12-2019
#>>> affiche_date(decale_date(date_noel, 7))
#1-1-2020


### QUESTION 13
def est_avant(date1, date2):
    d_annee = no_annee(date2) - no_annee(date1)
    d_mois = no_mois(date2) - no_mois(date1)
    d_jour = no_jour(date2) - no_jour(date1)

    if d_annee > 0:
        return True
    elif d_mois > 0:
        return True
    elif d_jour > 0:
        return True
    else:
        return False


### QUESTION 14
def nb_jours_entre(date1, date2):
    """ calcule le nombre de jours qui séparent 2 dates données.
    	en entrée : 2 dates date1 et date2 tel que date1 <= date2
    	résultat : un entier
    """
    res = 0
    while est_avant(date1, date2):
        date1 = lendemain(date1)
        res = res + 1
    return res
#>>> nb_jours_entre(date_aujourdhui, date_noel)
#49
#>>> nb_jours_entre(date_aujourdhui, date_anniv)
#56


### QUESTION 15
def suivant(jour_semaine):
    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    s = (semaine.index(jour_semaine) + 1) % 7
    return semaine[s]


### QUESTION 16
def quel_jour(date):
    d_jours = nb_jours_entre(Dref, date)
    jour_semaine = "vendredi"

    for i in range(d_jours):
        jour_semaine = suivant(jour_semaine)

    return jour_semaine


### QUESTION 17
def nb_lundis(date1, date2):
    """Prend en paramètre deux date avec date1 < date2.
        Renvoie le nombre de lundis entre les deux dates inclus.
    """
    lundi_date1 = quel_jour(date1) == "lundi"
    nombre_lundis = nb_jours_entre(date1, date2) // 7 + lundi_date1
    return nombre_lundis


### QUESTION 18
def combien_de(jour_semaine, date1, date2):
    inclu_date1 = quel_jour(date1) == jour_semaine
    return nb_jours_entre(date1, date2) // 7 + inclu_date1


### QUESTION 19
def vendredi_13(annee1, annee2):
    date1 = cree_date(1, 1, annee1)
    date2 = cree_date(1, 1, annee2)
    d_date = nb_jours_entre(date1, date2)
    jour_semaine = quel_jour(date1) # un peu long
    nb_v13 = 0
    while d_date > 0:
        if no_jour(date1) == 13:
            if jour_semaine == "vendredi": # on limite le temps de calcul
                nb_v13 += 1
        date1 = lendemain(date1)
        jour_semaine = suivant(jour_semaine)
        d_date -= 1
    return nb_v13


### QUESTION 20
# Entre 1600 et 2000 il y a 688 vendredi 13. 
# Je remarque également que entre 2000 et 2400 il y a aussi 688 vendredi 13. 
# Après quelques tests, j'en conclu qu'il y a toujours 688 vendredi 13 sur une perdiode de 400 ans.
