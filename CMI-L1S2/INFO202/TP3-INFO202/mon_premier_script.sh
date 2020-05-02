#!/bin/bash

# un exemple commenté de script bash pour illustrer quelques
# fonctionnalités...

# NOTE 1 : comme en Python, on peut mettre des commentaires en utilisant le
# symbole "#".
#
# NOTE 2 : la première ligne du fichier est en général
#!/bin/bash
# De cette manière, le système reconnaitra automatiquement que le fichier est
# un script bash.
#
# NOTE 3 : pour tester, il faut commencer par "charger" le fichier dans le
# shell
#     $ source mon_premier_script.sh
# puis appeler une fonction définie
#     $ affiche_fichiers ARGUMENT1 ARGUMENT2 ARGUMENT3 ...
#

# une première fonction qui affiche seulement ses arguments qui sont des
# fichiers
function affiche_fichiers() {

    # boucle sur les arguments de la fonction
    for a in "$@"
    do
        # test pour vérifier si la variable a contient un fichier standard
        if [ -f "$a" ]
        then
            # affichage
            echo "$a est un fichier"
        fi
    done
    echo "FIN de la fonction affiche_fichiers"
}


# la fonction montre_args donnée dans le sujet, pour tester
function montre_arg() {
  echo "Tous les arguments : $@"
  echo "Argument 1: $1"
  shift
  echo "Autres arguments : $@"
}

function types() {
    for file in "$@"
    do
        if [ -f "$file" ]
        then
            echo "$file : fichier"
        elif [ -d "$file" ]
        then
            echo "$file : dossier"
        else
            echo "$file : inconnu"
        fi
    done
}
