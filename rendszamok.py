f=open("autok.txt")
teljes=f.read()
f.close()

teljes=teljes[0:-1]

darabok=teljes.split("\n")

rendszamok=[]
for egySor in darabok:
    vag=egySor.split(" ")
    if not(vag[2] in rendszamok):
        rendszamok.append(vag[2])


#print(rendszamok)

f=open("rendszamok.txt", "w")
for egyAdat in rendszamok:
    f.write(egyAdat+"\n")
#f.write("\n".join(rendszamok))
f.close()

f=open("rendszamok.txt", "a")
f.write(rendszamok.count + "darab auto volt")
f.close()
