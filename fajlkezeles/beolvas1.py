#A fájl tartalmának beolvasás, amikor egy sort olvasok be:
with open("otsor.txt","r",encoding="utf-8") as forrasfajl:
    sor=forrasfajl.readline()
    print(len(sor))
    print(sor)
    sor=sor.strip()
    print(len(sor))
    print(sor)
    sor=forrasfajl.readline()
    print(len(sor))
    print(sor)
    sor=sor.strip()
    print(len(sor))
    print(sor)