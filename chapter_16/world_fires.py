from pathlib import Path
import csv
import plotly.express as px

# Parse file.
path = Path("world_fires_24h.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract index locations.
for index, column_header in enumerate(header_row):
    if column_header == "latitude":
        latitude = index
    if column_header == "longitude":
        longitude = index
    if column_header == "frp":
        frp = index

# Extract data.
lats, lons, frps = [], [], []
for row in reader:
    lats.append(float(row[latitude]))
    lons.append(float(row[longitude]))
    frps.append(float(row[frp]))

# Set up graph.
title = 'Worldwide Wildfires In The Last 24 Hours'
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=frps, color=frps,
                     color_continuous_scale='YlOrRd',
                     labels={'color': 'Radiative Power'},
                     projection='natural earth',
                     )
fig.show()
