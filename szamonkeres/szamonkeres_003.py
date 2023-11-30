#Kocsis Marcell 10.D 2023.11.30
#Sorszám:8
#2. Feladart (páros)

"""
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását
(fej vagy íreás) , majd adjon tájékoztatást, hogy eltalálta-e!"
"""
import random
micsoda=random.randint(1,2)
lepes=None
while lepes!="fej" or lepes!="írás":
    lepes=input("Fej vagy írás? Kis betűvel írd be! ")
    if lepes=="fej" or lepes=="írás":
        break

if micsoda==1:
    micsoda="fej"

elif micsoda==2:
    micsoda="írás"

if lepes==micsoda:
    print(f"Eltalátad, te választottad:{lepes}, ez lett: {micsoda}")   
else:
    print(f"Nem találtad el, te választottad: {lepes}, ez lett: {micsoda}")     
 

