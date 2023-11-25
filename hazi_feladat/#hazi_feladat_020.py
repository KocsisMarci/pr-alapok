sor=1
while sor<6:
    oszlop=1
    while oszlop<6:
        if (sor+oszlop)%2==0 and sor==oszlop:
            print(f"O ", end="")
        else:
            print(". ",end="")    
        oszlop+=1
    print("")
    sor+=1    