"""
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!
"""


#A feladatokban a listákat for ciklussal járom be.


with open("forras.txt","r",encoding="utf-8") as forras:
    Szotarak_listaja=[]
    Listak_Listaja=[]
    
    print("")

    for sor in forras:
        ev,nyelv,keresztnev,vezeteknev=sor.strip().split(";")
        Szotar={
            "Év":int(ev),
            "Nyelv":nyelv,
            "Szerző keresztneve":keresztnev,
            "Szerző vezetékneve:":vezeteknev
        }
        Lista=[ev,nyelv,keresztnev,vezeteknev]
        Szotarak_listaja.append(Szotar)
        Listak_Listaja.append(Lista)

    for szotar in Szotarak_listaja:
        print(szotar)    

    
    print("")
    print("")

    for lista in Listak_Listaja:
        print(lista)