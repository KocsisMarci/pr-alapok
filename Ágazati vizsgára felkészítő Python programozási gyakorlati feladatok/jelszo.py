
sikeres_bejelentkezes=False

while not sikeres_bejelentkezes:
        felhasznalonev=input("Adja meg a felhasználónevét! ")
        jelszo=input("Adja meg a jelszavát! ")
        if felhasznalonev=="bori99" and jelszo=="Szivecske<3":
                sikeres_bejelentkezes=True
        
        else:
                print("Belépés megtagadva.")

if sikeres_bejelentkezes:
        print("Belépés engedélyezve.")
                