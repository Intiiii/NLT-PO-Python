import random
import math
import matplotlib.pyplot as plt

def twitter():
    def is_in_twitter_egg(x, y):
        if x is None or y is None:
            return False
        return math.sqrt(x**2 + y**2) + (2/3) * math.sqrt(x**2 + ((5/6) - y)**2) <= 1

    num_punten = 1000000
    binnen = 0
    schattingen = []
    punten = []

    for i in range(1, num_punten + 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-0.4, 1)
        punten.append((x, y, is_in_twitter_egg(x, y)))
        if is_in_twitter_egg(x, y):
            binnen += 1
        
        if i % 1000 == 0:
            oppervlakte_schatting = (binnen / i) * 2.8  # oppervlakte van het vierkant is 4
            schattingen.append(oppervlakte_schatting)
    
    uiteindelijke_oppervlakte = round(schattingen[-1],2)
    
    # Plot de distributie van de goede en slechte punten
    binnen_punten = [(x, y) for x, y, binnen in punten if binnen]
    buiten_punten = [(x, y) for x, y, binnen in punten if not binnen]
    
    if binnen_punten:
        plt.scatter(*zip(*binnen_punten), color='green', s=1, label='Binnen')
    if buiten_punten:
        plt.scatter(*zip(*buiten_punten), color='red', s=1, label='Buiten')
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Add text in the middle of the egg
    plt.text(0, 0.3, f'Oppervlakte = {uiteindelijke_oppervlakte:.2f}', fontsize=12, ha='center')
    
    plt.show()
    return uiteindelijke_oppervlakte
	

print(f"De oppervlakte van het Twitter ei is {twitter()}")