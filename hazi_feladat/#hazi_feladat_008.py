szam=int(input("Írj be egy számot: "))
if szam%2==0 and szam>0:
    print(f"A megadott szám, {szam} pozitv páros")
elif szam%2!=0 and szam<0:
    print(f"A megadott szám, {szam} negatív páratlan")    