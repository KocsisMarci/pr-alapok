"""
Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót,
és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
"""
import random
random_index=random.randint(1,4)
lehetseges_szavak=["programozás","Bükk","munka","pankráció","relaxáció"]

szo=lehetseges_szavak[random_index]

print(szo)
jo_tippek=[]
rossz_tippek=[]
eleg=False
szamok=["0","1","2","3","4","5","6","7","8","9"]
while eleg!=True:
    betu=input("Adj meg egy betűt amiről úgy gondolod, hogy a tárolt szóban van: ")

    if len(betu)>1 or betu in szamok:
            print("Betűt adj meg! ")
    else:
        if betu in szo and betu not in jo_tippek and betu!="":
            jo_tippek.append(betu)
        elif betu not in szo and betu not in rossz_tippek and betu!="":
            rossz_tippek.append(betu)
        if betu=="":
            eleg=True



print("A jó tippeid:")
print(jo_tippek)
print("")
print("A rossz tippeid:")
print(rossz_tippek)
