a, b = input("rood zwart: ").split()
a = int(a)
b = int(b)

Rood = input("Rood: ")
Zwart = input("Zwart: ")
e = int(input("sec: "))

RList = list(Rood[::-1])
print(RList)
ZList = list(Zwart)

Ants = RList + ZList
print(Ants)


for _ in range(e):
    print(Ants)
    for i in range(max(a,b)-1):
        if i in RList and i+1 in ZList:
            Ants[i], Ants[i+1] = Ants[i+1], Ants[i]
            

