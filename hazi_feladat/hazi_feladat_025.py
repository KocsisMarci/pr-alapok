#hazi_feladat_025
'''
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő szavakat is elfogadja.

'''
a_betuvel_kezdodok=[]

szo=None
while szo!="":
    szo=input("Írj be egy kis/nagy a betűvel kezdődő szót, ha nem a-val kezdődik akkor figyelmen kívűl hagyjuk az adott szót: ")
    if szo!="":
            if szo[0]=="a" or szo[0]=="A":
                a_betuvel_kezdodok.append(szo)

    if szo=="":
        print(f"Az általad megadott szavak, mellyek a, vagy A betűvel kezdődnek: {a_betuvel_kezdodok}")        