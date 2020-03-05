#!/usr/bin/env python3
# coding: utf-8

from random import shuffle

def sauvegarde_nom_score(nom_fichier: str, nom: str, score: float) -> None:
    """sauvegarde un nom et un score dans un fichier :

    Paramètres :
      - nom_fichier, de type chaine de caractères : nom du fichier où sauvegarder le score
      - nom, de type chaine de caractères : nom du joueur
      - score, de type flottant : score du joueur
    """

    file = open(nom_fichier, 'w')
    file.write(nom + '\n' + str(score))
    file.close()

#sauvegarde_nom_score("file.txt", "simon", 12.0)

def lire_score(nom_fichier: str) -> float:
    """lit et renvoie le score (deuxième ligne) dans un fichier

    paramètre : nom_fichier, de type chaine de caractères : nom du fichier à ouvrir

    valeur de retour : flottant
    """

    file = open(nom_fichier, 'r')
    file.readline() # nom
    score = float(file.readline())

    file.close()
    return score

#print(lire_score("file.txt"))

def question(q: dict) -> int:
    """Affiche une question, propose des réponses, et dit si la réponse de l'utilisateur est bonne"""
    #Affichage question
    print(q['question'])
    reponses = [q['correcte'], q['incorrecte']]
    shuffle(reponses)
    print("1 - " + reponses[0], "2 - " + reponses[1], sep="\n")

    #Intéraction utilisateur
    choice = int(input("Entrez votre choix : "))
    if reponses[choice-1] == q['correcte']:
        print("Bonne réponse !")
        return 1
    else:
        print("Mauvaise réponse !")
        return -1

def questionnaire(qs: dict, fonction_question=question) -> float:
    """Pose toutes les questions du questionnaire "qs" passé en argument. Renvoie le score.
        fonction_question pour prendre en compte la seconde question
    """
    scores = []
    shuffle(qs)
    for i in range(len(qs)):
        print("Question", i+1, ":", end="  ")
        score = fonction_question(qs[i])
        scores.append(score)
        print()
    
    print("Fin du questionnaire.")
    pourcentage = sum(scores)*100/len(qs)
    return pourcentage

def lecture_quizz(file_name: str) -> list:
    """Renvoie une liste de question à partir dur fichier file_name"""
    questions = []
    file = open(file_name, 'r')
    current_line = file.readline()
    while current_line != '':

        if current_line != '\n':
            current_line = current_line.strip()

            if current_line[0] == '+': # Réponse juste
                questions[-1]['correcte'] = current_line[2:]

            elif current_line[0] == '-': # Réponse fausse
                questions[-1]['incorrecte'] = current_line[2:]
            
            else: # Question
                questions.append({'question':current_line})
        current_line = file.readline()
                
    file.close()
    return questions

def gestion_score(s: float) -> None:
    """Récupère le score dans score.txt et le met à jour si s est plus grand que le score stocker"""
    score = lire_score("score.txt")
    if s > score:
        username = input("Votre nom d'utilisateur : ")
        sauvegarde_nom_score("score.txt", username, s)

def quizz(fichier: str) -> None:
    file_score = open("score.txt", 'r')
    username = file_score.readline().strip()
    score = float(file_score.readline().strip())
    file_score.close()

    print("Le meilleur joueur est {} avec {:0.0f}%\n".format(username,score))

    questions = lecture_quizz(fichier)
    score = questionnaire(questions)
    print("Votre score est de {:0.0f}".format(score))
    gestion_score(score)

def question_qcm(q: dict) -> int:
    """Affiche une question, propose des réponses, et dit si la réponse de l'utilisateur est bonne.
		Renvoie le nombre de points gagnés/perdus
	"""
    #Affichage question
    print(q['question'])
    reponses = q['correcte'][:]
    reponses.extend(q['incorrecte'])
    # PYTHONNERIES
    # reponses = [*q['correcte'], *q['incorrecte']]
    # `*liste` sert à passer (ou recevoir) des arguments un à un à une fonction (ici un constructeur, list.__init__()).
    # `liste` passé à une fonction sera juste vue comme une liste.
    # il y a aussi les arguments nommé `**dico`, voir lien ci-dessous
    # https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232273-utilisez-des-dictionnaires#/id/r-2232590
    shuffle(reponses)
    for i, rep in enumerate(reponses):
        print("{} - {}".format(i+1, reponses[i]))

    #Intéraction utilisateur
    choice = int(input("Entrez votre choix : "))
    if reponses[choice-1] in q['correcte']:
        print("Bonne réponse !")
        return 1
    else:
        print("Mauvaise réponse !")
        return -(len(q['correcte'])/len(q['incorrecte']))

def lecture_qcm(file_name: str) -> list:
    """Renvoie une liste de question à partir dur fichier file_name"""
    questions = []
    file = open(file_name, 'r', encoding="utf-8")
    current_line = file.readline()
    while current_line != '':

        if current_line != '\n':
            current_line = current_line.strip()

            if current_line[0] == '+': # Réponse juste
                questions[-1]['correcte'].append(current_line[2:])

            elif current_line[0] == '-': # Réponse fausse
                questions[-1]['incorrecte'].append(current_line[2:])
            
            else: # Question
                questions.append({'question':current_line, 'correcte':[], 'incorrecte':[]})
        current_line = file.readline()
                
    file.close()
    return questions

def quizz2(fichier: str) -> None:
    file_score = open("score.txt", 'r')
    username = file_score.readline().strip()
    score = float(file_score.readline().strip())
    file_score.close()

    print("Le meilleur joueur est {} avec {:0.0f}%\n".format(username,score))

    questions = lecture_qcm(fichier)
    score = questionnaire(questions, question_qcm)
    print("Votre score est de {:0.2f}".format(score))
    gestion_score(score)
