
def szamolo(a, b, c=100):
    """
    c alapértelmezett értéke: 100
    """
    return (a+b)*c


# alapértelmezett paraméter használata
print(szamolo(1, 7))

# alapértelmezett paraméter felülírása
print(szamolo(1, 7, 10000))

# név szerinti paraméter átadás
print(szamolo(c=10000, a=1, b=7))

