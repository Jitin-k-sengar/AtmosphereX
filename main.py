from logo import display_logo
from colorama import Fore
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load variables from .env file
api_key = os.getenv("API_KEY")
    
    
def input_city():
    city = input(Fore.YELLOW + "Enter the city name: ")
    return city

def Current_weather(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    if  response.status_code == 200:
        data = response.json()
        
        weather_main = data['main']
        
        Temperature = int(weather_main['temp'] - 273.15)
        min_temp = int(weather_main['temp_min'] - 273.15)
        max_temp = int(weather_main['temp_max'] - 273.15)
        humidity =  weather_main['humidity']
        pressure  = weather_main['pressure']
        



        print(Fore.BLUE + f"Temperature : {Temperature}°C")
    

while True:
    display_logo()
    city_name = input_city()
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")


    if  response.status_code == 200:
        data = response.json()
        
        
        weather_main = data['main']
        
        Temperature = int(weather_main['temp'] - 273.15)
        print(Fore.BLUE + f"Temperature : {Temperature}°C")
        
        pressure =  weather_main['pressure']
        print(f"Pressure : {pressure} hPa")
        
        humidity  = weather_main['humidity']
        print(f"Humidity : {humidity}%")
        
        sea_level  = weather_main['sea_level']
        print(f"Sea Level : {sea_level} m")
        
        ground_level =  weather_main['grnd_level']
        print(f"Ground Level : {ground_level} m")

        
        print(f"Temperature Maximum: {int(weather_main['temp_max']-273.15)}°C")
        print(f"Minimum :  {int(weather_main['temp_min']-273.15)}°C")
    else:
        print("Internet not Working")
        