#feladat_037
#Listák bővítése


nyelvek = ['Python', 'C', 'C++', 'Java']

# a lista végére hozzáfűz egy elemet
nyelvek.append('Python')

# a listát másolja
nyelvek_masolat = nyelvek.copy()

# a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)

# adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')     

