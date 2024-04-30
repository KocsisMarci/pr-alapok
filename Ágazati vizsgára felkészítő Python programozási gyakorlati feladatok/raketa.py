mennyit=int(input("Hány órás visszaszámlálást tervezünk? "))
print(f"Visszaszámlálás: {mennyit}")

ennyit_kell=mennyit
felfuggesztett_orak=0
while ennyit_kell!=0:
    kell_e=input(f"Fel kell függeszteni a visszaszámlálást (i/n)? ")
    ennyit_kell-=1
    print(f"Visszaszámlálás: {ennyit_kell}")
    if  kell_e=="i":
        felfuggesztett_orak+=1

if ennyit_kell==0:
    teljes_ido=mennyit+felfuggesztett_orak
    print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {teljes_ido} ")
