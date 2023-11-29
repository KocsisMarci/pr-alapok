sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        if oszlop==2 and 9>=sor>=2 or oszlop==9 and 9>=sor>=2 or sor+oszlop==11 and 6<=oszlop<=9 or sor==5 and oszlop==5 or sor==oszlop and 2<=sor<=4 and 2<=oszlop<=4:
            print("O ",end="")
        else:
            print(". ",end="")   
        #print(f"({sor+oszlop:3}) ",end="")
        oszlop+=1
    print("")
    sor+=1    