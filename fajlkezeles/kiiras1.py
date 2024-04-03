#Fájlbaírás lehetőségei
#Megnyitási módok:
# r: olvasás
# w: írás, fájlt hoz létre; ha létezik ilyen nevű fájl már, felülírja az eredetit, ha nem létrehoz egyet
# a: a létező fájl végére hozzáfűz, ha mlg nem létezik ilyen létrehoz

with open("kimenet1.txt", "w", encoding="utf-8") as celfajl:
        #sztringet ír a fájlba
        celfajl.write('aaaaalma, körte, eper')
        celfajl.write('aaaaalma, kkkkkörte, eper')