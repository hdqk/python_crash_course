import requests
from operator import itemgetter
import plotly.express as px

# Make an API call and check the response.
url = "https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=state:*"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
state_pops = r.json()
# remove redundant header dictionary
state_pops.pop(0)

# Build a new dictionary for each state.
state_dicts, states, pops = [], [], []
for state_pop in state_pops:
    state_dict = {
        'state': state_pop[0],
        'pop': int(state_pop[1]),
    }
    state_dicts.append(state_dict)

# Sort the list by population in descending order.
state_dicts = sorted(state_dicts, key=itemgetter('pop'), reverse=True)

# Build x and y axes.
states, pops = [], []
for sorted_state in state_dicts:
    # Process census information.
    states.append(sorted_state['state'])
    pops.append(sorted_state['pop'])

# Make visualization.
title = "Population by State\nUnited States Census Data, 2019"
labels = {'x': 'State', 'y': 'Population'}
fig = px.bar(x=states, y=pops, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
