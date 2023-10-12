#hazi_feladat_003.py
"""
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj
egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám
egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
"""

gondolt_szam = 3
tipp = int(input("Írj be egy számot, lehetőleg 1 és 5 között: "))
if tipp == gondolt_szam:
     print(f"A te számod egyelő a gép által gondolt számmal")
elif tipp < gondolt_szam:
    print(f"A te számod kisebb a gép által gondolt számmal")
elif tipp > gondolt_szam:
    print(f"A te számod nagyobb a gép által gondolt számnál")         
