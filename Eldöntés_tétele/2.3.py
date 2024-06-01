"""
Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet megadnia.
A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot!
A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).
"""



szo="programozás"

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
