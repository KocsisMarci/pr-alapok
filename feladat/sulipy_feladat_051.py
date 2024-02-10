
# Függvény definíciója
def festek_kalkulator(x, y):
    """
    Kiszámolja az adott falfelület festéséhez
    szükséges festék mennyiségét
    """
    t = x * y
    l = t * 0.13
    return l


# Függvény hívása
liter = festek_kalkulator(5, 2)

# A függvény hívása lehet egy kifejezés része is
ar = festek_kalkulator(5, 2) * 700

