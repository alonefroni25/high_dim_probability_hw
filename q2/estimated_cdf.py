import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# num of repiti
M = 10 ** 5

# generate M normal values
mu = 0
sigma = 1
data = np.random.normal(0, 1, M)

# Calculate the CDF values
x = np.sort(data)
y = norm.cdf(x, mu, sigma)

# plot the normal cdf
plt.plot(x, y, label=f'normal')

for n in range (10, 110, 10):
    normalized_averages = []
    for _ in range(M):    
        random_variables = np.random.exponential(scale=1, size=n)
        average = np.mean(random_variables)
        z = np.sqrt(n) * (average - 1)
        normalized_averages.append(z)
    normalized_averages.sort()

    # the y axis is probability, which is exactly the index of the point in the array
    y = np.arange(1, M + 1) / M

    # generate plot for every n
    plt.plot(normalized_averages, y, label=f'n = {n}')

# generate the plot
plt.title(f'cdf for all n-s')
plt.xlabel('x')
plt.ylabel('cumulative probability')
plt.grid(True)
plt.legend()
plt.show()