#!/usr/bin/python
import json
import math
import geopy
import random

from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

origin = geopy.Point(40.705150, -74.0085300)
#destination = VincentyDistance(kilometers=15).destination(origin, 139.3)

destination = VincentyDistance(kilometers=15).destination(origin, random.randrange(0,360))

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
        "prop0": "Bearing"
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


