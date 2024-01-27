#feladat_046

# eldöntés    
szavak = ['lámpa', 'xablak', 'kutya', 'Attila', 'kukta']

index = 0
while index < len(szavak):
    print(szavak[index])
    if szavak[index][0] == 'a':
        print('Van "a" betűvel kezdődő szó!')
        break
    index += 1
else:
    print('Nincs ilyen szó!')
  