import plotly.express as px
from random_walk import RandomWalk


# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the steps in the walk.
fig = px.scatter(x=rw.x_values, y=rw.y_values)

fig.show()  # shows the figure in your default browser
