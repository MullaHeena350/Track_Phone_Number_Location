
import phonenumbers
from secret import NUMBER
from secret import API_KEY
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

x=phonenumbers.parse(NUMBER,None)#this parse coverts one form to another form
#country location
location=geocoder.description_for_number(x,"en")#en means english
print(location)

# operator name or sim name 
operator_name=phonenumbers.parse(NUMBER,)
data=carrier.name_for_number(operator_name,"en")
print(data)
geocoder=OpenCageGeocode(API_KEY)
query=str("Mumbai,india")
result=geocoder.geocode(query)
# print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)
my_map=folium.Map(location = [lat,lng],zoom_start=9)#Map is a method in folium
folium.Marker([lat,lng],popup=location).add_to(my_map)
my_map.save("mytracker.html")

