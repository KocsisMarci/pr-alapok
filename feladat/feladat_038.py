#feladat_038
nyelvek = ['Python', 'C', 'C++', 'Java']

# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
torolt_nyelv = nyelvek.pop()

# eltávolítja a megadott indexű elemet,  és azzal tér vissza
nyelvek.pop(1)

# eltávolítja a megadott indexű elemet
del nyelvek[1]

# eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')

# törli a listát
nyelvek.clear()
