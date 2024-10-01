import matplotlib.pyplot as plt
import numpy as np

def nulpunten(a, b, c):
    D = b**2 - 4*a*c
    
    if D < 0:
        nulpunten = []
    else:
        n1 = (-b+np.sqrt(D)) / (2*a)
        n2 = (-b-np.sqrt(D)) / (2*a)
        nulpunten = [n1, n2]
    x = np.linspace(-10, 10, 1000)   
    y = a*x**2+b*x+c
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    
    if nulpunten:
        plt.scatter(nulpunten, [0, 0], color='red')
        for n in nulpunten:
            plt.annotate(f"x = {n:.2f}", (n, 0))
    
    plt.show()
    return nulpunten
    
print(f"de nulpunten zijn {nulpunten(1, 2, -10)}")