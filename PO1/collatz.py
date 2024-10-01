a = int(input("a: "))
a_max = 0

while a != 1:
    if a == 1:
        print("klaar")
    elif a % 2 == 0:
        a1 = a/2
        a = a1
    elif a % 2 == 1:
        a1 = 3*a+1
        a = a1
    if a1 > a_max:
        a_max = a
        

print(int(a_max))
    