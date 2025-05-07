import streamlit as st
import folium
import requests
from streamlit import components

# Título de la aplicación
st.title("🌎 Gemelo Digital de Valledupar")
st.write("Este es un prototipo inicial para visualizar datos de vegetación, clima y biodiversidad.")

# Mapa de Valledupar
m = folium.Map(location=[10.4637, -73.2499], zoom_start=12)
folium.Marker([10.4637, -73.2499], popup="Ubicación de Valledupar").add_to(m)
map_html = m._repr_html_()  # Convierte el mapa de Folium en una cadena HTML
components.v1.html(map_html, height=500)

# API key de OpenWeatherMap
api_key = "8b1621940a22861f049d6dc05c514828"  # Asegúrate de que esta clave es correcta

# Ciudad para obtener el clima
ciudad = "Valledupar"

# URL de la API de OpenWeatherMap (con HTTPS)
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

# Realizamos la solicitud a la API
respuesta = requests.get(url)

# Convertimos la respuesta a JSON
data = respuesta.json()

# Verificamos si la API respondió correctamente
if data.get("cod") != 200:
    st.write("❌ Error al obtener los datos del clima.")
    st.write(data)  # Muestra el error de la API para depuración
else:
    # Extraemos la información del clima si la respuesta es correcta
    main_data = data.get("main", {})
    weather_data = data.get("weather", [{}])[0]
    
    if main_data:
        temperature = main_data.get("temp", "No disponible")
        humidity = main_data.get("humidity", "No disponible")
        weather_description = weather_data.get("description", "No disponible")
        
        # Mostrar la información del clima
        st.write(f"🌡️ Temperatura: {temperature}°C")
        st.write(f"💧 Humedad: {humidity}%")
        st.write(f"🌥️ Descripción: {weather_description}")
    else:
        st.write("❌ No se encontraron datos de clima.")
