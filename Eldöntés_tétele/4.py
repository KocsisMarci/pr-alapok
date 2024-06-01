"""
A program kérjen be egy szöveget!

Határozza meg és írja ki a képernyőre, hogy
- az adott szövegben volt-e,
- ha igen akkor hány darab,
- és hányadik helyen / helyeken (a legelső hely az egyes számú)
”a”, ”e”, ”i” , ”o” vagy ”u” magánhangzó!

Mindegyik magánhangzóra külön-külön adja meg az információkat!
"""


a_szam=0
e_szam=0
i_szam=0
o_szam=0
u_szam=0

volt_a=False
volt_e=False
volt_i=False
volt_o=False
volt_u=False

a_helyek=[]
e_helyek=[]
i_helyek=[]
o_helyek=[]
u_helyek=[]



szoveg=input("Adj meg egy szöveget: ")


for index,betu in enumerate(szoveg):
    if betu=="a":
        a_szam+=1
        a_helyek.append(index+1)
        volt_a=True

    elif betu=="e":
        e_szam+=1
        e_helyek.append(index+1)
        volt_e=True
    elif betu=="i":
        i_szam+=1
        i_helyek.append(index+1)
        volt_i=True
    elif betu=="o":
        o_szam+=1
        o_helyek.append(index+1)
        volt_o=True
    elif betu=="u":
        u_szam+=1
        u_helyek.append(index+1)
        volt_u=True



print("a: ")
print(f"Volt betű: {volt_a} ")
if volt_a:
    print(f"Ennyi: {a_szam} ")
    if a_szam==1:
        print("Az alábbi helyen: ")
        print(a_helyek)
    else:
          print("Az alábbi helyeken: ")
          print(a_helyek)




print("")
print("")


print("e: ")
print(f"Volt betű: {volt_e} ")
if volt_e:
    print(f"Ennyi: {e_szam} ")
    if e_szam==1:
        print("Az alábbi helyen: ")
        print(e_helyek)
    else:
          print("Az alábbi helyeken: ")
          print(e_helyek)



print("")
print("")


print("i: ")
print(f"Volt betű: {volt_i} ")
if volt_i:
    print(f"Ennyi: {i_szam} ")
    if i_szam==1:
        print("Az alábbi helyen: ")
        print(i_helyek)
    else:
          print("Az alábbi helyeken: ")
          print(i_helyek)

print("")
print("")


print("o: ")
print(f"Volt betű: {volt_o} ")
if volt_o:
    print(f"Ennyi: {o_szam} ")
    if o_szam==1:
        print("Az alábbi helyen: ")
        print(o_helyek)
    else:
          print("Az alábbi helyeken: ")
          print(o_helyek)

print("")
print("")


print("u: ")
print(f"Volt betű: {volt_u} ")
if volt_u:
    print(f"Ennyi: {u_szam} ")
    if u_szam==1:
        print("Az alábbi helyen: ")
        print(u_helyek)
    else:
          print("Az alábbi helyeken: ")
          print(u_helyek)