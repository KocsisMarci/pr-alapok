#A saját megoldásom:

"""
class Beteg:
    def __init__(self,nev,tajszam,sorszam):
            self.nev=nev
            self.tajszam=tajszam
            self.sorszam=sorszam
    

    def leir(self):
        varakozasiido=self.sorszam*5
        print(f"{self.sorszam}. {self.nev} {self.tajszam}, Várható várakozás: {varakozasiido} perc.")


betegek=[]
eleg=False
sorszam=0
while not eleg:
        nev=input("Add meg a beteg nevét! ")
        taj_szam=input("Add meg a beteg TAJ számát! ")
        beteg=Beteg(nev,taj_szam,sorszam)
        betegek.append(beteg)
        sorszam+=1
        if len(betegek)==3:
            eleg=True


for beteg in betegek:
    beteg.leir()



"""

#A minta megoldás: 
class Beteg:
    def __init__(self,nev="",TAJ="",sorszam=0):
        self.nev=nev
        self.TAJ=TAJ
        self.sorszam=sorszam
    
    def varakozas(self):
        return self.sorszam*5
    
betegek=[]

for i in range(3):
    nev=input("Add meg a beteg nevét! ")
    TAJ=input("Add me a beteg TAJ számát! ")
    beteg=Beteg(nev,TAJ,i)
    betegek.append(beteg)

for beteg in betegek:
    print(f"{beteg.sorszam}. {beteg.nev} {beteg.TAJ}, Várható várakozás: {beteg.varakozas()} perc.")