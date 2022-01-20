import requests
import os

city = input('Please enter city ')

message = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ.get("api_key")}&units=metric'
response = requests.get(message)
city_weather = response.json()
n = city_weather['name']
t = city_weather['main']['temp']
p = city_weather['main']['pressure']
s = city_weather['wind']['speed']
d = city_weather['wind']['deg']
print(f'Weather forecast in {n} \nTemperature {t} C \nPressure {p} hPa \nWind {s} m/s \nWind direction {d} grade')



