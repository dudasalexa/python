f=open("naplo.txt")
adatok=f.read().split("\n")
f.close()

naplo=[]
honap=0
nap=0
for e in adatok:
    if e[0]=="#":
        honap=e[2:3]
        nap=e[5:6]
        
