
mondat=None
while mondat!="":
    mondat=input("Írj be egy mondatot mondatvégi írásjellel: ")
    if mondat!="":
        if mondat[-1]==".":
            print(f"Az általad megadott mondat: {mondat} , egy kijelentő mondat")
        elif mondat[-1]=="?":
            print(f"Az általad megadott mondat: {mondat} , egy kérdő mondat")
        elif mondat[-1]=="!":
                    print(f"Az általad megadott mondat: {mondat} , felkiáltó/felszólító/óhajtó egy mondat")
        else:
            print(f"Az általad megadott mondatról: {mondat} , nem tudom eldönteni ,hogy milyen mondat")

    if mondat=="":
          print(f"Program vége")                     