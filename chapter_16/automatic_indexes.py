from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    if column_header == "NAME":
        station = index
    if column_header == "DATE":
        date = index
    if column_header == "TMAX":
        tmax = index
    if column_header == "TMIN":
        tmin = index

# Extract dates and temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date], '%Y-%m-%d')
    try:
        high = int(row[tmax])
        low = int(row[tmin])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Format plot.
title = f"Daily High and Low Temperatures, 2021\n{row[station]}"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
