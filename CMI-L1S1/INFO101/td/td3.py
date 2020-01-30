apparait_dans = lambda phrase, lettre: lettre in phrase # On test une seul lettre
nb_dans = lambda phrase, lettres: sum([1 for char in phrase if char in lettres])

est_consonne = lambda lettre: apparait_dans("zrtpqsdfghjklmwxcvbn", lettre)
nb_consonne = lambda phrase: nb_dans(phrase, "zrtpqsdfghjklmwxcvbn")

est_voyelle = lambda lettre: apparait_dans("aeiouy", lettre)
est_minuscule = lambda lettre: lettre.islower()
est_majuscule = lambda lettre: lettre.isupper()
est_chiffre = lambda lettre: lettre.isdigit()
from string import ponctuation
est_ponctuation = lambda lettre: lettre in ponctuation

