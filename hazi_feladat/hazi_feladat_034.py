#hazi_feladat_034
"""
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a felhasználó által megadott szín a listában! 
Ha a megadott szín nincs még tárolva, továbbra is a "A megadott szín nem szerepel a listában." szöveg jelenjen meg!

"""

Színek=["Piros", "Kék", "Sárga", "Zöld", "Kék"]

Szín=input("Adj meg egy színt, nagy kezdőbetűvel: ")

if Szín in Színek:
    print(f"Az általad megadott szín: {Szín}, {Színek.count(Szín)} alkalommal, szerepel a listában")
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))

else:
    print(f"Az  megadott szín, nem szerepel a listában ")
    print(f"A listában szereplő színek:")
    print(", ".join(Színek))
