sor=1
while sor <=11:
    oszlop=1
    while oszlop<=11:
        if sor==2 or oszlop==6 and sor>=2:
            print("X ",end="")
        else:
            print(". ",end="")    
        #print(f"({sor+oszlop:2}) ",end="")
        oszlop+=1
    print("")
    sor+=1    