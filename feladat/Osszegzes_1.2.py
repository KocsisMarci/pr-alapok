import random
Szamok=[]

while len(Szamok)!=5:
    szam=random.randint(1,10)
    Szamok.append(szam)




def osszegzes(szamok):
    osszeg=0
    for szam in szamok:
        if szam%2==0:
            osszeg+=szam

    print(f"A lista páros számainak  az össszege: {osszeg}")
    print("_________________________________________")
    print("")
    print(f"A lista elemei: {szamok}")
  




Teszt=osszegzes(Szamok)
