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
#1.feladat v�ge

#2.feladat
print("2. feladat\nA napl�ban " +str(len(naplo)) + " hi�nyz�s van.")
#2. feladat v�ge

#3.feladat
igazolt=0
igazolatlan=0
for e in naplo:
    igazolt+=e[3].count("X")
    igazolatlan+=e[3].count("I")

igazolt=[e[3].count("X") for e in naplo]
print("3. feladat\nAz igazolt hi�nyz�sok sz�ma" + str(igazolt) + " ,az igazolatlanok�" + str(igazolatlan) + " �ra.")
#3. feladat v�ge

#4. feladat
def hetnapja(honap,nap):
    napnev =["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1] + nap) % 7
    return napnev[napsorszam]
#4. feladat v�ge

#5. feladat
honap=int(input("A h�nap sorsz�ma: "))
nap=int(input=("A nap sorsz�ma: "))
print("Azon a napon" + hetnapja(honap,nap) + " volt.")
#5.feladat v�ge

#6.feladat
napnev=input("a nap neve= ")
ora=int(input("Az �ra sorsz�ma: "))

db=0
for e in naplo:
    if hetnapja(e[0], e[1])==


#7. 
