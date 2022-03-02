import requests
from key import api_key
#Algún lugar por Australia
# LAT = -33.868820
# LONG = 151.209290
#GDL
LAT = 35.0075
LONG = -84.1895
key = api_key
open_weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": key,
}

response = requests.get(url=open_weather_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()["hourly"]

rain = False

for hour in weather_data[:12]:
    if hour["weather"][0]["id"] < 700:
        rain = True

if rain:
    print("Va llober, mijo, lleva tu umbrella")
else:
    print("No te priopuques, no va llober")
