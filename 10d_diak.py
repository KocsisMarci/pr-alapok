# A Diak osztály létrehozása

class Diak:
    szam_01 = 5
    szam_02 = 10
    def __init__(self,vezeteknev,keresztnev, osztaly = "10.D", csoport='1. csoport'):
        self.vnev=vezeteknev
        self.knev=keresztnev
        self.osztaly=osztaly
        self.csoport=csoport
    
    def bemutatkozas(self):
        return self.vnev + " " + self.knev + "nak hívnak."

    def kerdes(self):
        return f"Mennyi az {Diak.szam_01} és a {Diak.szam_02} összege?"
#---------------------------------------------------------------------   
   


diak_01=Diak("Bacskai","Bálint")
diak_02=Diak("Bak","Balázs")
diak_03=Diak("Bak3","Balázs3", "13.D", "22. csoport")


print(f"{diak_01.vnev} {diak_01.knev} {diak_01.osztaly} {diak_01.csoport}")
print(f"{diak_02.vnev} {diak_02.knev} {diak_02.osztaly} {diak_02.csoport}")
print(f"{diak_03.vnev} {diak_03.knev} {diak_03.osztaly} {diak_03.csoport}")

print(diak_01.bemutatkozas())
print(diak_02.bemutatkozas())
print(f"{diak_01.bemutatkozas()} {diak_01.kerdes()}")


diak01_valasza=int(input())
print(diak01_valasza)

if diak01_valasza==Diak.szam_01+Diak.szam_02:
    print("Helyes válasz")

else:
    print("Helytelen válasz")