import matplotlib.pyplot as plt
import numpy as np

# Define the centers of the circles
centers = [(0, 0), (np.cos(np.pi / 3), np.sin(np.pi / 3)), (-np.cos(np.pi / 3), np.sin(np.pi / 3))]
radius = 1

# Create a figure and axis
fig, ax = plt.subplots()

# Draw circles
for (x, y) in centers:
    circle = plt.Circle((x, y), radius, fill=False, edgecolor='b', linewidth=2)
    ax.add_artist(circle)

# Define the vertices of the triangle
triangle_vertices = [(-1, 0), (1, 0), (0, np.sqrt(3))]

# Draw the triangle
triangle = plt.Polygon(triangle_vertices, fill='b', facecolor='lightcoral', edgecolor='r', linewidth=2)
ax.add_artist(triangle)

# Set limits and aspect ratio
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal', 'box')

# Add grid
ax.grid(True)

# Plot the centers
for (x, y) in centers:
    ax.plot(x, y, 'r')  # Red dot at the center of each circle

# Add labels for the centers
ax.text(0, 0, '(0,0)', fontsize=12, ha='right')
# ax.text(np.cos(np.pi / 3), np.sin(np.pi / 3), '(cos(pi/3), sin(pi/3))', fontsize=12, ha='right')
# ax.text(-np.cos(np.pi / 3), np.sin(np.pi / 3), '(-cos(pi/3), sin(pi/3))', fontsize=12, ha='right')

# Title
plt.title('The given figure')

# Show plot
plt.show()