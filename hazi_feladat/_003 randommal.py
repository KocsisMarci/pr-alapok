#hazi_feladat_003.py
"""
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj
egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám
egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
"""

import random
gondolt_szam = random.randint(1, 5)
tipp = int(input("Írj be egy számot, lehetőleg 1 és 5 között: "))
if tipp == gondolt_szam:
     print(f"A te számod ({tipp}) egyelő a gép által gondolt számmal ({gondolt_szam})")
elif tipp < gondolt_szam:
    print(f"A te számod ({tipp}) kisebb a gép által gondolt számmal")
elif tipp > gondolt_szam:
    print(f"A te számod ({tipp}) nagyobb a gép által gondolt számnál")         
