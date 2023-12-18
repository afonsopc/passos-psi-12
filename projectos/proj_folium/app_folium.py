import folium

latitude = 37.5665
longitude = 126.9780

# Create a map object
map = folium.Map(location=[latitude, longitude], zoom_start=12)

folium.Marker([latitude, longitude], popup='Lixbona').add_to(map)

# Save the map as an HTML file
map.save("map.html")
