'''
    In de officiele opdracht moet je met stuivers en kwartjes etc werken, ik heb persoonlijk
    geen kennis over hoe dit vroeger allemaal werkte, dus heb ik de opdracht gemaakt met de 
    moderne munten, dus met 2 euro, 1 euro, 50 cent, 20 cent, 10 cent, 5 cent, 2 cent en 1 cent.     
'''
while True:
    prijs = float(input("Hoeveel wisselgeld moet er gegeven worden? "))
    prijs = round(prijs*100,0)
    munten = 0
    if prijs >= 0:
        while prijs > 0:
            if prijs >= 25:
                prijs -= 25
            elif prijs >= 10:
                prijs -= 10
            elif prijs >= 5:
                prijs -= 5  
            elif prijs >= 1:
                prijs -= 1
            munten += 1
        print(munten)
        break
    else:
        continue
