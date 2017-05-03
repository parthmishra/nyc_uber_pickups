import os
import json
import csv
import pandas as pd


locationIds = pd.read_csv("rf_locationId.csv",names=['locationID','num_rides'])
puma_data = pd.read_csv("locations_with_puma.csv")
loc_to_puma = {}
puma_num_rides = {}

for index, row in puma_data.iterrows():
    loc_id = row['locationID']
    puma = row['PUMA']
    if loc_id not in loc_to_puma:
        loc_to_puma[loc_id] = puma

for index, row in locationIds.iterrows():
    puma = loc_to_puma[row['locationID']]
    num_rides = row['num_rides']
    if puma not in puma_num_rides:
        puma_num_rides[puma] = num_rides
    else:
        puma_num_rides[puma] += num_rides

#print(puma_num_rides)
df = pd.DataFrame.from_dict(puma_num_rides,orient='index')
print(df.columns)

#print(df)
#df.to_csv('puma_rides.csv')

"""
print(puma_num_rides[3701])

with open("nyc.json") as f:
    data = json.load(f)

for feature in data['features']:
    puma = int(feature['properties']['PUMA'])
    feature['properties']['num_rides'] = int(puma_num_rides[puma])

with open('data.geojson', 'w') as outfile:
    json.dump(data, outfile)
"""
