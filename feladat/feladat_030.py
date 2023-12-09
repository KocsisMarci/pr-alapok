#Csak olvasod a listaelemeket, vagy módosítani is akarod?!

"""
Nem mindegy, hogyan járod be a listát!
A fentiekben bemutatott három lehetőség közül az I. és III. számú esetben a lista bejárása úgy történik, hogy az egyes elemek - minden egyes cikluslépésben 
- egy 'honap' nevű átmeneti változóba kerülnek kimásolásra, és ezt használjuk fel a print utasításban. Ha módosítani szeretnéd a listaelemet 
(pl. nagybetűsre alakítani) akkor hiába tennéd ezt meg a 'honap' nevű változó esetében, ez az eredeti listaelemet NEM módosítaná! 
Így ez a bejárás csak az adatok olvasására alkalmas!
"""
honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
        # az eredeti listaelem NEM módosul!
	     honap = honap.upper()	

    