import random
szakaszok=[]
meredekek=[]
meredekek_visszafele=[]
while len(szakaszok)!=30:
    szakasz=random.randint(1,9)
    szakaszok.append(szakasz)

if len(szakaszok)==30:
    for index, szakasz in enumerate(szakaszok):
        if szakasz>= szakaszok[index-1]+2:
                meredekek.append(szakasz)
        if szakasz<= szakaszok[index-1]+2:
                meredekek_visszafele.append(szakasz)


print(f"Ennyi meredek van az úton odafele: {len(meredekek)}")
print(f"Ennyi meredek van az úton visszafele: {len(meredekek_visszafele)} ")
print("_____________________________")
print("")
print("Odafele: ")
print(meredekek)
print("")
print("Visszafele: ")
print(meredekek_visszafele)
print("")
print("_____________________________")
print("")
print(f"Amúgy, ezek a szakaszok: {szakaszok}")