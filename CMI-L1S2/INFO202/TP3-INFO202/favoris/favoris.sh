#!/bin/bash

FAV="$HOME/.favoris_bash"

function fav() {
    command=$1
    shift 2> /dev/null
    case $command in
        A|a) A $@;;
        C|c) C $@;;
        R|r) R $@;;
        L|l) L $@;;
        ''|--help)
            echo 'fav A <name>\n\t Ajoute le répertoire courant au favoris sous le nom `name`'
            echo 'fav C <name>\n\t Change de répertoire pour celui correspondant à `name`\n\t `name` doit être un favoris unique ou explicite'
            echo 'fav R <name>\n\t Supprime le favoris `name`\n\t `name` doit $etre explicite'
            echo 'fav L [motif]\n\t Affiche tout les favoris\n\t Si `motif` est spécifié, affiche seulement les favoris correspondant au motif'
            ;;
        *) echo "Commande inconnu"; return 1;;
    esac
}

function A() {
    echo "$1 -> $PWD" >> $FAV
    echo "le répertoire $PWD est sauvegardé dans vos favoris"
    echo "Raccourci : $1"
}

function C() {
    # -f3- permet de prendre en charge les dossiers contenant un espace
    chemin=$(grep -w "^$1.*->" $FAV | cut -d' ' -f3-)
    if [ $(echo $chemin | wc -l) -gt 1 ] # Si plusieurs favoris correspondant
    then
        chemin=$(grep -w "^$1 " $FAV | cut -d' ' -f3-) # Favoris exacte
        if [ -z $chemin ] # Si aucun favoris exacte
        then
            echo "Favoris '$1' innexistant"
            return 1
        fi
    fi
    cd $chemin
}

function R() {
    tmp=$(grep -w "^$1" $FAV)
    if [ -z $tmp ]
    then
        echo "favoris '$1' inconnu"
        return 1
    else
        tmp=$(grep -vw "^$1" $FAV)
        echo $tmp > $FAV
    fi
}

function L() {
    if [ -z $1 ]
    then
        column -t -s '->' $FAV
    else
        grep -w "^$1.*->" $FAV | column -t -s '->'
    fi
}

