#hazi_feladat_023
'''
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, 
írja ki az addig megadott neveket, és lépjen ki.

'''
Nevek=[]
Nev=None
Megadott=0
while Nev!="" or Megadott==3:
    Nev=input(f"Írj be egy keresztnevet: ")
    if Nev!="":
        Nevek.append(Nev)
        Megadott+=1

    if Nev=="":
      
        print(f"A nevek amellyeket beírtál: {Nevek}")    
    if Megadott==3:
        print(f"Több nevet nem adhatsz meg, az eddig megadotak: {Nevek}")    
        break