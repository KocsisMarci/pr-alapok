sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        if oszlop==1 or sor==10:
            print("O ",end="")
        else:
            print(". ",end="")    
        #print(f"({sor+oszlop:2}) ",end="")
        oszlop+=1
    print("")
    sor+=1    