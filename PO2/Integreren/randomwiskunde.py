import random
def randomwiskunde():
    totaantal = 0
    N=1000000
    for i in range(N):
        totaal = 0
        aantal = 0
        while totaal < 1:
            x = random.random()
            totaal += x
            aantal += 1
        totaantal += aantal
    gem = totaantal / N
    
    print(f"Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is: {round(gem,5)}")
        
            
        
randomwiskunde()