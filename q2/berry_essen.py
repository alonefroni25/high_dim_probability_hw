import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

# num of repiti
M = 10 ** 5

log_max_distances_array = []
log_n_array = []

for n in range (10, 110, 10):
    normalized_averages = np.array([])

    # generate the list of averages
    for _ in range(M):    
        random_variables = np.random.exponential(scale=1, size=n)
        average = np.mean(random_variables)
        z = np.sqrt(n) * (average - 1)
        normalized_averages = np.append(normalized_averages, z)

    # sort the list
    normalized_averages.sort()
    cdf_distance_array = []
    for i in range(M):
        # For every point out of M I calculate the distance
        cdf_distance_array.append(abs(i / M - norm.cdf(normalized_averages[i], 0, 1)))

    # extract the maximum of the distances ~ supermum
    max_distance = max(cdf_distance_array)
    log_max_distances_array.append(math.log(max_distance))
    log_n_array.append(math.log(n))

# Perform linear regression
slope, intercept = np.polyfit(log_n_array, log_max_distances_array, 1)  # 1 indicates linear regression (degree 1 polynomial)

# Calculate the values of the regression line
y_fit = slope * np.array(log_n_array) + intercept

# generate the plots
plt.scatter(log_n_array, log_max_distances_array, color='red')
plt.plot(log_n_array, y_fit, color='blue', label=f'y = {slope:.3f}x + {intercept:.3f}')
plt.title(f'cdf distance from normal as func of n (logarithmic)')
plt.xlabel('log(n)')
plt.ylabel('| Pr(Zn <= z) - normal_cdf(z) |')
plt.grid(True)
plt.legend()
plt.show()