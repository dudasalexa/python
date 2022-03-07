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
print("A fizetések száma: " + str(kosar.count("F")))

#3.feladat
print("3.feladat")
print("Az első vásárló" + str(kosar.index("F")) + "darab árucikket vásárolt.")

sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucikk neve: ")
darab=int(input("Darabszám: "))

#5. feladat
aruindex=kosar.index(arunev)
darabLista=kosar[:aruindex]
print(darabLista)
vasarlasDb=darabLista.count("F")
print(vasarlasDb)

print("5. feladat")
print("Az elso vasarlas sorszama :" + str(vasarlasDb))
