import phonenumbers
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
from ph_tracker_test import number, number1

from phonenumbers import geocoder, carrier

api_key1 = "67e86ce4afb143058d40ac4bb7ee5ff9"

ch_number = phonenumbers.parse(number)

location = geocoder.description_for_number(ch_number, "en")

service_provider = phonenumbers.parse(number)

#print(carrier.name_for_number(service_provider, "en"))

ch_number1 = phonenumbers.parse(number1)

location1 = geocoder.description_for_number(ch_number1, "en")

service_provider1 = phonenumbers.parse(number1,)

#print(carrier.name_for_number(service_provider1, "en"))


geocoder1 = OpenCageGeocode(api_key1)

query = str(location)

results = geocoder1.geocode(query)

#print(results)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print([lat, lng])


my_map = folium.Map(location=[lat, lng], zoomstart=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)

my_map.save("mylocation.html")
