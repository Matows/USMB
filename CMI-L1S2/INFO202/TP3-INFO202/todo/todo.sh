#!/bin/bash

function list() {
    nl -s " - " -w 2 $TODO
}

function add() {
    if [[ $1 =~ ^[0-9]+$ ]]
    then
        before=$(( $1-1 ))
        final=$(head -n $before $TODO)
        [ $2 -eq '1' ] && n='' || n='\n'
        final="$final$n${@:2}"
        final="$final\n$(tail -n +$1 $TODO)"
        printf "$final\n" > $TODO
    else
        echo ${@:1} >> $TODO
    fi
}

function fait() {
    if [[ $1 =~ ^[0-9]+$ ]]
    then
        before=$(( $1-1 ))
        after=$(( $1+1 ))
        final=$(head -n $before $TODO)
        final="$final\n$(tail -n +$after $TODO)"
        printf "$final" > $TODO
    else
        explicite=$(grep -w "^$1.*" $TODO | wc -l)
        if [ $explicite = 1 ] 
        then 
            final=$(grep -vw "^$1.*" $TODO)
            printf "$final\n" > $TODO 
        else
            echo "Non explicite"
        fi
    fi
}

function todo() {
    TODO="$HOME/.todo_list"
    touch -a $TODO
    command=$1
    shift 2> /dev/null
    case $command in
        ''|list) list;;
        add) add $@;;
        fait) fait $@;;
        manual) $EDITOR $TODO;;
        --help)
            echo "todo list | todo\n\t Affiche les tâches à faire"
            echo "todo add [indice] <task>\n\t Ajoute la tâche \`task\` à la liste\n\t Si \`indice\` est précisé, insère la tâche à l'indice \`indice\`"
            echo "todo fait <indice|motif>\n\t Supprime la tâche :\n\t\t- Si le paramètre est un nombre, supprime la tâche d'indice \`indice\`\n\t\t- Sinon supprime suivant le motif. \n\t\t  Le motif est un groupement de lettre qui correspond au début du nom d'une tâche. \n\t\t  Ne doit désigné qu'une seul tâche"
            ;;
        *) echo "Not supported"; return 1;;
    esac
}
