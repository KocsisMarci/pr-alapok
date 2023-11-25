#a 0 értéket a fej, az 1 értéket az írás képviseli
import random
szam=random.randint(0,1)
eredmeny=None
if szam==0:
    eredmeny="fej"
else:
    eredmeny="írás"
lepes=None
while lepes!="fej" or  lepes!="írás":
    lepes=input("Fej vagy írás?, Csak a kiskezdő betűt tudom értelmezni! ")
    if lepes=="fej" or lepes=="írás":
        break

if lepes==eredmeny: 
    print(f"Győztél, te választottad: {lepes}, ez lett: {eredmeny}")   
else:
    print(f"Vesztettél, te választottad: {lepes}, ez lett: {eredmeny}")    