"""
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza.
Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
"""

class Negyzet:
    def __init__(self,oldalhossz):
        self.oldalhossz=oldalhossz
    
    def kerulet(self):
        return f"A négyzet kerülete 2 tizedesjegy pontosággal: {self.oldalhossz*4:.2f} cm"

    def terulet(self):
        return f"A négyzet területe 2 tizedesjegy pontosággal: {self.oldalhossz*self.oldalhossz:.2f} négyzet cm"


negyzet1=Negyzet(5)
negyzet2=Negyzet(7)
print(negyzet1.kerulet())
print(negyzet1.terulet())
print("")
print(negyzet2.kerulet())
print(negyzet2.terulet())