szam=int(input("Írj be egy számot: "))
if szam%3==0 and szam%4!=0:
    print("csak 3-mal osztható")
elif szam%3!=0 and szam%4==0:
    print("csak 4-el osztható") 
elif szam%3==0 and szam%4==0:
    print("3-mal, és 4-el is otható")
else:
    print("sem 3-mal, sem 4-el nem osztható")           