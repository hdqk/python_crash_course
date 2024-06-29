from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/santo_domingo_2023_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    if column_header == "NAME":
        station = index
    if column_header == "DATE":
        date = index
    if column_header == "PRCP":
        rain_id = index

# Extract dates and rainfall.
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[date], '%Y-%m-%d')
    try:
        rain = float(row[rain_id])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(rain)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(dates, rainfall, color='blue', s=10)

# Format plot.
title = f"Daily Rainfall, 2023\n{row[station]}"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Inches", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
