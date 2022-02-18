'''
be=input("Kérek egy kisbetűt: ")
print(be.upper())

be=input("Kérek egy nagybetűt: ")
print(be.lower())

for i in range(70):
    print(be,end="")

print()
print(be.ljust(70,be))

be=input("Kérek egy szöveget: ")
if len(be)>=12:
    if be[11]=="k":
        print("Igaz")
    else:
        print("Nem igaz")

print(be[:3])
print(be[-3:])
szo=be[:3].upper() + be[3:-3].lower() + be[-3:].upper()
print(szo)
'''
'''
#szöveg visszafele

be=input("Kérek egy mondatot: ")
fordit=be.split(" ")
print(fordit)

fordit.reverse()

print(fordit)
print(" ".join(fordit).capitalize())

'''

be="Vizsgálja és, meg, és és és ésé sé és ésésésésésésés hogy az és szó hányszor szerepel benne."
darab=be.replace(",","").split(" ")

db=0
for szo in darab:
    if szo=="és":
        db+=1

if db==0:
    print("Nem volt egy sem")
else:
    print(str(db)+" darab volt")







