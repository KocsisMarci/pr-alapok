#hazi_feladat_033
"""
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. 
A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!
"""
Színek=["Piros", "Kék", "Sárga", "Zöld", "Kék"]

Szín=input("Adj meg egy színt, nagy kezdőbetűvel: ")

if Szín in Színek:
    print(f"Az általad megadott szín: {Szín} , szerepel a listában")
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))

else:
    print(f"A megadott szín,  nem szerepel a listában ")
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))
