#Az összegzés tétele
#osszeg függvény 
def osszeg(lista):
    osszeg=0
    for szam in lista:
        osszeg+=szam
    
    return osszeg 

lista5=[12, 5, 2, 8, 9, 11, 10, 16, 6]

print(f"A lista5 lista elemeinek az összege: {osszeg(lista5)}")
