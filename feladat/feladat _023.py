#feladat_023
honapok=[] #üres lista
print(honapok)
honapok = ['január', 'február','március', 'április']

# lista kiíratása
print(honapok)

# join(): a lista elemeit egy sztringgé fűzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(honapok))

# lista hossza: len( )
print(len(honapok))

# a 0. indexű az első elem
print(honapok[0])

# jelen esetben a 3. indexű az utolsó elem
print(honapok[3])

# túlindexelés, hibát okoz!
# ebben a listában az utolsó elem indexe: 3
# print(honapok[4]) <- HIBÁS!!!

# az 1-es és 2-es indexű elemek kiíratása
print(honapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2-es indexű elemtől a végéig
print(honapok[2:])

#vagy: 
print(honapok[2:len(honapok)])  

# hátulról az első, vagyis az utolsó elem
print(honapok[-1])      
print("---------------------------------------------")
print()


# hátulról a második, vagyis az utolsó előtti elem
print(honapok[-2])      
print("---------------------------------------------")
print()