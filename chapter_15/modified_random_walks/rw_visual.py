import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a random walk.
rw = RandomWalk(500)
rw.fill_walk()

# Plot the point_numbers in the walk.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10.67, 6))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=2)
ax.set_aspect('equal')  # gives each axis equal spacing between ticks

# Emphasize the first and last points of the walk.
ax.scatter(0, 0, color='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1],
           color='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()