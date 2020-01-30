def mult2_pas3(nb):
    """fonction qui indique si un nombre nb passé en paramètre est multiple de 2 et pas de 3.
    	en entrée : nb - 1 nombre - le nombre dont on cherche à savoir s'il est divisible par 2 et pas par 3.
    	résultat : un booléan = vrai si nb est multiple de 2 mais pas de 3."""
    	
    reste2 = (nb % 2)
    reste3 = (nb % 3)
    if ((reste2 == '0') and (reste3!='0')):
        res = True
    else:
        res = False
    return res
