#A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát, és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!

with open("forras.txt", "r", encoding="utf-8") as forrasfajl,\
    open("cel.txt","w", encoding="utf-8") as celfajl:
    for sor in forrasfajl:
        sor=sor.strip().split(";")

        celfajl.writelines([f"{sor[0]} ",f"{sor[1]}\n"])