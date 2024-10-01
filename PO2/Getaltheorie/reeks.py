def priem_of_niet(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def alle_priems():
    primes = []
    for num in range(2, 10000):
        if priem_of_niet(num):
            primes.append(num)
    return primes
   
   
def reeks_niet_priem():
    primes = alle_priems()
    non_primes = [i for i in range (10000) if i not in primes]
    a = 1
    b = 0
    begin_getal = 0
    langste_reeks = 0
    for i in range(len(non_primes)-1):
        if non_primes[i]+1 == non_primes[i+1]:
            a+=1
        else:
            if a > langste_reeks:
                langste_reeks = a
                begin_getal = non_primes[i-a+1]        
            a = 1
    eind_getal = begin_getal+langste_reeks-1
    print(f"De langste reeks niet-priemgetallen onder de 10.000 begint op {begin_getal} en eindigt bij {eind_getal}")
    print(f"De reeks is {langste_reeks} lang.")

reeks_niet_priem()
