class TípusError(Exception):
    """
    Ügyel arra, hogy csak szám kerüljön elfogásra, (az S kivétel)
    """

class HatarError(Exception):
    """
    Ügyel arra, hogy 1 és 10 közötti szám kerüjön elfogadásra csak
    """
def vizsgalat(tipp):
    
    if type(tipp)!=int:
        raise TípusError(f"Hibás tíups")
    
    elif type(tipp)==int and tipp>10 or tipp<1:
        raise HatarError(f"Hibás érték")
    
    else:
        return tipp

import modulka
import random
szamom=random.randint(1,10)
szam=modulka.random_szam(szamom)
szamok=[]
tippek_szam=0
segitseg_szam=0
lehetoseg=5
probaszam=0
Tippeltek=[]

while tippek_szam!=5 or tipp!=szam:
    try:
        tipp=vizsgalat(int(input(f"Gondoltam, egy számra 1 és 10 között próbáld meg, kitalálni. Hátralévő próbák száma: ({lehetoseg}): ")))
            
        if tipp!=szam:
                print("Nem jó a tipped ")
                
                if tipp not in Tippeltek:
                        lehetoseg-=1
                        probaszam+=1
                        Tippeltek.append(tipp)
                else:
                     print("Ezt a számot már tippelted, nem veszem érvényes tippnek")        
        elif tipp==szam:
                
                print(f"Gratulálok eltaláltad. A tipped: {tipp}, a megfejtés: {szam}, ennyi próbából: {probaszam}")
                probaszam+=1
                Tippeltek.append(tipp)

                kiirni_tippek=input("Szeretnéd látni a tippjeidet? I/N ")
                
                if kiirni_tippek=="I":
                     
                     for x in Tippeltek:
                          print(x)
                else:
                     print("Nem I-t írtál szóval, nem írom ki")          
                break
        if  lehetoseg==0:
                print(f"Sajnos, ennyi próbád volt, a megfejtés: {szam}")    
                
                kiirni_tippek=input("Szeretnéd látni a tippjeidet? I/N ")
                if kiirni_tippek=="I":
                     for x in Tippeltek:
                          print(x)
                else:
                     print("Nem I-t írtál szóval, nem írom ki")        
                break


    except HatarError:
            print("1 és 10 közötti számot kell, hogy megadj, ezt nem számítjuk, érvényes tippnek")

    except TípusError:
        print("Számot kell, hogy megadj, betűből egyedül csak S-t írhatsz be, a segítség miatt")