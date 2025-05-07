import folium

mapa = folium.Map(location=[10.4741, -73.2436], zoom_start=13)  # Coordenadas de Valledupar
mapa.save("mapa_valledupar.html")
