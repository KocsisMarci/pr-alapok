szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
evagyEvalkezdonek=[]


def kivalaszt(szavak):
    for keres in szavak:

        if keres[0]=="e" or keres[0]=="E":
            evagyEvalkezdonek.append(keres)

    print(f"Ennyi e vagy E betűvel kezdődő szó van, a listában: {len(evagyEvalkezdonek)}")
    print("______________________________________________________________________________")
    print(f"Ezek a szavak pedig: {evagyEvalkezdonek}") 



tesz=kivalaszt(szavak)