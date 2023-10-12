#Kocsis Marcell 10.D 1.csoport
#szamonkeres_001.py
"""
Bekérek egy osztályzatot, 1-5, 
irassuk ki a megadott jegyet értékkel és szövegesen
ha nem megfelelő jegyet adtam, akkor írja ki, a jegy értékét és 
melllé azt a szöveget, hogy nem megfelelő jegy.
"""
jegy = input("Írd be a jegyedet: ")
jegy = int(jegy)
if jegy == 1:
    print(f"A jegyed {jegy}, ez elégtelen")

elif jegy == 2:
    print(f"A jegyed {jegy}, ez elégséges")
elif jegy == 3:
    print(f"A jegyed {jegy}, ez közepes")
elif jegy == 4:
    print(f"A jegyed {jegy}, ez jó")
elif jegy == 5:
    print(f"A jegyed {jegy}, ez jeles")

else:
    print(f"{jegy} nem megfelelő jegy")    