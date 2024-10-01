'''
    In de officiele opdracht moet je met stuivers en kwartjes etc werken, ik heb persoonlijk
    geen kennis over hoe dit vroeger allemaal werkte, dus heb ik de opdracht gemaakt met de 
    moderne munten, dus met 2 euro, 1 euro, 50 cent, 20 cent, 10 cent, 5 cent, 2 cent en 1 cent.     
'''
prijs = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
prijs = int(prijs * 100)
munten = 0

while prijs > 0:
    if prijs >= 200:
        prijs -= 200
    elif prijs >= 100:
        prijs -= 100  # Correctie: trek 100 af in plaats van prijs-100
    elif prijs >= 50:
        prijs -= 50   # Correctie: trek 50 af
    elif prijs >= 20:
        prijs -= 20   # Correctie: trek 20 af
    elif prijs >= 10:
        prijs -= 10   # Correctie: trek 10 af
    elif prijs >= 5:
        prijs -= 5    # Correctie: trek 5 af
    elif prijs >= 2:
        prijs -= 2    # Correctie: trek 2 af
    elif prijs >= 1:
        prijs -= 1    # Correctie: trek 1 af
    munten += 1  # Correctie: verhoog munten met 1 voor elke munt

print(munten)

