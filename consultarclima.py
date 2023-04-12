import requests
import json
from geopy.geocoders import Nominatim
import conexion_mongo as dbase
from app import nombreUser

db = dbase.dbConexion()

def obtener_loca():
    collection = db['usuario']
    usuario_encontrado = collection.find_one({"usuario": nombreUser})
    ubic = usuario_encontrado["ubicacion"]
    # Cambia "my_app_name" por el nombre de tu aplicación
    geolocator = Nominatim(user_agent="my_app_name")

    location = geolocator.geocode(ubic)

    lat = location.latitude
    lon = location.longitude
    clima(lat, lon)

def clima(lat,lon):
    API="2117ed898541126a01a020cb4ef22941"
    lat=lat
    lon=lon
    url= f'https://api.openweathermap.org/data/2.5/weather?={lat}&lon={lon}&appid={API}&units=metric'

    res= requests.get(url)

    data=res.json()

    temp= data["main"]["temp"]
    hume = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data ["weather"][0]["description"]

    print("Temperatura: ",temp)
    print("Humedad: ", hume)
    print("Velocidad del viento: ",wind_speed)
    print("Descripcion: ", description)