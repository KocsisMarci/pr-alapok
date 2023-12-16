Betuk=[]
Betu=None

while Betu!="":
    Betu=input("Adj meg egy betűt: ")
    if Betu  in Betuk:
             print("Ezt a betűt már rögzítettem")    
             print(Betuk.sort())    
    elif Betu not in Betuk and Betu!="":
         Betuk.append(Betu)
         print(sorted(Betuk))    

if Betu=="":

    print(f"A betűk: {sorted(Betuk)}")   