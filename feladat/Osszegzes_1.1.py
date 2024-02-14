import random
Szamok=[]

while len(Szamok)!=5:
    szam=random.randint(1,10)
    Szamok.append(szam)




def osszegzes(szamok):
    osszeg=0
    for szam in szamok:
        osszeg+=szam

    print(f"A lista számainak az össszege: {osszeg}")
    print("_________________________________________")
    print("")
    print(f"A lista elemei: {szamok}")
  




Teszt=osszegzes(Szamok)
