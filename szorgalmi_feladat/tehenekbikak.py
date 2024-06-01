"""
A Cows and Bulls egy toll és papír kódtörő játék, amelyet általában 2 játékos játszanak. Ebben a játékos megpróbálja kitalálni a második játékos által választott titkos kódszámot. 
A szabályok a következők:
A játékos létrehoz egy titkos kódot, általában egy 4 jegyű számot. Ebben a számban nem lehetnek ismétlődő számjegyek.
Egy másik játékos tippel (4 jegyű szám), hogy feltörje a titkos számot. A tippeléskor 2 tippet adunk – tehenek és bikák.
A bikák a helyes számjegyek számát jelzik a megfelelő pozícióban, a tehenek pedig a rossz pozícióban lévő helyes számjegyek számát. Például, ha a titkos kód 1234 és a kitalált szám 1246, 
akkor 2 BIKA (az 1-es és 2-es számjegy pontos egyezéséért) és 1 COW-unk van (a rossz pozícióban lévő 4-es számjegy egyezéséért)
A játékos addig találgat, amíg fel nem törik a titkos kódot. Az a játékos nyer, aki kitalálja a minimális számú próbálkozást.

"""

szam=""

import random


while len(szam)!=4:
    szamjegy=random.randint(0,9)
    szamjegy=str(szamjegy)
    if szamjegy not in szam:
        szam+=szamjegy
    

print("Bika tehén")
print("Játék szabályok: adott egy 4 jegyű szám ki kell találni, 1 bika= 1 jó szám jó helyen, 1 tehén= 1 jó szám rossz helyen, 1 számjegy egyszer szerepelhet")


probaszam=0
talalat=False
while not talalat:
    tehen=0
    bika=0

    tipp=int(input("Tippelj egy számot: "))

    tipp=str(tipp)
    if len(tipp)==4:
        probaszam+=1

        if tipp==szam:
            talalat=True
        for index, szamjegy in enumerate(tipp):
            if szamjegy in szam and szam[index]==szamjegy:
                bika+=1
            
            if szamjegy in szam and szam[index]!=szamjegy:
                tehen+=1

    
        print(f"Válasz:  {bika} bika, {tehen} tehén")




print("Gratulálok eltaláltad")
print(f"A gondolt szám: {int(szam)} ")
print(f"Amit most tippeltél: {int(tipp)}")
print(f"Ennyi próba kellett: {probaszam}")