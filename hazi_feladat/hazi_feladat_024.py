#hazi_feladat_024
'''
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, 
akkor azt hagyja figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! 
A program a bekért neveket írja ki a képernyőre!

'''
a_betuvel_kezdodok=[]

szo=None
while szo!="":
    szo=input("Írj be egy kis a betűvel kezdődő szót, ha nem kis a-val kezdődik akkor figyelmen kívűl hagyjuk az adott szót: ")
    if szo!="":
            if szo[0]=="a":
                a_betuvel_kezdodok.append(szo)

    if szo=="":
        print(f"Az általad megadott szavak, mellyek a betűvel kezdődnek: {a_betuvel_kezdodok}")        