import json
import requests

WARD_ID = '2529'

wards_url = 'http://mapit.mysociety.org/area/{key}/children'
ward_geometry_url = 'http://mapit.mysociety.org/area/{key}.geojson'

all_wards = {
    "type": "FeatureCollection",
    "features": []
}


wards = json.loads(requests.get(wards_url.format(key=WARD_ID)).text)

for key, ward_properties in wards.iteritems():
    if ward_properties['type'] == 'MTW': #Metropolitan district ward
        ward_geometry = json.loads(requests.get(ward_geometry_url.format(key=key)).text)

        all_wards["features"].append({
            "type": "Feature",
            "geometry": ward_geometry,
            "properties": ward_properties
        })

with open('wards.geojson', 'w') as f:
    f.write(json.dumps(all_wards))
