import random 
gep_szam=random.randint(1,3)
felhasznalo_szam=int(input("Írj be egy számot 1 és 3 között "))
while felhasznalo_szam>3 or felhasznalo_szam<1:
    felhasznalo_szam=int(input("Mondom 1 és 3 között: "))

if gep_szam < felhasznalo_szam:
    print(f" Az általad megadott szám, ({felhasznalo_szam}) nagyobb a gép számánál ({gep_szam})")
elif gep_szam > felhasznalo_szam:
    print(f"Az általad megadott szám, ({felhasznalo_szam}) kisebb a gép számánál ({gep_szam})")
elif gep_szam == felhasznalo_szam:
    print(f"Az általad megadott szám, ({felhasznalo_szam}) egyelő a gép számával ({gep_szam})")