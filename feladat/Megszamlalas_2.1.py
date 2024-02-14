szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
avagyAvalkezdonek=[]


def kivalaszt(szavak):
    for keres in szavak:

        if keres[0]=="a" or keres[0]=="A":
            avagyAvalkezdonek.append(keres)

    print(f"Ennyi a vagy A betűvel kezdődő szó van, a listában: {len(avagyAvalkezdonek)}")
    print("______________________________________________________________________________")
    print(f"Ezek a szavak pedig: {avagyAvalkezdonek}")    



tesz=kivalaszt(szavak)