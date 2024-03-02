'''
A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
hány darab van az adatsorban (itt a listában).

A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in lista:
        if szam % 3 == 0:
            darab = darab + 1

print('A listában lévő hárommal osztható számok száma: ', darab)  
