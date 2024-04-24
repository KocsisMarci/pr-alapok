#Olvasás - írás

with open("gyumolcsok.txt", "r", encoding="utf-8") as forrasfajl, \
    open("gyumolcsok_masolata.txt","w",encoding="utf-8") as celfajl:
    for sor in forrasfajl:
        celfajl.writelines([f"{sor}\n"])