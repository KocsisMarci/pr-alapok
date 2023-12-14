class HatarError(Exception):
    """
    Ügyel arra, hogy 1 és 45 között lehessen megadni csak értéket
    """

class MarvoltError(Exception):
    '''
    Ügyel arra, hogy egy érték ne szereplhessen több alkalommal
    '''    
import random
szam1=random.randint(1,45)
szam2=random.randint(1,45)
szam3=random.randint(1,45)
szam4=random.randint(1,45)
szam5=random.randint(1,45)
Nyero_szamok=[szam1,szam2,szam3,szam4,szam5]
Tippek=[]
def vizsgal(szam):
    if 1<=szam<=45 and szam not in Tippek:
        return szam

    elif szam in Tippek:
        raise MarvoltError(f"Ismétlődési hiba")
    
    
    else:

        raise HatarError(f"Határ hiba")

while len(Tippek)!=5:
    try:
        szam=vizsgal(int(input("Adj meg egy számot 1 és 45 között: ")))
        Tippek.append(szam)
    
    except ValueError as e:
        print(e)
        print("Nem számot adtál meg ")

    except HatarError as gond:
        print(gond) 
        print("1 és 45 közötti értéket, kell ,hogy megadj")       

    except MarvoltError as gond2:
        print(gond2)
        print(f"Az alábbi számot: {szam}, már megadtad, adj meg másik értéket")


    
    
    
    
if len(Tippek)==5:
    index=1
    print("A nyerő számok:") 
    for index in range(len(Nyero_szamok)):
            print(f"A(z) {index}. nyerőszám: {Nyero_szamok[index]}")
            index+=1
    print("_________________________________")
    print("A te számaid:")

for x, szam in enumerate(Nyero_szamok):
        print(f"{x}.{szam}")    


    
