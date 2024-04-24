diak2_adatok=["Daryl","Dixon"]

class Diak:
    keresztnev=diak2_adatok[0]
    def __init__(self,veznev,knev):
        self.veznev=veznev
        self.knev=knev
    
    def megkerdez(self,keresztnev):
        print(f"Hogy hívnak, {keresztnev}? ")
    
    def valaszol(self):
        print(f"A nevem: {self.veznev} {self.knev}")



diak1=Diak("Phillip","Blake")
diak2=Diak(diak2_adatok[0],diak2_adatok[1])
diak1.megkerdez(Diak.keresztnev)
diak2.valaszol()