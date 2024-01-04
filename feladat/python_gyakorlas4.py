nev=input("Adja meg a keresztnevét: ")
kor=int(input("Adja meg az életkorát: "))

if kor < 1:
    print("A kora alapján", nev, "cscsemő!")
elif kor < 6:
    print("A kora alapján", nev, "kissgyerek!")
elif kor < 12:
    print("A kora alapján", nev, "gyerek!")
elif kor < 16:
    print("A kora alapján", nev, "serdülő!")
elif kor < 25:
    print("A kora alapján", nev, "ifjú!")
elif kor < 65:
    print("A kora alapján", nev, "felnőtt!")
else:
    print("A kora alapján", nev , "nyugdíjas!")