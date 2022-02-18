import random
import math

#1.feladat
print(random.random())

szam=(random.random())
print (szam)


#2. feladat
szamok=[]
darab=int(input("Kérek egy számot:"))
for i in range(1,darab):
    szamok.append(math.floor(random.random()*100)-100)
    
print szamok


#4.feladat
lista = list ((12345,123456))*50

print(lista)
for elem in lista:
    elem=elem*2
    print(elem)

print(lista)

for i in range(8):
    print(lista[i])

for i in range (1,21):
    szam=math.floor(random.random())
    print (i,szam)
print(lista)

#5. feladat
lista = list (())

print(lista)
for elem in lista:
    elem=elem
    print(elem)

num= 0
while(num < len(list)):
    if list[num] % 5 == 0:
        print(list[num], end==" hiba ")

print szam
