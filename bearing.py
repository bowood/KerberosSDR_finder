#!/usr/bin/python
import json
import math
import geopy
import random

from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

# FIDI Manhattan
origin = geopy.Point(40.705150, -74.0085300)
orig_bearing = 139.3

# Crown Heights
#origin = geopy.Point(40.673512, -73.958879)
#orig_bearing = 195


with open('/home2/greenim9/data/data.json') as data_file:
    data_loaded = json.load(data_file)

stroke_weight = float(data_loaded['DATA']['PWR'])

destination = VincentyDistance(kilometers=15).destination(
    origin, 
    orig_bearing+float(data_loaded['DATA']['DOA'])
  )

lat2, lon2 = destination.latitude, destination.longitude

print "Content-type: application/json"
print 

start = [-74.0085300, 40.705150];
end = [lon2, lat2];

print json.dumps({
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "prop0": "Bearing",
        "strokeWeight": stroke_weight
      },
      "geometry": {
        "type": "LineString",
        "coordinates":
        [
          start,
          end
        ]
      }
    }
  ]
})


