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
    ossz+=tulelo
    ossz+=eltunt

print("3.feladat: " +str(ossz) + "f�")

kulcsSzo=input("4.feladat: Kulcssz�: ")
van=false

for e in adatok:
    if e.find(kulcsSzo)>=0:
        van=True
        break

if van:
    print("Van tal�lat")
else:
    print("Nincs tal�lat")


adatok2=[]
for e in adatok:
    temp=e.split(";")
    temp[1]=int(temp[1])
    temp[2]=int(temp[2])
    adatok2.append(temp)
print(adatok2)

talalat=[e for e in adatok if e[0].find(kulcsSzo)>-1]
print(talalat)
if len(talalat)>0:
    print("Van tal�lat")
else:
    print("Nincs tal�lat")

##
print("5.feladat")
for e in talalat:
    print(e[0]+ " " + str(e[1]+e[2])+" f�")


print([ e[0]+ " " + str(e[1]+e[2])+" f�" for e in talalat2 ])

