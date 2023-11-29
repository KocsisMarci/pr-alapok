sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
        if oszlop==2 and sor>=3 or (sor+oszlop)%2==0 and sor==oszlop and sor>=3 or oszlop==10 and sor>=3:
            print("O ",end="")
        else:
            print(". ",end="")
        #print(f"({sor+oszlop:5}) ",end="")
        oszlop+=1
    print("")
    sor+=1    