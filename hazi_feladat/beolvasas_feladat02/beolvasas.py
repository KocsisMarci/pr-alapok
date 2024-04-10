"""
A mellékelt fájl Rainer Maria Rilke: A párduc című versét tartalmazza Szabó Lőrinc fordításában (forrás: Magyar Elektronikus Könyvtár).
Az általad írt program olvassa be a fájl tartalmát a read() metódussal, és adja meg a válaszokat az alábbi kérdésekre:
- hány betűt tartalmaz a vers,
- hány magánhangzót tartalmaz a vers,
- hány szó fordul elő a versben?
"""

with open("forras.txt","r",encoding="utf-8") as vers:
    vers=vers.read()
    maganhngzok=['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű', 'A', 'Á', 'E', 'É', 'I', 'Í', 'O', 'Ó', 'Ö', 'Ő', 'U', 'Ú', 'Ü', 'Ű']
    betuk_szama=0
    maganhngzok_szama=0
    szavak_szama=0
    szavak_szama=szavak_szama-1
    for betu in vers:
            betuk_szama+=1
            if betu in maganhngzok:
                  maganhngzok_szama+=1
            
            if betu==" ":
                  szavak_szama+=1
                  
    
    print("A költemény: ")
    print(f"Ennyi betűt tartalmaz: {betuk_szama}")
    print(f"Ennyi magánhangzót tartalmaz: {maganhngzok_szama}")
    print(f"Ennyi szót tartalmaz: {szavak_szama}")