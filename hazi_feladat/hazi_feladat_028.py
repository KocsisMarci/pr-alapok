#hazi_feladat_028
#Az adott lista (amely a 'Próbáld ki!' gombra kattintva elérhető) elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for keres in szavak:
    if keres[0]=="t" or keres[0]=="T":
        print(keres)
