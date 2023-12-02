#fhazi_feladat_027
#Készíts egy programot, amely [1; 40] intervallumon kiírja a 3-mal osztható számokat!

Szamok=range(1,40)
for x in Szamok:
    if x%3==0:
        print(x)