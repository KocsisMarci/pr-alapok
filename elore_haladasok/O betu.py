sor=1
while sor<=10:
    oszlop=1
    while oszlop<=10:
     if sor==2 and 3<=oszlop<=8 or oszlop==2 and 3<=sor<=8 and sor==9 :
        print("O ",end=" ")
     else:
        print(". ",end=" ")
        #print(f"({sor+oszlop:3}) ",end="")
     oszlop+=1
    print("")  
    sor+=1
