f=open("naplo.txt")
adatok=f.read().split("\n")
f.close()
#1.feladat
naplo=[]
honap=0
nap=0
for e in adatok:
    if e[0]=="#":
        honap=e[2:4]
        nap=e[5:]
    else:
        temp=[]
        temp.append(honap)
        temp.append(nap)

        vag=e.split(" ")
        temp.append(" ".join(vag[0:2]))
        temp.append(vag[2])
        naplo.append(temp)
#1.feladat vége

#2.feladat
print("2. feladat\nA naplóban " +str(len(naplo)) + " hiányzás van.")
#2. feladat vége

#3.feladat
igazolt=0
igazolatlan=0
for e in naplo:
    igazolt+=e[3].count("X")
    igazolatlan+=e[3].count("I")

igazolt=[e[3].count("X") for e in naplo]
print("3. feladat\nAz igazolt hiányzások száma" + str(igazolt) + " ,az igazolatlanoké" + str(igazolatlan) + " óra.")
