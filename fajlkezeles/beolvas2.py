#A teljes fájltartalom beolvasása
#listávál tér vissza, a sorok a lista elemei
with open("otsor.txt","r",encoding="utf-8") as forrasfajl:
    lista=forrasfajl.readlines()

jo_lista = []
rossz_lista = []    
for sor in lista:
    rossz_lista.append(sor)
    sor=sor.strip()
    jo_lista.append(sor)

print(rossz_lista)
print(jo_lista)