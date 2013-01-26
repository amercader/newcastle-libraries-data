import csv
import json

with open('libraries_with_wards.geojson', 'r') as f:
    libraries = json.loads(f.read())

councillors = []
with open('councillors-emails.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        councillors.append(row)

def get_councillors(ward_name):
    found = []
    for councillor in councillors:
        if ward_name == councillor['ward']:
            found.append(councillor)
    return found

for library in libraries['features']:

    library['properties']['councillors'] = get_councillors(library['properties']['ward_name'])

with open('libraries_with_councillors.geojson', 'w') as f:
    f.write(json.dumps(libraries))
