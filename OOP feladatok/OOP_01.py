import random
class Kor: 
    def __init__(self,sugar,kozeppont=(0,0)):
        self.sugar=sugar
        self.kozeppont=kozeppont

    
    def terulet(self):
        return pow(self.sugar,2)*3.14
    
    def kerulet(self):
        return self.sugar*3.14*2

"""
#objektum létrehozása
kor01=Kor(5)
print(kor01.kozeppont)
print(kor01)
print(type(kor01))
print(isinstance(kor01,Kor)) #Rákérdezni, hoya kor01 a Kor osztály objektum példánya-e?
print(kor01.kozeppont)
print(kor01.sugar)


kor02=Kor(10,(1,1))
print(kor02.kozeppont)
print(kor02.kozeppont)
print(kor01.terulet())
print(kor02.terulet())
print(kor01.kerulet())
print(kor02.kerulet())
"""
"""




"""
korok=[]
for _  in range(5):
    kor=Kor(random.randint(1,10))
    korok.append(kor)


for kor in korok:
    print(kor.sugar,kor.kerulet())

print(korok[1].sugar)