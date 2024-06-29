from pathlib import Path
import json
import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data\eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)
    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)
    eq_title = eq_dict['properties']['title']
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags, color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
