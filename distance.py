import googlemaps
from datetime import datetime
import numpy as np
import config

gmaps = googlemaps.Client(key=config.google_key)

# # Coverts to latlong
# geocode_result = gmaps.geocode('1007 S Congress Ave, Austin, TX 78704')
# print(str(geocode_result))

now = datetime.now()
matrix = gmaps.distance_matrix("Round Rock, TX", "Austin, TX",
                mode="driving",
                avoid="tolls",
                departure_time=now,
                traffic_model="optimistic")
print(str(matrix))
