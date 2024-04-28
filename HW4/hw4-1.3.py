import math
import numpy as np

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

# Parameters for exp3 algorithm
gama = 0.5
T = 100
weights = np.array([1.0, 1.0])
probabilities = np.zeros(2)

# Array for the xhat 
xhat = np.zeros(2)

# Variables to calculate average and variance
history = np.zeros(T)

# Loop for the algorithm
for i in range(T):
    # Calculate the probabilities
    for j in range(2):
        probabilities[j] = (1-gama) * (weights[j] / np.sum(weights)) + gama / 2
        
    # Draw a stock based on the probabilities
    chosenStock = np.random.choice(2, p=probabilities)
    
    # Invest in the chosen stock
    percentGain = np.random.normal(mu[chosenStock], sigma[chosenStock])
    money += money * percentGain
    
    # Add money to a running total to calculate the average
    history[i] = money

    # Update the xhat values
    for j in range(2):
        if (j == chosenStock):
            xhat[j] = percentGain / probabilities[j]
        else:
            xhat[j] = 0

        # Update the weights
        weights[j] = weights[j] * np.exp(gama * xhat[j] / 2)
    
    # Print the results
    print('After investing in', stocks[chosenStock], ': $', money)

# Print final results
print('Average: $', np.average(history))
print('Variances: ', np.var(history))