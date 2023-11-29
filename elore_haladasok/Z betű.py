sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        
        if sor==1 and oszlop>1 and oszlop<10 or sor+oszlop==10 and oszlop>1 or sor==8 and oszlop>=2 and oszlop<10:
            print("O ",end="")
        else:
            print(". ",end="")
        
        #print(f"({sor+oszlop:2}) ",end="")
        oszlop+=1
    print("")
    sor+=1    