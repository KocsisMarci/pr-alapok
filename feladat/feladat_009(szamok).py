# feladat_009
"""
Kérjünk be két egész számot, szám1 és szám1.
Hasonlítsuk össze a két számot, és irassuk ki, hogy a szám1 kisebb mint a szám2,  vagy a szám 2 kisebb mint a szám 1, vagy a szám1 egyelő a szám 2-vel
"""

szám1=input("Írj be egy számot: ")
szám2=input("Írj be mégegy számot: ")
szám1=int(szám1)
szám2=int(szám2)

if szám1>szám2:
    print(f"A {szám1} nagyobb , mint a {szám2} ")
elif szám1<szám2 :
    print(f"A {szám2} nagyobb, mint a {szám1}")
else:
    print(f"A {szám1} egyelő a {szám2} számmal")   