
class Kor: 
    osztaly_valtozo=111
    evszam=2024

    def __init__(self,sugar,kozeppont=(0,0)):
        self.sugar=sugar
        self.kozeppont=kozeppont

    
    def terulet(self):
        return f"A kör területe: {pow(self.sugar,2)*3.14:.2f} négyzet cm" 
    
    def kerulet(self):
        return f"A kör kerülete: {self.sugar*3.14*2:.2f} cm"


# ------------------------------------------------------------------
print(Kor.evszam)

kor01=Kor(5,(4,4))
print(kor01.evszam)
kor02=Kor(10,(1,1))

print(f"A kor01 sugara: {kor01.sugar} cm")
print(f"A kor02 sugara: {kor02.sugar} cm")
print(f"Az előbb említett kettő sugár összege: {kor01.sugar+kor02.sugar:.2f} cm")

print(kor01.kerulet())
print(kor02.terulet())
print(kor01.kerulet())
print(kor02.terulet())
print(f"{kor01.sugar}")
print(f"{kor02.sugar}")

