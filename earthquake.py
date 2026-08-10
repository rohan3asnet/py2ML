from pathlib import Path
import json

path=Path('earthquakes.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

all_eq_dicts=all_eq_data['features']
print(len(all_eq_dicts))