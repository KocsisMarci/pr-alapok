import random #random modul beimportálása
dobások=[] #Egyelőre egy üres lista
for _ in range(10000000): #Amég nem lesz 10000000 addig fut a program, a(z) _ az amivel végig megyünk
        dobás=random.randint(1,6) #1 és 6 között kapunk egy véletlen számot
        dobások.append(dobás) #a dobások listához hozzáadjuk az aktuális dobás értékét


ennyi_hatos=0 #Ez a változó fogja jelezni a hatos találatok számát

for dobás in dobások: #Végig megyünk a dobások listán, amely tartalmazza a rengeteg dobást
    if dobás==6:
        ennyi_hatos+=1 #Ha a dobás értéke hat, akkor az ennyi_hatos változót megnöveljük eggyel.


print("Összesen", ennyi_hatos, "hatost dobtunk.") #Kiiratjuk mennyi hatost "dobtunk"

