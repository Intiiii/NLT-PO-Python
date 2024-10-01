'''
n = int(input("Naar welk priemgetal bent u op zoek? "))
number = 1
b = 0
while b < n:
    number += 1
    delers = 0
    getal = 0
    for i in range(number):
        getal += 1
        if number%getal != 0:
            continue
        else:
            delers += 1
            if delers > 2:
                break
    if delers>2:
        continue
    elif delers == 2:
        b += 1
print(number)

^^ deze code had ik eerst gemaakt, voordat ik wist dat het 3 defs moest gebruiken
'''

def priem_of_niet(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def alle_priem_tot(c):
    primes = []
    for num in range(2, c + 1):
        if priem_of_niet(num):
            primes.append(num)
    return primes

def zoveelste_priem(n):
    number = 1
    count = 0
    while count < n:
        number += 1
        if priem_of_niet(number):
            count += 1
    return number

n = int(input("Naar welk priemgetal bent u op zoek? "))
if n < 2:
    print("Input moet groter zijn dan of gelijk aan 2")
else:
    print(zoveelste_priem(n))