
"""
#gyakorlás

hőmérséklet=int(input("Add meg a hőmérsékletedet: "))



if 35<=hőmérséklet<37:
    print('Normális')

elif 38>hőmérséklet>=37:
    print("Hőemelkedés")

elif 40>hőmérséklet>=38:
    print("Lázas")

elif hőmérséklet>=40:
    print("Korház")

else:
    print("ORVOST!")

"""

hőmérséklet=float(input("Add meg a hőmérsékletedet: "))


def vizsgal(hőmérséklet):
    if 35<=hőmérséklet<37:
            print('Normális')

    elif 38>hőmérséklet>=37:
            print("Hőemelkedés")

    elif 40>hőmérséklet>=38:
            print("Lázas")

    elif hőmérséklet>=40:
            print("Korház")
    else:
            print("ORVOST!")


vizsgal(hőmérséklet)

