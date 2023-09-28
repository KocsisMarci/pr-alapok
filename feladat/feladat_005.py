# feladat_005
# dk9 104-oldal
"""
Amikor karakterlánccá alakítunk, az str utasításra van szükség.
"""
felhasználó_kora = 16
print(f"A felhasználó_kora változó típusa: {type(felhasználó_kora)}")
felhasználó_kora = str(felhasználó_kora)
print(f"A felhasználó_kora változó típusa: {type(felhasználó_kora)}")
ilyen = input('És milyen ' + felhasználó_kora + ' évesnek lenni? ')
olyan = input(f'És milyen {felhasználó_kora} évesnek lenni? ')