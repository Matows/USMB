# TD3

## Exo 1

2. À cause des blocs. FS de blocs de 4ko = la taille des fichiers est un multiple de 4ko. Vérifier la taille d'un fichier sur le disque = `ls -sh`
3. 
    - 1o (1 bloc) -> gaspillage : (4096 - 1) / 4096 = 0.9997558593750
    - 1kio + 1o (1 bloc) -> gaspillage : (4096-1025)/4096 = 0.749 
    - 1 mio + 1 o (256 + 1 bloc) & 1mio + 4kio    & 0.389%
    - 1 gio + 1 o (262144 + 1 bloc)  & 1gio + 4kio    & 0.000381%
4. Proprio, perm, nom du fichier... Oui elles occupent de l'espace

## Exo 2

1. absolu = depuis la racine. relatif = depuis le répertoir courant.
2. 
    - OLD: {/home/pierre/info202/,}OLD
    - tom: {/home/,../../}tom
    - info202: {/home/pierre/info202,.}
    - VRzQOcf: {/tmp/,../../../tmp/}VRzQOcf
3. 
    - `.py` -> {tp1,tp2}.py
    - `*.?` -> test.h
    - `*[ch]` -> test.cc, test.h
    - `*.?/*h` -> RIEN
    - `*.*` -> tout les fichiers avec extension (tout les fichiers sauf OLD)

# Exo 3

1. 
```
70 72 6f 6a 65 74 00 01 00 00 00 04 54 4f 44 4f
 p  r  o  j  e  t // //  -tailleF-  T  O  D  O
```
2. Il faut parcourir toute l'arborescence et vérifié que l'octet est après le dernier `ff ff ff ff`
3.
