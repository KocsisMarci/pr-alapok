import random
szamok_elsofel=random.sample(range(1,13),10)
szamok_masodikfel=random.sample(range(1,13),10)

mennyi=0
for vizsgalat in szamok_elsofel:

        if vizsgalat%3==0:
            print(vizsgalat)
            mennyi+=1

for vizsgalat in szamok_masodikfel:
      if vizsgalat%3==0:
            print(vizsgalat)
            mennyi+=1


print(f"Összesen {mennyi} db szám volt osztható 3-al")        















