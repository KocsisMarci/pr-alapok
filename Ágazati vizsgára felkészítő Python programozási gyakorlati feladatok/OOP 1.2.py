"""
Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza, 
hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
"""

class Negyzet:
    def __init__(self,oldalhossz):
        self.oldalhossz=oldalhossz
    
    def kerulet(self):
        print(f"A négyzet kerülete 2 tizedesjegy pontosággal: {self.oldalhossz*4:.2f} cm")

    def terulet(self):
        print(f"A négyzet területe 2 tizedesjegy pontosággal: {self.oldalhossz*self.oldalhossz:.2f} négyzet cm")


negyzet1=Negyzet(5)
negyzet2=Negyzet(7)
negyzet1.kerulet()
negyzet1.terulet()
print("")
negyzet2.kerulet()
negyzet2.terulet()