f=open("penztar.txt")

#1.fealdat
kosar=[]
#szoveg=f.read()
#print(szoveg)
print(f.readline())
for sor in f:
    kosar.append(sor.strip())

f.close()
print(kosar)
#2. feladat
print("2.feladat")
print("A fizet�sek sz�ma: " + str(kosar.count("F")))

#3.feladat
print("3.feladat")
print("Az els� v�s�rl�" + str(kosar.index("F")) + "darab �rucikket v�s�rolt.")

sorszam=int(input("V�s�rl�s sorsz�ma: "))
arunev=input("�rucikk neve: ")
darab=int(input("Darabsz�m: "))

#5. feladat
aruindex=kosar.index(arunev)
darabLista=kosar[:aruindex]
print(darabLista)
vasarlasDb=darabLista.count("F")
print(vasarlasDb)

print("5. feladat")
print("Az elso vasarlas sorszama :" + str(vasarlasDb))

utolsoIndex=0
for i in range(0,len(kosar)):
    if kosar[i*-1-1]==arunev:
        utolsoIndex=len(kosar)-i
        break
darabLista=kosar[:utolsoIndex]
vasarlasDb=darabLista.count("F") + 1
print("Az utols� vasarlas sorszama :" + str(vasarlasDb))


        
