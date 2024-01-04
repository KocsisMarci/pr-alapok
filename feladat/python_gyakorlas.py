import random
szam=random.randint(1,3)

bekerendo=int(input("Adj meg egy számot 1 és 3: "))
while bekerendo>3 or bekerendo <1:
    bekerendo=int(input("Az általad megadott szám nem ebbe a tartományba esik: "))

if 1<=bekerendo<=3:
    if szam<bekerendo:
        print(f"Az általad megadott szám: {bekerendo}, nagyobb mint a gép száma: {szam}")
    elif szam>bekerendo:
            print(f"Az általad megadott szám: {bekerendo}, kisebb mint a gép száma: {szam}")
    elif szam==bekerendo:
            print(f"Az általad megadott szám: {bekerendo}, egyelő a gép számával: {szam}")    