f=open("titanic.txt")
adatok=f.read().split("\n")

f.close()

print("2. feladat: " + str (len(adatok)) + "db")

print ([e.split(";")[1] for e in adatok])
ossz=0
for e in adatok:
    temp=e.split(";")
    tulelo=int(temp[1])
    eltunt=int(temp[2])
    pssz+=tulelo
    ossz+=eltunt

print("3.feladat: " +str(ossz) + "fõ")

kulcsSzo=input("4.feladat: Kulcsszó: ")
van=false
