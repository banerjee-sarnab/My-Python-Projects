import phonenumbers

from phone_number import number

from phonenumbers import geocoder

import folium

key = "96543e6276214d2880c57f832e0888d6"

sam_number = phonenumbers.parse(number)

location = geocoder.description_for_number(sam_number, "en")
print(number)
print(location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
# print(lat,lng)
mymap = folium.Map(location = [lat,lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to(mymap)

mymap.save("location.html")

