import math
import numpy as np
import matplotlib.pyplot as plt

# Starting conditions
global money
money = 1000

# The stocks to invest in
stocks = ['Apple', 'Micosoft']

# The details about each stock
mu1 = 0.05
mu2 = 0.1

sigma1 = 0.1
sigma2 = 0.3

# Apple corrisponds to stock 1 and Microsoft to stock 2
mu = [mu1, mu2]
sigma = [sigma1, sigma2]

history = np.zeros(100)

# Helper functions to invest in the stocks
def invest(stock, amount):
    global money 

    gain = amount * np.random.normal(mu[stock], sigma[stock])
    
    money += gain

    return gain

def problem2():
    global money

    # The number of days to simulate
    days = 100
    
    print('Starting money: $', money)

    # Invest once and see which one returns more
    gains = np.zeros(2)
    for stock in range(2):
        gains[stock] = invest(stock, money/2)
    
    # Add the money to the history
    history[0] = money

    # Get the stock that returned more the first time
    chosenStock = np.argmax(gains)
    print('Chose to invest in', stocks[chosenStock])

    # Invest in the stock that returned more the first time
    for i in range (days-1):
        invest(chosenStock, money)
        print('After investing in', stocks[chosenStock],': $', money)
        history[i+1] = money
        
    # Print the average and variance
    print('Average: $', np.mean(history))
    print('Variance:', np.var(history))
    
if __name__ == '__main__':
    problem2()