import openrouteservice
from openrouteservice import convert
import folium


client = openrouteservice.Client(key='5b3ce3597851110001cf6248c3fd703faef94757bf90ac1f97e868da')

coords = ((107.626096, -6.910096 ),(107.614830,-6.909976),(107.610782, -6.908217))
res = client.directions(coords)
geometry = client.directions(coords)['routes'][0]['geometry']
decoded = convert.decode_polyline(geometry)

distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

m = folium.Map(location=[-6.910096, 107.626096 ],zoom_start=10, control_scale=True,tiles="cartodbpositron")
folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

folium.Marker(
    location=list(coords[0][::-1]),
    popup="E",
    icon=folium.Icon(color="black"),
).add_to(m)

folium.Marker(
    location=list(coords[1][::-1]),
    popup="B",
    icon=folium.Icon(color="red"),
).add_to(m)

folium.Marker(
    location=list(coords[2][::-1]),
    popup="A",
    icon=folium.Icon(color="blue"),
).add_to(m)


m.save('map.html')