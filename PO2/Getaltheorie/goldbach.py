# program om vermoeden van goldbach te bewijzen of te weerleggen

# maak een lijst van alle priemgetallen
def alle_priems():
    primes = []
    for num in range(2, 1000):
        if priem_of_niet(num):
            primes.append(num)
    return primes

# bereken of getal 'number' een priemgetal is
def priem_of_niet(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# hoofdprogramma; checkt alle getallen vanaf 4 tot 1000
def goldbach(n):
    primes = alle_priems()
    a = len(primes) - 1
    while a >= 0:
        if n - primes[a] in primes:
            prime2 = n - primes[a]
            if prime2 == 1: # als prime2 1 is, skipt hij en zoekt hij een andere, want 1 != een priemgetal
                continue
            print(f"{n} = {primes[a]} + {prime2}")
            return
        a -= 1
    print(f"{n} kan niet worden geschreven als de som van twee priemgetallen")

for i in range(4, 1001, 2):  # Controleer alleen even getallen vanaf 4, want 2 is een priemgetal
    goldbach(i)
