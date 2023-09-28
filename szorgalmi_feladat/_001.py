#szorgalmi_001
"""
Ez a program megpróbálja eldönteni a mondat, mondatvégi írásjele alapján, a mondat modalitását:
"""
mondat=input("Adj meg egy mondatot, mondatvégi írásjellel: ")

if mondat[-1]==".":
    print("A mondat amit beírtal, az egy kijelentő mondat")
elif mondat[-1]=="?":
        print("A mondat amit beírtál,az egy kérdő mondat.") 
elif mondat[-1]=="!":
    print("A mondat amit beírtál, az vagy felkiáltó, vagy felszólító, vagy óhajtó mondat lehet!")
elif "Bárcsak" or "bárcsak" in  mondat:
    print("A mondat amit beírtál, az egy óhajtó mondat!")        
else:
    print("Nem észleletem modndatvégi írásjelet, próbáld újra")
    mondat=input("Adj meg egy mondatot, mondatvégi írásjellel: ") 