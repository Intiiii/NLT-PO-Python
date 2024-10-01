from math import sqrt
import random

def vierkant(N):
    totaalafstand = 0
    gemafstand = 0
    for _ in range(N):
        afstand = 0
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()
        afstand = sqrt((x2-x1)**2+(y2-y1)**2)
        totaalafstand += afstand
    gemafstand = totaalafstand / N
    return round(gemafstand, 2)
print(vierkant(10000))
