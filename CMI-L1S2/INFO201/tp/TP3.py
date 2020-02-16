#!/usr/bin/env python3
# coding: utf-8

def affiche(n):
    if n>0:
        print(n)
        affiche(n-1)
# Q1: Il ne se passe rien, car la condition revoie false pour un nomre négatif

def fonction_mystere(l):
    if l == "":
        return 0
    else:
        c = l[0]
        if c == 'a':
            resultat = 1
        else:
            resultat = 0
        s = l[1:] # on prend la sous-chaine sans le premier caractère    
        resultat = resultat + fonction_mystere(s) # appel récursif
        return resultat
# Q2: Compte le nombre de 'a'
