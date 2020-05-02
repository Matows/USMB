#!/usr/bin/env python3

def create_hole(filename, size, start="START\n", end="\nEND"):

    b_start = bytes(start, "UTF-8")
    b_end = bytes(end, "UTF-8")

    f = open(filename, mode="wb")
    f.write(b_start)
    f.seek(size - len(end))
    f.write(b_end)
    f.close()

if __name__ == "__main__":
    import sys

    if not 1 < len(sys.argv) < 4:
        print("Utilisation :\n   {} taille [nom_fichier]".format(sys.argv[0]))
        sys.exit(1)

    try:
        s = sys.argv[1].strip()
        if s[-1] in "0123456789":
            size = int(s)
        elif s[-1] in "kK":
            size = int(s[:-1]) * 1<<10
        elif s[-1] in "mM":
            size = int(s[:-1]) * 1<<20
    except:
        print("'{}' n'est pas une taille valide...".format(s))
        sys.exit(1)


    if len(sys.argv) == 3:
        filename = sys.argv[2]
    else:
        filename = "sparse_file"

    create_hole(filename, size)
    print("Le fichier {} a été créé...".format(filename))
