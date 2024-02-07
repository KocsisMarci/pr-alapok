"""
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA estében azt vizsglájuk, hogy meliyk a legkisebb,
illetve a legnagyobb értké az adatsorban (itt a listában)
"""

lista=[12, 5, 4, 8, 9, 11, 10, 15, 6]

min=lista[0]
max=lista[0]

for szam in lista:
    if szam<min:
        min = szam
    
    if szam>max:
        max = szam    

print("A legkisebb szám a listában: ", min)
print(f"A legnagyobb szám a listában: {max} " )

# ------------------------------------------

#Alakítsd át a programot függvénnyé!


lista=[12, 5, 4, 8, 9, 11, 10, 15, 6]

min=lista[0]
max=lista[0]

for szam in lista:
    if szam<min:
        min = szam
    
    if szam>max:
        max = szam    

print("A legkisebb szám a listában: ", min)
print(f"A legnagyobb szám a listában: {max} ")
# -----------------------------------------------
#Alakítsd át a programot függvénnyé!
print("")
print("------------------------------------------")
print("")

lista=[12, 5, 3, 8, 9, 11, 10, 16, 6]
min1=lista[0]

def maximum(list):
    max1 =list[0]
    for szam in list:
        if szam>max1:
            max1 = szam
    return max1        

print(f"A lista legnagyobb eleme: {maximum(lista)}")


def minimum(list):
    min1=list[0]
    for szam in list:
        if szam<min1:
            min1=szam

    return min1

print(f"A lista legkisebb eleme: {minimum(lista)} ")            


#A lista legnagyobb  és legkisebbb eleme közötti különbség
lista=[12, 5, 3, 8, 9, 11, 10, 16, 6]
print(f"A lista_max és a lista_3_min különbsége: {maximum(lista)-minimum(lista)} ")

#---------------------------------------------------------
#osszeg függvény 


def osszeg(lista):
    osszeg=0
    for szam in lista:
        osszeg+=szam
    return osszeg    
lista5=[12, 5, 2, 8, 9, 11, 10, 16, 6]

print(f"A lista5 lista elemeinek az összege: {osszeg(lista)}")
