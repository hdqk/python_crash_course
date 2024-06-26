import matplotlib.pyplot as plt
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(x) for x in poss_results]

# Plot the dice rolls.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies, width=1, edgecolor="white", linewidth=0.7)

plt.show()
