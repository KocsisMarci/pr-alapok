sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        if oszlop==2 and 2<=sor<=9 or sor==2 and 2<=oszlop<=8 or oszlop==9 and 3<=sor<=4 or sor==5 and 2<=oszlop<=8:
            print("O ",end=" ")
        else:
            print(". ",end=" ")
        #print(f"({sor+oszlop:3}) ",end=" ")
        oszlop+=1
    print("")
    sor+=1   