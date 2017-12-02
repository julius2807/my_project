import googlemaps
import json
import pprint
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBcTRLn1VOTMqW_ZZHnTQWHN9ifcoMJJV4')

# Geocoding an address
#geocode_result = gmaps.geocode('Griya Loka, BSD, ID')

#print(geocode_result)

#print('==========================')

autocomplete = gmaps.places_autocomplete( 'Jalan Raya Bekasi Barat')

for result in autocomplete:
    print(result['description'])
    print('+++')


# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

#print(reverse_geocode_result)

# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
#                                     mode="transit",
#                                     departure_time=now)
#print(directions_result)
