Szamok=[]
Intervallum_masikmegoldashoz=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
szam=0
while -5<=szam<=5:
    szam=int(input("Adj meg egy számot [-5;5] intervallumon: "))
    if -5<=szam<=5:
        Szamok.append(szam)


def osszegzes(Szamok):
    osszeg=0
    for szam in Szamok:
        osszeg+=szam

    print(f"Az általad megadott számok ,mellyek benne vannak az intervallumban: {Szamok}")  
    print("_______________________________________________________________________________")
    print(f"Ezeknek a számoknak az összege: {osszeg}")
    
    """
    Amit kért a feladat, szóval szerintem az alternatív megoldás is elfogadható: 
    A program írja ki a megadott intervallumba eső számokat és az összegüket!

    osszeg=0
    for szam in Intervallum_masikmegoldashoz:
        osszeg+=szam
    print(f"Az általad megadott számok ,mellyek benne vannak az intervallumban: {Intervallum_masikmegoldashoz}")  
    print("_______________________________________________________________________________")
    print(f"Ezeknek a számoknak az összege: {osszeg}")
    """


teszt=osszegzes(Szamok)