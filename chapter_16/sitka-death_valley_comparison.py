from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path_dv = Path("weather_data/death_valley_2021_simple.csv")
lines_dv = path_dv.read_text().splitlines()
reader_dv = csv.reader(lines_dv)
header_row_dv = next(reader_dv)
path_sk = Path("weather_data/sitka_weather_2021_simple.csv")
lines_sk = path_sk.read_text().splitlines()
reader_sk = csv.reader(lines_sk)
header_row_sk = next(reader_sk)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)  # print what's in the header

# Extract dates and temperatures.
dates_dv, highs_dv = [], []
for row in reader_dv:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_dv = int(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_dv.append(current_date)
        highs_dv.append(high_dv)

# Extract temperatures.
dates_sk, highs_sk = [], []
for row in reader_sk:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high_sk = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_sk.append(current_date)
        highs_sk.append(high_sk)

# Plot the temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates_dv, highs_dv, color='red', alpha=0.5)
ax.plot(dates_sk, highs_sk, color='orange', alpha=0.5)
ax.set(ylim=(15, 135))

# Format plot.
title = "Daily High Temperatures, 2021\nDeath Valley, CA vs. Sitka, AK"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
