"""
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában.
Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában!
Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
"""


import random

szamok=[]

while len(szamok)!=5:
    szam=random.randint(1,7)
    szamok.append(szam)



kert_szam=int(input("Adj meg egy számot, ami szerinted előfordul a szamok listában: "))


if kert_szam in szamok:
    print(f"Az általad megadott szám: {kert_szam}, szerepel a számok listában")

else:
    print(f"Az általad megadott szám: {kert_szam}, nem szerepel a számok listában")



print("A lista számai: ")

szamlalo=0
for szam in szamok:
    if szamlalo!=4:
        print(f"{szam}, ", end="")
    else:
        print(f"{szam}", end="")

    szamlalo+=1