from blue_area_monte_carlo import *
import math
import matplotlib.pyplot as plt
import numpy as np

x = np.array([])
y = np.array([])

delta = 100
POINTS_NUM = 50000000

real_area = math.sqrt(3) + math.pi * 3 / 2

square_area = (MAX_VAL - MIN_VAL) ** 2

# Create a figure and axis
fig, ax = plt.subplots()

# Add grid
ax.grid(True)

my_dict = {}
in_points_counter = 0
n = delta
last_n = 0

# Im multiplying n by 2 and update the calculations as in the last section.
while n <= POINTS_NUM:
    in_points_counter += get_num_of_in_points(n - last_n)
    in_point_probability = in_points_counter / n

    estimated_area = square_area * in_point_probability

    error = abs(real_area - estimated_area)
    x = np.append(x, math.log(n))
    y = np.append(y, math.log(error))
    # x, y = n, error
    ax.plot(x, y, 'ro')
    last_n = n 
    n *= 2

# Perform linear regression
slope, intercept = np.polyfit(x, y, 1)  # 1 indicates linear regression (degree 1 polynomial)

# Calculate the values of the regression line
y_fit = slope * x + intercept

plt.scatter(x, y, color='red')
plt.plot(x, y_fit, color='blue', label=f'y = {slope:.3f}x + {intercept:.3f}')

plt.xlabel('log(n)')
plt.ylabel('log(error)')

# Title
plt.title('Error as func of n')
plt.legend()

# Show plot
plt.show()