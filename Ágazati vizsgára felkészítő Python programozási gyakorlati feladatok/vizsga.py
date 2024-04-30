

def eldont(pont):
    if pont>=48:
        return True
    else:
        return False
nev=None
elert_pont=None

eleg=False

while eleg!=True:
    nev=input("Add meg a vizsgázó nevét! ")
    elert_pont=(input("Add meg a pontszámát! "))
    if elert_pont!="":
        elert_pont=int(elert_pont)
    if nev!="" and elert_pont!="":
        atment_e=eldont(elert_pont)
        if atment_e==True:
            print(f"{nev} vizsgája sikeres.")
        else:
            print(f"{nev} vizsgája sikertelen.")
    
    elif nev=="" and elert_pont=="":
        eleg=True