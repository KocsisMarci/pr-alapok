import random

class Kutya:
    def __init__(self,nev,eletkor,nem):
        self.nev=nev
        self.eletkor=eletkor
        self.nem=nem
    
    def kiir(self):
        print(f"A kutya neve: {self.nev}")
        print(f"A kutya életkora : {self.eletkor}")
        print(f"A kutya neme: {self.nem} ")

    


nev=(input("Add meg a kutya nevét: "))
eletkor=random.randint(0,31) #A 31 azért, mert a világ legidősebb kutyája, Bobi, 31 évet élt
nem_szama=random.randint(0,1)

if nem_szama==0:
    nem="kan"
else:
    nem="szuka"

kutya=Kutya(nev,eletkor,nem)
kutya.kiir()




