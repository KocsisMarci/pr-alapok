#hazi_feladat_002.py
"""
Készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!
"""
r= int(input("Add meg a kör sugarát, cm-ben: "))
kerulet=2*r*3.14
terulet=r**2*3.14
#másik megoldás a területre: terulet=(r*r)*3.14
print(f"A kör kerülete:{kerulet} centiméter ")
print(f"A kör kerülete:{terulet} négyzetcentiméter ")