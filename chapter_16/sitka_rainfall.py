from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)  # print what's in the header

# Extract dates and temperatures.
dates, rainfall = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        rainfall.append(rain)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, rainfall, color='blue', alpha=1)

# Format plot.
title = "Daily Rainfall, 2023\nSitka, Alaska, USA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Inches", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
