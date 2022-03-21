f=open("titanic.txt")
adatok=f.read().split("\n")

f.close()

print("2. feladat: " + str (len(adatok)) + "db")

print ([e.split(";")[1] for e in adatok])
