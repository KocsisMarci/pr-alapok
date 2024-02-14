from ast import Param
import random
Szamok=[]
Parosak=[]
while len(Szamok)!=5:
    szam=random.randint(1,10)
    Szamok.append(szam)


def osszegzes(Szamok):

    for szam in Szamok:
        if szam%2==0:
            Parosak.append(szam)
    
    parosakszama=len(Parosak)
    print(f"A listában tárolt páros számok száma: {parosakszama}")
    print(f"A lista elemei: {Szamok}")



teszt=osszegzes(Szamok)
