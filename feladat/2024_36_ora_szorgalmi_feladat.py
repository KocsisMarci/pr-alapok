import random
Filmek=["Piedone Afrikában","Red", "Zombieland", "Haláli Hullák Hajnala", "Holtak Hajnala (2004)"]
Fo_szereplok=["Rizzo","Frank", "Colombus", "Shaun","Anna"]

print(", ".join(Filmek))
szereplo_indexe=random.randint(0,4)

Kigondolt_szereplo=Fo_szereplok[szereplo_indexe]
print("")
tipp=input(f"Az alábbi szereplő: {Kigondolt_szereplo}, melyik film főszereplője, az előzőleg felsorolt filmek közül közül? ")

if Filmek[szereplo_indexe]==tipp:
    print(f"Gratulálok eltaláltad, {Kigondolt_szereplo} tényleg a {Filmek[szereplo_indexe]} filmben szerepelt")
else:
    print(f"Sajnálom, a kigondolt szereplő ({Kigondolt_szereplo}), a {Filmek[szereplo_indexe]} filmben szerepelt")