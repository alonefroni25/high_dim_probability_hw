import numpy as np
import matplotlib.pyplot as plt

# num of repetitions:
M = 10 ** 5

for n in range (10, 110, 10):
    averages = [] # initiate the averages list for n
    for _ in range(M):    
        random_variables = np.random.exponential(scale=1, size=n)
        average = np.mean(random_variables)
        averages.append(average)

    # plot the hostogram for n:
    plt.hist(averages, edgecolor='black', bins = 30, alpha=0.7, label=f'n = {n}')

# plot the hostogram of everyone:
plt.title(f'Histogram of Averages of Exponential Random Variables')
plt.xlabel('Average')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.show()