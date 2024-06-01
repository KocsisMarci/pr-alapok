"""
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban!
Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
"""

szo="programozás"



eleg=False

while eleg!=True:
    betu=input("Adj meg egy betűt amiről úgy gondolod, hogy a tárolt szóban van: ")
    if len(betu)==1:
        eleg=True


if betu in szo:
    print(f"Az általad megadott betű: {betu}, szerepel a szóban")

else:
    print(f"Az általad megadott betű: {betu}, nem szerepel a szóban")



print(f"A tárolt szó: {szo}")
