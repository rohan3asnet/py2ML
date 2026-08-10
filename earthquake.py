from pathlib import Path
import json
import plotly.express as px

path=Path('earthquakes.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

all_eq_dicts=all_eq_data['features']
# print(len(all_eq_dicts))
magnitudes, longitudes, latitudes=[],[],[]
for eq_dict in all_eq_dicts:
    magnitude=eq_dict['properties']['magnitude']
    longitude=eq_dict['geometry']['coordinates'][0]
    latitude=eq_dict['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)

# print(magnitudes[:10])
# print(longitudes[:10])
# print(latitudes[:10])

title='Nepal Earthquake'
fig=px.scatter_map(lat=latitudes, lon=longitudes, title=title, map_style="open-street-map")

fig.show()