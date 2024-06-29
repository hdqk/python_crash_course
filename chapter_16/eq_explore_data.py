from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('eq_data/readable_eq_data.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)
    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
