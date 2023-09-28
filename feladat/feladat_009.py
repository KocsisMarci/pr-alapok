#feladat_009
"""
Ez a program a sebesség alapján eldönti, hogy mennyivel ment a sofőr, és ha büntetés jár neki, akkor mennyi, valamint a büntetőpontokat is számolja
A forrásom: https://kalkulatorlap.hu/gyorshajtas_buntetes_kalkulator.html
"""
buntetopont=0
birsag=0
sebesség=int(input("Add meg a sebessségedet 0-tól 447-ig "))
while sebesség>447:
    sebesség=int(input("Az általad beírt eredmény nem reális, adj meg egy reálisat: "))

if sebesség==0:
    print("Egy helyben álsz")
elif 0<sebesség<=50:
       print(f"Megengedet sebeséggel mentél, {sebesség} km/h-val")

elif 50<sebesség<=65:
    print(f"Nem kapsz büntetést, sem büntetőpontot de vigyázzál mert, {sebesség} km/h-val mentél")
elif 65<sebesség<=75:
    buntetopont+=4
    birsag+=39000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont} db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 75<sebesség<=85:
    buntetopont+=4
    birsag+=58500
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 85<sebesség<=95:
    buntetopont+=4
    birsag+=78000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 95<sebesség<=105:
    buntetopont+=6
    birsag+=117000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 105<sebesség<=115:
    buntetopont+=6
    birsag+=169000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 115<sebesség<=125:
    buntetopont+=8
    birsag+=260000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél")
elif 125<sebesség<=447:
    buntetopont+=8
    birsag+=390000
    print(f"A büntetésed {birsag} Ft, ezért {buntetopont}  db büntetőpontot kapsz, {sebesség} km/h-val mentél ")    
    
print("__________________________________________")


if buntetopont==0 and birsag==0:
    print("Nem követtél el szabálytalanságot")
else:
    print(f"{buntetopont} db büntetőpontot értél el, a pénzbírságod pedig: {birsag} Ft")   
    