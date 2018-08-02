#Project to build open map with Python package called Folium
#To install from cmd prompt: python -m pip install folium

import folium
import itertools

#map object is its main one
map = folium.Map(location=[37.245209, -121.828859], zoom_start = 11, tiles='Stamen Terrain')
#The above object exists only in python until imported into html

places = [(37.388500, -121.932656,'Reference 1'),(37.245209, -121.828859,'Reference 2')]
hikes_done = [(37.173962,-121.825096,'Almaden Quicksilver County Park'),(37.396869,-121.802276,'Alum rock park'),(37.173209,-121.760445,'Calero County Park'),
              (37.085122,-121.791877,'Uvas Canyon County Park')]
hikes_to_go = [(37.881591,-121.914153,'Mt. Diablo State Park'),(37.512436,-121.880513,'Mission Peak Summit'),(37.235352,-122.062720,'Sanborn County Park')]

for i,j,k in itertools.izip_longest( range(len(places)), range(len(hikes_done)), range(len(hikes_to_go))):
    if i != None:
        map.add_child(folium.Marker(location=[places[i][0],places[i][1]],popup=(places[i][2]), icon = folium.Icon(color = 'blue')))
    if j != None:
        map.add_child(folium.Marker(location=[hikes_done[j][0],hikes_done[j][1]],popup=hikes_done[j][2], icon = folium.Icon(color = 'purple',icon_color = 'pink')))
    if k != None:
        map.add_child(folium.Marker(location=[hikes_to_go[k][0],hikes_to_go[k][1]],popup=hikes_to_go[k][2], icon = folium.Icon(color = 'darkred')))

map.save(outfile='Hike_Map.html')
#Above line creates a html page which can be opened in browser to reveal the map.

