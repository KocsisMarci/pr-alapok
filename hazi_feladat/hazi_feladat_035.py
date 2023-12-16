#hazi_feladat_035
"""


"""
Színek=["Piros", "Kék", "Sárga", "Zöld"]

Szín=input("Adj meg egy színt, nagy kezdőbetűvel: ")

if Szín in Színek:
    print(f"Az általad megadott szín: {Szín}, szerepel a listában")
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))

else:
    print(f"Az általad  megadott szín: {Szín}, nem szerepel a listában, de hozzáadjuk ")
    Színek.append(Szín)
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))
