#hazi_feladat_004.py

"""
Készíts egy programot, amely megkérdezi a felhasználótól, hogy jó napja van-e!
A válasz kétféle lehet: igen vagy nem. A választól függően írjon ki üzenetet a gép!
"""

Válasz=input("Jó napod van? ")
if Válasz=="igen":
    print("Még több ilyet!")
elif Válasz=="nem":
    print("Kitartást")
    
"""
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó
nem a két lehetséges válasz (igen/nem) közül ad meg egyet, a gép kiírja: 
"Sajnos nem értem a válaszodat!"
"""
Válasz=input("Jó napod van? ")
if Válasz=="igen":
    print("Még több ilyet!")
elif Válasz=="nem":
    print("Kitartást")
else:
    print("Sajnos nem értem a válaszodat!")    