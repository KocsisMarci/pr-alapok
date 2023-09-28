#feladat_008
"""
Ez a prpogram a sebesség alapján eldönti, hogy mennyivel ment a sofőr, és ha büntetés jár neki, akkor mennyi, és a büntetőpontokat
"""
sebesség=int(input("Add meg a sebessségedet 0-tól 300-ig "))
if sebesség==0:
    print("Egy helyben álsz")
elif 0<sebesség<=50:
       print(f"Megengedet sebeséggel mentél, {sebesség}-el/al")

elif 50<sebesség<=65:
    print(f"A büntetséd 15 000 Ft, {sebesség} km/h-val mentél")
elif 65<sebesség<=80:
    print(f"A büntetésed 30 000Ft, {sebesség} km/h-val mentél")
elif 80<sebesség<=100:
    print(f"A büntetásed 60 000 Ft,{sebesség} km/h-val ")
elif sebesség>100:
    print(f"Elvették a jogosítványodat, {sebesség} km/h-val mentél")