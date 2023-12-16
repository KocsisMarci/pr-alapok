mondat=input("Írj be egy mondatot, mondatvég írásjellel: ")
        
if mondat[-1]==".":
            print(f"Az általad megadott mondat: {mondat}, egy kijelentő mondat") 
            
elif mondat[-1]=="?":
            print(f"Az általad megadott mondat: {mondat}, egy kérdő mondat") 
            
elif mondat[-1]=="!":
            print(f"Az általad megdott mondat: {mondat}, egy felkiáltó/felszólító/óhajtó mondat")

else:
        print(f"Az általad megadott mondatról: {mondat}, nem tudom eldönteni, hogy milyen mondat")            
            
