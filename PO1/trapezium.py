a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

a = a-c
for i in range(b):
    a = a+c
    print(a*"*")