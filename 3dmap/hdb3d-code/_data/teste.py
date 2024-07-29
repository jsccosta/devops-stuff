import json

new_geo_file = {}
with open('singapore-latest-new.geojson', 'r') as f:
    geo_file = json.load(f)
    new_geo_file["type"] = "FeatureCollection"
    new_geo_file["features"] = []
    for entry in geo_file:
        for feature in entry["features"]:
            if feature["geometry"]["type"] == "Polygon":
                feature["properties"]["building"] = "Y"
                new_geo_file["features"].append(feature)

with open('singapore-latest.geojson', 'w') as f:
   json.dump(new_geo_file, f) 

