#hazi_feladat_029
"""
Az előző programot alakítsd át úgy, hogy a feltételeknek megfelelő szavak kerüljenek rögzítésre 
egy másik listában is, és ez utóbbi listát írja ki a program a képernyőre!
"""
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
tvel=[]
for keres in szavak:
    if keres[0]=="t" or keres[0]=="T":
        tvel.append(keres)

print(tvel)        