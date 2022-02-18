import random

szamok=[]

megegyszer = True
while megegyszer:
    szamok.clear()
    szamok.append(random.randint(1,9))
    szamok.append(random.randint(1,9))

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
        
    if joValasz==valasz:
        print("helyes válasz")
    else:
        print("nem jó válasz")
        megegyszer = false

#21.12.08
