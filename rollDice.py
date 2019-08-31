import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print roll, "You lose!"
        return False
    elif roll <= 50:
        #print roll, "You lose"
        return False
    elif 100 > roll >= 50:
        #print roll, "You win!"
        return True
        
def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    wX = []
    vY = []
    
    currentWager = 1 
    
    while currentWager <= wager_count:
        if rollDice():
            value +=wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
        currentWager += 1
    if value < 0:
        value = "Broke!"
    #print "Funds:", value
    
    plt.plot(wX,vY)
    

x = 0
while x < 100:    
    simple_bettor(10000, 100, 100)
    x += 1

plt.ylabel("Account Value")
plt.xlabel("Wager Count")
plt.show()
    