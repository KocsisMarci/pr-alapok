konnyu_szavak=["munka","könyv","autó","tudás","kép"]
kozepes_szavak=["programozás","relaxáció","kötelesség","esemény","tapasztalat"]
nehez_szavak=["képernyőkép","játékkiadó","fájlkezelő","intelligencia","algoritmizálás"]
lehetsegek_tippek=['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'ö', 'ő', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ü', 'ű', 'v', 'w', 'x', 'y', 'z']


class HosszError(Exception):
     pass

class TippError(Exception):
     pass

class IsmetlodesError(Exception):
     pass

jo_tippek=[]
rossz_tippek=[]
def tippetvizsgal(tipp):
        if len(tipp)!=1:
             raise HosszError("Hibás hossz")
    
        if tipp not in lehetsegek_tippek:
             raise TippError("Hibás tipp")
        
        elif tipp in jo_tippek or tipp in rossz_tippek:
             raise IsmetlodesError("Ismétlődés")
        
        else:
             return tipp
def main():
    jo_tippek.clear()
    rossz_tippek.clear()
    szotgeneral()


def szotgeneral():

    import random

    joszonehezseg=False
    while not joszonehezseg:
          szonehezseg=input("Milyen nehéz szót akarsz kitalálni? Könnyű[KŰ], közepes[KS], nehéz[NZ]? ")
          if szonehezseg=="KŰ" or szonehezseg=="KS" or szonehezseg=="NZ":
                    joszonehezseg=True
     
    if szonehezseg=="KŰ":
          kitalalando=konnyu_szavak[random.randint(0,4)]

    elif szonehezseg=="KS":
         kitalalando=kozepes_szavak[random.randint(0,4)]

    else:
          kitalalando=nehez_szavak[random.randint(0,4)]

    kitalalando_betukszama=len(kitalalando)
    


    beker(kitalalando_betukszama,kitalalando)

def beker(kitalando_betukszama,kitalalando):
    kiiro=[]
    kitalalandok=[]
    akasztva=False
    kitalalva=False
    eleg=False
    joakasztasig=False
    while not joakasztasig:
     akasztasig=int(input("Mennyi legyen az akasztásig? "))
     if akasztasig>0 and type(akasztasig)==int:
          joakasztasig=True
    for betu in kitalalando:
        kiiro.append("_")
        kitalalandok.append(betu)
    while not eleg:
        print(" ".join(kiiro))
        try:
            print("")
            print("Ennyi van akasztásig: ")
            print(akasztasig)


            tipp=tippetvizsgal(input("Adj meg egy betűt amiről, úgy gondolod, hogy benne lehet a szóban (csak kis betűk jöhetnek szóba): "))
          
            if tipp in kitalalandok:
                 hozzaadva=0
                 mennyiszer=0

                 for keres in kitalalandok:
                        if keres==tipp:
                             mennyiszer+=1
                        
                 while hozzaadva!=mennyiszer:
                    jo_tippek.append(tipp)
                    hozzaadva+=1
                 
                 for index,keres in enumerate(kitalalandok):
                        if keres==tipp:
                             kiiro[index]=kitalalandok[index]
                
            else:
                 rossz_tippek.append(tipp)
                 akasztasig-=1

        except ValueError as hiba:
             print(hiba)
             
             print("")
             print("_________________________________________________")
             print("Számot kell, hogy megadj")
             print("_________________________________________________")
             print("")

             print("Nem számít érvényes tippnek")

            
        except HosszError as hiba:
             print(hiba)
             print("")
             print("_________________________________________________")
             print("Betűt kell megadnod, tehát egy karaktert")
             print("_________________________________________________")
             print("")

             print("Nem számít érvényes tippnek")

            
        except TippError as hiba:
             print(hiba)
             print("")

             print("_________________________________________________")
             print("Az általad megadott tipp nem tippelhető")
             print("_________________________________________________")
             print("")

             print("Nem számít érvényes tippnek")
    
        
        except IsmetlodesError as hiba:
             print(hiba)
             print("")
             print("_________________________________________________")
             print("Ezt a betűt már tippelted")
             print("_________________________________________________")
             print("")

             print("Nem számít érvényes tippnek")
    

        if akasztasig==0:
             print("Sajnos, felakasztottuk az illetőt")
             print("A kitalálandó szó ez volt:", kitalalando)

          
             eleg=True



        if len(jo_tippek)==len(kitalalando):
             print("Gratulálok megmentetted az illetőt ")
             eleg=True

    
    ertekelhetovalasz=False
    while not ertekelhetovalasz:
        ujkor=input("Akarsz új kört játszani I/N? ")
        if ujkor=="I":
             main()
             ertekelhetovalasz=True
            
        elif ujkor=="N":
             print("Ezesetben köszönöm a játékot")
             ertekelhetovalasz=True
            

main()