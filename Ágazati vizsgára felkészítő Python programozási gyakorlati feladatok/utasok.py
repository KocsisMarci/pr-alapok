class Utas:
    def __init__(self,kedvezmény,kilométer,jegyár=0):
        self.kedvezmény=kedvezmény
        self.kilométer=kilométer
        self.jegyár=jegyár
        self.jegyár=self.kilométer*50*(1-self.kedvezmény/100)
    
    def kmar(self):
        kilométerár=self.jegyár/ self.kilométer
        return kilométerár
    
    def jegytipus(self):
        jegytipus=""
        if self.kedvezmény==50:
            jegytipus="Diák"
        
        elif self.kedvezmény==90:
            jegytipus="Nyugdíjas"
        
        elif self.kedvezmény==0:
            jegytipus="Teljes"
        
        else:
            jegytipus="Egyéb"
        

        return jegytipus


utasok=[]
eleg=False
while not eleg:
    kedvezmeny=int(input("Adja meg hány százalékos kedvezményt szeretne:"))
    kilometer=int(input("Adja meg hány kilométert fog utazni:"))
    if kilometer==0 or len(utasok)==8:
        eleg=True
    
    elif kilometer!=0:
        utas=Utas(kedvezmeny,kilometer)
        utasok.append(utas)



for utas in utasok:
    jegytipus=utas.jegytipus()
    kilometerar=utas.kmar()
    print(f"{jegytipus}({utas.kedvezmény}%), 1 kilométer ára: {kilometerar:.1f} Forint ")
    