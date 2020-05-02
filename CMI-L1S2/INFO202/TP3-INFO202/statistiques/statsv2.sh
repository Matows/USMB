#!/bin/bash

function stats() {
    niv=1
    case $1 in
        1 | '') niv=1;;
        2) niv=2;;
        3) niv=3;;
        --help)
            echo "'$0' and '$0 1' give small amount of information on current dir"
            echo "'$0 2' give medium amount of information on current dir"
            echo "'$0 3' give large amount of information on current dir TAKE FEW MINUTES"
            exit 0;;
        *) echo "Commande inconnu au bataillon"; exit 1;;
    esac

    echo "Analyse de $PWD :"
    t="    " # Soft tabulation

    ## Répertoires
    rep=$(find -type d | grep -vw "^.$" | wc -l) # le grep enlève le répertoire courant
    s=$([ $rep -gt 1 ] && echo s) # plurial
    printf "$t- $rep répertoire$s" # le premier ne contient pas de \n
    if [ $niv -ge 2 ]
    then
        ## Cachés
        # ne compte pas les dossiers lié à git
        rep=$(find -type d -name ".*" | grep -vE "\.(git|github)" | grep -vw "^.$" | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep répertoire$s caché$s"

        ## Vides
        rep=$(find -type d -empty | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep répertoire$s vide$s"
    fi

    ## Fichiers
    rep=$(find -type f | grep -vw "^.$" | wc -l)
    s=$([ $rep -gt 1 ] && echo s) # plurial
    printf "\n$t- $rep fichier$s"
    if [ $niv -ge 2 ]
    then
        printf " dont"

        ## Cachés
        rep=$(find -type f -name ".*" | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s caché$s"

        ## Vides
        rep=$(find -type f -empty | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s vide$s"
    fi
    if [ $niv -eq 3 ]
    then
        ## Moins de 512 kio
        rep=$(find -type f -size -$((512*1024))c | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s de moins de 512 kio"

        ## Plus de 15 Mio
        rep=$(find -type f -size +$((15*1024*1024))c | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s de plus de 15 Mio"

        ## Le plus gros fichiers
        rep=$(find -type f | xargs du 2> /dev/null | sort -n -r | head -n1 | cut -f2)
        rep=$(realpath $rep)
        printf "\n$t$t- le plus gros fichier est $rep"

        ## Types fichiers
        printf "\n\n$t  Il y a :"
        ### Python
        rep=$(find -type f -regextype sed -regex ".*\.py$" | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s Python"

        ### Image
        rep=$(find -type f | xargs file --mime-type | grep image | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s image$s"

        ### Vidéo
        rep=$(find -type f | xargs file --mime-type | grep video | wc -l)
        s=$([ $rep -gt 1 ] && echo s) # plurial
        printf "\n$t$t- $rep fichier$s image$s"

    fi
    rep=$(du -hs | cut -f1)
    printf "\n$t- taille totale : ${rep}io"


    echo $final
}

