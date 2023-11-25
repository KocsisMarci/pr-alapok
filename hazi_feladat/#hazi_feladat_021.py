sor=1
while sor<8:
    oszlop=1
    while oszlop<8:
        if sor+oszlop==8 or (sor+oszlop)%2==0 and sor==oszlop:
            print("O ",end="")
        else:
            print(". ",end="")    
        oszlop+=1
    print("")
    sor+=1    