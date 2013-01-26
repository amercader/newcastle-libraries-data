import json
import requests

query_by_point_url = 'http://mapit.mysociety.org/point/4326/{lon},{lat}'

with open('libraries.geojson', 'r') as f:
    libraries = json.loads(f.read())

for library in libraries['features']:
    url = query_by_point_url.format(
            lon=library['geometry']['coordinates'][0],
            lat=library['geometry']['coordinates'][1]
            )

    areas = requests.get(url).json

    for key, area in areas.iteritems():
        if area['type'] == 'MTW':   # We want Metropolitan district wards
            library['properties']['ward_id'] = key
            library['properties']['ward_name'] = area['name']
            break

with open('libraries_with_wards.geojson', 'w') as f:
    f.write(json.dumps(libraries))
