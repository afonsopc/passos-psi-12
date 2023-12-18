import folium

latitude = 38.725330
longitude = -9.15002

# Create a map object


# MAP OF LISBON WITH A MARKER AND LAYERS WITH STAELITE LAYER
map = folium.Map(location=[latitude, longitude], zoom_start=12)
folium.TileLayer('openstreetmap').add_to(map)
folium.TileLayer('CartoBD Voyager', attr='CartoDB Voyager').add_to(map)
folium.TileLayer('Stamen Terrain', attr='Stamen Terrain').add_to(map)

folium.LayerControl().add_to(map)

# Add a marker to the map
titulo_popup = '<b>Lisboa, Portugal</b>'
texto_popup = 'Lisboa é a capital de Portugal e a cidade mais populosa do país. Tem uma população de 506 892 habitantes, dentro dos seus limites administrativos. Na Área Metropolitana de Lisboa, residem 2 821 697 pessoas (2011), sendo por isso a maior e mais populosa área metropolitana do país. Lisboa é o centro político de Portugal, sede do Governo e da residência do chefe de Estado. É o principal centro económico do país, sendo uma das cidades mais desenvolvidas da União Europeia, com um PIB superior à média da região. É ainda a cidade mais rica de Portugal, com um PIB per capita de 23 559 euros (paridade do poder de compra), tendo a segunda maior conta bancária domiciliada na cidade, apenas atrás de Madrid, na Península Ibérica. É a nona cidade mais rica do sul da Europa, depois de Madrid, Barcelona, Milão, Roma, Atenas, Nápoles, Turim e Valência.'
caminho_imagem = "lisboa.png"
conteudo_html = f"""
    <h1>{titulo_popup}</h1>
    <p>{texto_popup}</p>
    <img src="{caminho_imagem}" alt="Lisboa" style="width: 100%; height: auto;  aspect-ratio: 1 / 1;">
"""

folium.Marker(
    [latitude, longitude], 
    popup=folium.Popup(conteudo_html, max_width=300),
    icon=folium.Icon(color='green', icon='info-sign'),
    tooltip='Sporting'
).add_to(map)

titulo_popup = '<b>Lisboa Lisboa, Portugal</b>'


map.save("map.html")