#hazi_feladat_022
'''
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! 
A program a bekért neveket írja ki a képernyőre!
'''

Nevek=[]
Nev=None
while Nev!="":
    Nev=input(f"Írj be egy keresztnevet: ")
    if Nev!="":
        Nevek.append(Nev)
    if Nev=="":
        print(f"A nevek amellyeket beírtál: {Nevek}")    