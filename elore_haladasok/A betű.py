sor=1
while sor<=10:
    oszlop=1
    while oszlop<=11:
        if sor+oszlop==11 and oszlop<=6 or (sor+oszlop)%2!=0 and oszlop>sor and sor>=6 or sor==6 and oszlop==5:
            print("x ", end="")
        elif sor==6 and oszlop==9 or sor==6 and oszlop==11 or sor==10 and oszlop==10 or sor==8 and oszlop==10:
            print(". ",end="")
        else:
            print(". ", end="")    
        #print(f"({sor+oszlop:2}) ",end="")
        oszlop+=1
    print("")
    sor+=1    