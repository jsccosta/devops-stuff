#!/bin/env python

#-- a script to fetch coordinates of each building
#-- Filip Biljecki <filip@nus.edu.sg>
#-- 2019-08

import pandas as pd
import json
import time
import requests
import urllib.parse

# Read the HDB data from the CSV
blocks = pd.read_csv('../hdb-property-information.csv', sep=',')

#-- create a new dictionary with block id, address, and coordinate; or load a previous one if generated
try:
    with open('_data/blocks_coordinates.json', 'r') as f:
        blocks_coordinates = json.load(f)
    print("Loaded", len(blocks_coordinates), "entries from previous file.")
except:
    blocks_coordinates = {}

#-- list of HDB attributes we have in the CSV
all_att = ['code',
           'area',
           'year',
           'affordable',
           'insurance_price']

#-- counter
ids = 0
geoloc_file = []
#-- for each block
for i, j in blocks.iterrows():
    ids += 1
    #-- by default there is no location
    location = None
    #-- count how many features that are buildings are returned
    h = 0
    #-- construct the address for the geocoding API
    # address = str(j['blk_no']) + ' ' + str(j['street'])
    address = str(j['area'] + ', London, UK')
    # print(i, '\t', str(j['area']) + ' ' + str(j['street']))
    print(i, '\t', address)
    if i in blocks_coordinates:
        print("\tAlready fetched, skipping")
        continue

    #-- geocoder query
    for attempt in range(1):
        #-- max. 250 requests per second are allowed, so let's pause every 10ms not to exceed 100 requests per second
        # time.sleep(0.010)
        time.sleep(10)
        try:
            #-- fetch the location of the block
            #-- no authentication isneeded for this functionality of the API
            headers = {
                'User-Agent': 'Application GC 1.0',
                'From': 'tacigomess@me.com'  # This is another valid field
            }
            url = 'https://nominatim.openstreetmap.org/?q=' + urllib.parse.quote(address) + '&format=geojson&polygon_geojson=1'
            # response = requests.get('https://developers.onemap.sg/commonapi/search?searchVal=%s&returnGeom=Y&getAddrDetails=Y' % (address), auth=('user', 'password'))
            response = requests.get(url, headers=headers)
            location = response.json()
            #-- thank you OneMap
        except:
            continue
        else:
            break
    else:
        print('10 attempts failed')

    if location:
        print('\tThere are', 'result(s)')
        if not location:
            #-- if nothing is found (rarely happens)
            blocks_coordinates[i] = None
            continue
        #-- we are feeling lucky so we will just take the first result into consideration
        #-- save the information
        lat = location["features"][0]["bbox"][1]
        lon = location["features"][0]["bbox"][0]
        osm_id = location["features"][0]["properties"]["osm_id"]
        blocks_coordinates[i] = {
            'blk_no' : str(j['code']),
            'street' : str(j['area']),
            'address' : address,
            'latitude' : lat,
            'longitude' : lon,
            'id': osm_id,
            'hdb_max_floor_lvl': 5
            }
        geoloc_file.append(location)
        #-- save the HDB attributes
        for att in all_att:
            blocks_coordinates[i]['hdb_'+att] = str(j[att])

    else:
        print('Address not found')
        blocks_coordinates[i] = None

    #-- this may take some time, so let's save the data occasionally
    if ids % 100 == 0:
        with open('_data/blocks_coordinates.json', 'w') as f:
            json.dump(blocks_coordinates, f)

with open('_data/blocks_coordinates.json', 'w') as f:
        json.dump(blocks_coordinates, f)
with open('_data/singapore-latest-new.geojson', 'w') as f:
        json.dump(geoloc_file, f)
