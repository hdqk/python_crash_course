import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label parameters.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])  # axis range

# Set the tick parameters.
ax.tick_params(labelsize=14)  # tick label size
ax.ticklabel_format(style='plain')  # tick label style


# plt.show() #shows the plot on run
plt.savefig('scatter_squares.png', bbox_inches='tight')  # saves plot to file
