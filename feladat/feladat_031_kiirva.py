#feladat_031

honapok=["Január","Február","Március","Április","Május","Június"]
for index in range(len(honapok)):

        # az eredeti listaemlem módosul!
        print(f"{index}. {honapok[index]}",)
        honapok[index]=honapok[index].upper()
        print(f"{index}. {honapok[index]}")
