#Kocsis Marcell 10.D

"""
1. Függvény, returnnel, kell egy lista ami üres, bekérünk számokat, egészeket, ezekkel feltöltjük a listát, legyen 10 szám, *-al lehet kilépni, 
a listával kell visszatérni, fügvényneve: adatbekérés
"""

"""
2. Eljárás (nincs return)  neve: adatkiir, az előző listát írja ki, paranméterként az előző függvényt kell megadnunk
"""

"""
3. Megvan a 10 számos lista kell egy függvény a  4.: minum, és 5: maximum kiszámítására, kell egy függvény az összegére
"""

"""
6. A függvény visszaad egy darabszámot, a darabszám az elemszámot jelenti azt fogja jelölni, hogy mennyi van az átlag felett
"""

#_____________________________________________________________________________________________________________________________________

#1. feladat
print("")
print("1. feladat:")
print("")
Szamok=[]
def adatbekérés():

    Szam=None
    while len(Szamok)!=10:
        Szam=input("Adj meg egy számot: ")
        if Szam=="*":
            break
        else:
            Szam=int(Szam)
            Szamok.append(Szam)
        
    if len(Szamok)==10 or Szam=="*":
        return Szamok    

print(adatbekérés())

print("")
print("_____________________________________________________________________")
print("")


#2.feladat
print("")
print("2. feladat:")
print("")

def adatkiir(adatok):
    print(adatok)
  

adatkiir(Szamok)
print("")
print("_____________________________________________________________________")
print("")

#3. feladat
print("")
print("3. feladat:")
print("")

def minimumot(szamok):
    minimum=szamok[0]
    for szam in szamok:
        if szam<minimum:
            minimum=szam

    return f"A legkisebb szám a megadott számok közül: {minimum} "     




print(minimumot(Szamok))
print("")
print("_____________________________________________________________________")
print("")

#4. feladat
print("")
print("4. feladat:")
print("")

def maximumot(szamok):
    maximum=szamok[0]
    for szam in szamok:
        if szam>maximum:
            maximum=szam
    
    return f"A legnagyobb szám a megadott számok közül: {maximum}"



print(maximumot(Szamok))

print("")
print("_____________________________________________________________________")
print("")

print("")
print("5. feladat:")
print("")

#5. feladat

def osszeg(szamok):
    osszeg=0
    for szam in szamok:
        osszeg+=szam

    return f"A lista számainak az összege: {osszeg}"    


print(osszeg(Szamok))


print("")
print("_____________________________________________________________________")
print("")


print("")
print("6. feladat:")
print("")
#6. feladat

def mennyiAzAtlagFelett(szamok):
         atlagfelett=[]
         osszeg=0
         darab=len(szamok)
         for szam in szamok:
                    osszeg+=szam
         atlag=round(osszeg/darab,2)   

         for szam in szamok:
             if szam>atlag:
                 atlagfelett.append(szam)

         return f"A lista számainak, az átlaga 2 tizedesjegy pontosággal kerekítve: {atlag}, ennyi szám van az átlag felett: {len(atlagfelett)}, és ezek: {atlagfelett}"


print(mennyiAzAtlagFelett(Szamok))