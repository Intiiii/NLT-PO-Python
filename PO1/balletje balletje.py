a = int(input("Aantal bekertjes: "))
b = a
c = int(input("hoeveelheid wisselingen: "))

for i in range(c):
    d, e = input().split(" ")
    d = int(d)
    e = int(e)
    if d == b:
        b = e
    elif e == b:
        b = d

print(b)


    