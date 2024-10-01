import random
import matplotlib.pyplot as plt

# lijst waar je de random getallen in bewaart
totalen = []

# genereer 10.000 random getallen
n = 10000
    # plot de frequentie-distributie (50 bins)


def som_random_getallen(n):
    for i in range(n):
        totaal = 0
        below_40 = 0
        above_60 = 0
        for _ in range(100):
            getal = random.random()
            totaal += getal
        totalen.append(totaal)
    for x in totalen:
        if x < 40:
            below_40 += 1
        elif x > 60:
            above_60 += 1
    pro_below_40 = (below_40/len(totalen))*100
    pro_above_60 = (above_60/len(totalen))*100
    print(f"percentage onder 40 is: {pro_below_40}")
    print(f"percentage boven 60 is: {pro_above_60}")	
    return totalen

plt.xlim(30, 70)
plt.hist(som_random_getallen(n), bins=50)
plt.show()
