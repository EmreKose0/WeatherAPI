import datetime as dt
import requests
import os

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = open('C:\\Users\\emrek\\OneDrive\\Masaüstü\\weatherAPI\\venv\\api_key','r').read()
CITY ="ISTANBUL"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

def kelvin_to_celsius_fahr(kelvin):
    celsius = kelvin - 273.15
    fahr = celsius * (9/5) + 32
    return celsius,fahr


response = requests.get(url).json()

temp_kelvin =response['main']['temp']
temp_cels, temp_fahr = kelvin_to_celsius_fahr(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_cels, feels_like_fahr = kelvin_to_celsius_fahr(feels_like_kelvin)

description = response['weather'][0]['description']

wind_speed = response['wind']['speed']

print(f"Temp in {CITY}: {temp_cels:.2f} C or {temp_fahr} F")
print(f"Temp in {CITY}: feels like: {feels_like_cels:.2f} C or {feels_like_fahr} F")
print(f"Wind Speed in {CITY}: {wind_speed} km/h")
print(f"General Weather in {CITY}: {description}")


