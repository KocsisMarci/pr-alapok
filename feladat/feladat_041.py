#feladat_041
szavak = ['lámpa', 'ablak', 'kutya', 'Attila', 'kukta']

for szo in szavak:
    print(szo)

for karakter in 'almafa':
    print(karakter)

for index, karakter in enumerate('almafa'):
    print(f'{index}. {karakter}')

for sorsz, karakter in enumerate('almafa', start=1):
    print(f'{sorsz}. {karakter}')

for _ in range(1, 5, 2):
    print('alma')
  