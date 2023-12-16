import random
szam1=random.randint(1,3)
szam2=random.randint(1,3)
szam3=random.randint(1,3)
szam4=random.randint(1,3)
szam5=random.randint(1,3)
szam6=random.randint(1,3)
szam7=random.randint(1,3)
szam8=random.randint(1,3)
szam9=random.randint(1,3)
szam10=random.randint(1,3)

Számok=[szam1, szam2, szam3, szam4, szam5, szam6, szam7, szam8, szam9, szam10]

print(Számok)
törlendő=int(input("Melyik számot távolítsam el? "))
for törölhető in Számok:
    if törölhető==törlendő:
            Számok.remove(törölhető)
print(Számok)
