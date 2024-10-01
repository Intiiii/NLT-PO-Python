a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

a1 = a*(b+c)
b1 = b*(a+c)
c1 = c*(a+b)

print(max(a1,b1,c1))