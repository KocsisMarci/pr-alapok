mondatok=[]

mondat=None
while mondat!="":

    mondat=input("Írj be egy mondatot mondatvégi írásjellel: ")
    if mondat!="":
        mondatok.append(mondat)

    if mondat=="":
        for eldont in mondatok:
                        if eldont[-1]==".":
                                    print(f"Az általad megadott mondat: {eldont} , egy kijelentő  mondat")
                        elif eldont[-1]=="?":
                            print(f"Az általad megadott mondat: {eldont} , egy kérdő mondat")
                        elif eldont[-1]=="!":
                            print(f"Az általad megadott mondat: {eldont} , egy felkiáltó/felszólító/óhajtó mondat")
                        else:
                               print(f"Az általad megodtt mondatról: {eldont} , nem tudom eldöntenti, hogy milyen mondat")    