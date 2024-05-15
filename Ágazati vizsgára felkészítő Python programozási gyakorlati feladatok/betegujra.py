class Beteg:
    def __init__(self,nev,TAJ,sorszam):
        self.nev=nev
        self.TAJ=TAJ
        self.sorszam=sorszam
    
    def idot_szamit(self):
        ido=self.sorszam*5
        return ido


betegek=[]
for i in range(3):
    nev=input("Add meg a beteg nevét! ")
    taj=input("Add meg a beteg TAJ számát! ")
    beteg=Beteg(nev,taj,i)
    betegek.append(beteg)


kiiratas_sorszam=0
for beteg in betegek:
    print(f"{kiiratas_sorszam}. {nev} {taj}, Várható várakozás: {beteg.idot_szamit()} perc.")
    kiiratas_sorszam+=1