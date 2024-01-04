
import random

milyen=random.randint(1,2)

if milyen==1:
    milyen="Fej"
else:
    milyen="Írás"


lepes=None

while lepes!="Fej" or lepes!="Írás":
    if lepes=="fej" or lepes=="írás":
        lepes=input("Nagybetűvel írd: ")
    else:
        lepes=input("Fej, vagy írás nagybetűvel: ")

    if lepes=="Fej" or lepes=="Írás":
        break 



if lepes==milyen:
    print(f"Te választottad: {lepes}, ez lett: {milyen}, győztél")

else:
    print(f"Te választottad: {lepes}, ez lett: {milyen}, vesztettél")



