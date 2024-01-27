#feladat_042

# eldöntés    
szavak = ['lámpa', 'ablak', 'kutya', 'Attila', 'kukta']

for szo in szavak:
    print(szo)
    if szo[0] == 'a':
        print('Van "a" betűvel kezdődő szó!')
        break
else:
    print('Nincs ilyen szó!')  
  