Henrik=input("Jön Henrik ma kosarazni? ")
Hanna=input("Jön Hanna ma kosarazni? ")
if Hanna=="nem" or Hanna=="Nem" and Henrik=="Nem" or Henrik=="nem":
    print("Egyikük sem jön kosarazni")
elif Hanna=="igen" or Hanna=="Igen" and Henrik=="Igen" or Henrik=="igen":
    print("Mindketten jönnek kosarazni")
elif Hanna=="igen" or Hanna=="Igen" and Henrik=="Nem" or Henrik=="nem" or Hanna=="Nem" or Hanna=="nem" and Henrik=="Igen" or Henrik=="Nem":
    print("Csak az egyikük jön kosarazni")  
else:
    print("Nem tudom összehasonlítani")