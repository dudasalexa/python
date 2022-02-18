import random

szamok=[]

szamok.append(random.randint(1,99))
szamok.append(random.randint(1,99))

print(szamok)

muvelet=random.randint(0,2)

feladvany=str(szamok[0])
if muvelet==0:
    feladvany=feladvany+" + "
elif muvelet==1:
    feladvany=feladvany+" - "
elif muvelet==2:
    feladvany=feladvany+" * "

feladvany=feladvany+str(szamok[1]) + " = "
szoveg="() () () ="
print(szoveg.format(szamok[0],"+", szamok[1]));

print(feladvany)

valasz=input(feladvany)

joValasz=0
if muvelet==0:
    joValasz=szamok[0]+szamok[1]
elif muvelet==1:
    joValasz=szamok[0]-szamok[1]
elif muvelet==2:
    joValasz=szamok[0]*szamok[1]
    
