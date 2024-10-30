from Logo.logo import display_logo
from Logo.logo2 import display_logo2
from colorama import Fore
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
import os
import requests

load_dotenv()  # Load variables from .env file
api_key = os.getenv("API_KEY")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def input_city():
    city = input(Fore.YELLOW + "Enter the Location : ")
    return city

def Options():
    print(Fore.MAGENTA + "1. Current Weather Forecast")
    print(Fore.MAGENTA +  "2. 5-Day Forecast")
    print(Fore.MAGENTA  + "3. Air Pollution Forecast")
    print(Fore.MAGENTA + "4. Exit\n")
    Choice = input(Fore.GREEN +  "Enter your choice: ")
    return  Choice

def degree_to_direction(degree):
    # Define the compass directions in order
    directions = [
        "North", "North-Northeast", "Northeast", "East-Northeast",
        "East", "East-Southeast", "Southeast", "South-Southeast",
        "South", "South-Southwest", "Southwest", "West-Southwest",
        "West", "West-Northwest", "Northwest", "North-Northwest"
    ]
    
    # Determine the index in the directions list
    index = int((degree + 11.25) % 360 / 22.5)
    return directions[index]

def unix_to_ist(unix_timestamp):
    # Convert Unix timestamp to datetime in UTC
    utc_time = datetime.fromtimestamp(unix_timestamp, tz=timezone.utc)
    # Convert UTC time to IST by adding 5 hours and 30 minutes
    ist_time = utc_time + timedelta(hours=5, minutes=30)
    return ist_time.strftime('%I:%M %p')


def Current_weather(city_name):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    if  response.status_code == 200:
        clear_screen()
        display_logo2()
        data = response.json()
        
        weather = data['weather']
        weather_main = data['main']
        wind = data['wind']
        clouds = data['clouds']
        sun = data['sys']
        
        weather_condition = weather[0]['main']
        Temperature = int(weather_main['temp'] - 273.15)
        humidity =  weather_main['humidity']
        pressure  = weather_main['pressure']
        sea_level = weather_main['sea_level']
        ground_level =  weather_main['grnd_level']
        wind_speed =  wind['speed']
        wind_deg = wind['deg']
        wind_direction = degree_to_direction(wind_deg)
        cloud = clouds['all']
        Sunrise = unix_to_ist(sun['sunrise'])
        Sunset = unix_to_ist(sun['sunset'])

        print("\n")
        print(Fore.BLUE + f"Location : {city_name}  |  Date :  {datetime.now().strftime('%d %b %y')}  |  Time : {datetime.now().strftime('%I:%M %p')}")
        print("\n")
        print(Fore.BLUE + f"Weather Condition : {weather_condition}")
        print(Fore.BLUE + f"Temperature       : {Temperature}°C")
        print(Fore.BLUE + f"Humidity          : {humidity}%")
        print(Fore.BLUE + f"Pressure          : {pressure} hPa")
        print(Fore.BLUE + f"Sea Level         : {sea_level} hpa")
        print(Fore.BLUE + f"Ground Level      : {ground_level} hpa")
        print(Fore.BLUE + f"Wind Speed        : {wind_speed} m/s")
        print(Fore.BLUE + f"Wind Direction    : {wind_direction}")
        print(Fore.BLUE + f"Clouds            : {cloud}%")
        print(Fore.BLUE + f"Sunrise           : {Sunrise}")
        print(Fore.BLUE + f"Sunset            : {Sunset}")

        print("\n")
        input(Fore.RED + "Press Enter to  continue...")


while True:
    clear_screen()
    display_logo()
    choice = Options()
    if  choice == "1":
        city_name = input_city()
        Current_weather(city_name)
        
    else:
        print(Fore.RED + "Invalid choice. Please choose a valid option.")
        print("\n")
        input(Fore.RED + "Press Enter to  continue...")
