sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        if oszlop==1 or oszlop==10 or sor==5 and oszlop<=10 or sor==6 and oszlop<=10:
            print("x ",end="")
        else:
            print(". ",end="")
         #print(f"({sor+oszlop:2}) ",end="")
        oszlop+=1
    print("")
    sor+=1    