import geocoder
import folium

g = geocoder.ip("me")
myAddress = g.latlng
print(myAddress)
