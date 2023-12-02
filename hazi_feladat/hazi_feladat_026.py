#hazi_feladat_026
'''
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában. 
A végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista.
'''

neggyel=[]
import random
szam1=random.randint(0,50)
if szam1%4==0:
    neggyel.append(szam1)
szam2=random.randint(0,50)
if szam2%4==0:
    neggyel.append(szam2)
szam3=random.randint(0,50)
if szam3%4==0:
    neggyel.append(szam3)
szam4=random.randint(0,50)
if szam4%4==0:
    neggyel.append(szam4)
szam5=random.randint(0,50)
if szam5%4==0:
    neggyel.append(szam5)
szam6=random.randint(0,50)
if szam6%4==0:
    neggyel.append(szam6)
szam7=random.randint(0,50)
if szam7%4==0:
    neggyel.append(szam7)
szam8=random.randint(0,50)
if szam8%4==0:
    neggyel.append(szam8)
szam9=random.randint(0,50)
if szam9%4==0:
    neggyel.append(szam9)
szam10=random.randint(0,50)
if szam10%4==0:
    neggyel.append(szam10)
print(f"Azok a számok amellyek oszthatóak néggyel: {neggyel}")
print(f"Az előbb kiírt lista hossza: {len(neggyel)}")