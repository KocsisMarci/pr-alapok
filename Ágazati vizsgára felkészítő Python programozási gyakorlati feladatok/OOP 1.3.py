"""

Az 1.1 feladatban meghatározottak szerint készíts egy programot, amely a felhasználótól egymás után bekér négyzetek oldalhosszát egészen addíg, 
amíg a felhasználó 0 értéket nem ad meg! Ezen adat alapján a program hozzon létre negyzet objektumokat, melyeket egy listában tárol! 
A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
"""


class Negyzet:
    def __init__(self,oldalhossz):
        self.oldalhossz=oldalhossz

    def kerulet(self):
         return f"A négyzet kerülete 2 tizedesjegy pontosággal: {self.oldalhossz*4:.2f} cm"


    def terulet(self):
        return f"A négyzet területe 2 tizedesjegy pontosággal: {self.oldalhossz*self.oldalhossz:.2f} bégyzet cm"
    



oldalhosszak=[]
megall=False
while not megall:
    oldalhossz=int(input("Add meg egy négyzet oldalhosszát: "))
    if oldalhossz==0:
        megall=True
    
    else:
        oldalhosszak.append(oldalhossz)


for oldal in oldalhosszak:
    negyzet=Negyzet(oldal)
    if oldal!=oldalhosszak[-1]:
        print(f"Az alábbi négyzet oldalhossza: {oldal} cm ")
        print(negyzet.kerulet())
        print(negyzet.terulet())
        print("")
    else:
        print(f"Az alábbi négyzet oldalhossza: {oldal} cm ")
        print(negyzet.kerulet())
        print(negyzet.terulet())
