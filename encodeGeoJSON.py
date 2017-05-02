"""
encodeJSON.py

Encodes a PUMA geojson file with demographic information located in the
file 'locations_with_puma.csv'

"""

import os
import json
import csv
import pandas as pd


nyc_json = "nyc.json"
nyc_demo = "locations_with_puma.csv"
uber = "uber_data.csv"


locationIds = {}
puma_rides = {}


with open(nyc_json) as f:
    geo_data = json.load(f)

uber_data = pd.read_csv(uber)
#demo_data = pd.read_csv(nyc_demo)
#print(demo_data['PUMA'])
df_size = len(uber_data)
prog25 = df_size/4
prog50 = 2*prog25
prog75 = 3*prog25



# generate ride frequency for each location id
print("Generating locationIds...")
for index, row in uber_data.iterrows():
    l_id = row['locationID']
    if index == 1:
        print("Starting...")
    if index == prog25:
        print("25 percent complete!")
    if index == prog50:
        print("50 percent complete!")
    if index == prog75:
        print("75 percent complete!")

    if l_id not in locationIds:
        locationIds[l_id] = 1
    else:
        locationIds[l_id] += 1

#print(locationIds)
print("Finished creating locationIds!")
# add data to csv since running this takes too long
print("Writing to csv...")
with open('rf_locationId.csv','w') as f:
    fieldnames = ['locationID','num_rides']
    w = csv.writer(f)
    w.writerows(locationIds.items())
print("Done!")
