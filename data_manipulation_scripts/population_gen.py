import requests
import json
import csv

population_data = []

def get_city_opendata(city, country):
    tmp = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?refine=country:%s&refine=ascii_name:%s'
    cmd = tmp % (country, city)
    res = requests.get(cmd)
    dct = json.loads(res.content)
    out = dct['results'][0]['population']
    return out

csv_file = "finalfinal.csv"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    header.append("population")  # Add "pop" to the existing header

    for row in reader:
        if row[0] != "city":
            try:
                pop = get_city_opendata(row[0], 'India')
                row.append(pop)
                population_data.append(row)
            except:
                print("error in", row[0])
                row.append(0)
                population_data.append(row)


with open('finalfinal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Write the updated header
    for row in population_data:
        writer.writerow(row)



# Also corrected some cities spelling and manually added population