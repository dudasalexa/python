#Osztály definíció
class Kutya:
    #konstruktor
    def __init__(self,nev):
        self.nev=nev
    #osztály függvény
    def ugat(self):
        print("vauvau")
        
#Példányosítás    
k=Kutya("armageddon")
k.ugat()
print(k.nev)
#osztály változó értékadása
k.nev="Bruno"
print(k.nev)

#öröklés, leszármaztatás
class NemetJuhasz(Kutya):
    #új függvény
    def pitiz(self):
        print(self.nev + ": nein!")
    #függvény felülírás
    def ugat(self):
        print("wauwau")

n=NemetJuhasz("Rex")
n.ugat()
n.pitiz()

n2=NemetJuhasz("Kondér")
n2.pitiz()
