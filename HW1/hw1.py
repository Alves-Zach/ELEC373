import numpy as np

# Initial params
iterations = 100
initialCash = 100

# The ranges of the different returns from each stock
# The ranges are in percentages
S1range = np.array([-1, 1])
S2range = np.array([-2, 8])

# Stocks problem
def randomInvestment():
    curCash = initialCash
    # Simulation loop
    for i in range(100):
        # Create a random number from 0 to 1
        rand = np.random.rand()

        if (rand < 0.5):
            # Invest in Stock 1
            curCash += curCash * (np.random.uniform(S1range[0], S1range[1]) / 100)
            print("Stock 1")
        else:
            # Invest in Stock 2
            curCash += curCash * (np.random.uniform(S2range[0], S2range[1]) / 100)
            print("Stock 2")
        
        print("Iteration: ", i, " Cash: ", curCash, "\n")

def main():
    randomInvestment()

if __name__ == "__main__":
    main()