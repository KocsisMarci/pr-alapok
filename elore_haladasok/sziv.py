sor=1
while sor<=10:
    oszlop=1
    while oszlop<=11:
        
        if sor==10 and oszlop==6 or sor+oszlop==16 and oszlop<11 or sor==6 and oszlop<10 and oszlop>1 and oszlop!=5 and oszlop!=6 or sor==7 and oszlop==5 or sor==7 and oszlop==6 or  sor==10 and oszlop==5 or sor==9 and oszlop==4 or sor==8 and oszlop==3 or sor==7 and oszlop==2:
            print("O ",end="")
        else:
            print(". ",end="")
        
        #print(f"({sor+oszlop:3}) ",end="")
        oszlop+=1
    print("")
    sor+=1    