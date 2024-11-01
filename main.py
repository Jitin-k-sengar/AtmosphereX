from logo import display_logo
from colorama import Fore
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta, date
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def input_location():
    city = input(Fore.YELLOW + "Enter the Location : ")
    return city

def Options():
    print(Fore.MAGENTA + "1. Current Weather Forecast")
    print(Fore.MAGENTA + "2. 5-Days Forecast")
    print(Fore.MAGENTA + "3. Air Pollution Forecast")
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
    
    #  API endpoint for current weather
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    
    #  Check if the request was successful
    if  response.status_code == 200:
        
        clear_screen()
        display_logo()
        
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
        print(Fore.WHITE + f"Location : {city_name}  |  Date :  {datetime.now().strftime('%d %b %y')}  |  Time : {datetime.now().strftime('%I:%M %p')}")
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
        
    #   If the request was not successful, print an error message
    else:
        print(Fore.RED + "No Internet  Connection or Invalid Location")
    print("\n")
    input(Fore.RED + "Press Enter to  continue...")

def forecast(city_name):
    
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}")

    if  response.status_code == 200:
        
        clear_screen()
        display_logo()
        
        data = response.json()
        
        total = len(data['list'])
                        
        for k in range(0,total):
            
            forecast = data['list'][k]
            
            weather = forecast['weather']
            weather_main = forecast['main']
            wind = forecast['wind']
            clouds = forecast['clouds']
            date_time = data['list'][k]['dt_txt']
            
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
            
            # Convert to a datetime object
            dt_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

            # Format date as "30 Aug 2022" and time as "03:00 PM"
            date_str = dt_obj.strftime("%d %b %Y")
            time_str = dt_obj.strftime("%I:%M %p")
                
            print(Fore.RED + "*"*50)
            print(Fore.GREEN + f"Location : {city_name}  |  Date : {date_str}  |  Time : {time_str}")
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
            print("\n")
            
    else:
        print(Fore.RED + "No Internet  Connection or Invalid Location")
                  
    print("\n")
    input(Fore.RED + "Press Enter to  continue...")
        
def pollution(city_name):
    
    def get_lat_lon(city_name):
        
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
        
        if response.status_code == 200:
            data = response.json()
            latitude = data['coord']['lat']
            longitude = data['coord']['lon']
            return latitude, longitude
        
        else:
            print("Error fetching data:", response.status_code)
            return None,None
        
    lat,lon = get_lat_lon(city_name)
    
    if lat and lon:
        
        response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}")
        
        def evaluate_co(value):
            if value > 0 and  value <= 4400:
                return "Good", f"{Fore.GREEN}"
            elif value > 4400 and value <= 9400:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 9400 and value <= 12400:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 12400 and value <= 15400:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_o3(value):
            if value > 0 and  value <= 60:
                return "Good", f"{Fore.GREEN}"
            elif value > 60 and value <= 100:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 100 and value <= 140:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 140 and value <= 180:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_pm2_5(value):
            if value > 0 and  value <= 10:
                return "Good", f"{Fore.GREEN}"
            elif value > 10 and value <= 25:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 25 and value <= 50:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 50 and value <= 75:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"

        def evaluate_pm10(value):
            if value > 0 and  value <= 20:
                return "Good", f"{Fore.GREEN}"
            elif value > 20 and value <= 50:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 50 and value <= 100:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 100 and value <= 200:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_no2(value):
            if value > 0 and  value <= 40:
                return "Good", f"{Fore.GREEN}"
            elif value > 40 and value <= 70:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 70 and value <= 150:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 150 and value <= 200:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_so2(value):
            if value > 0 and  value <= 20:
                return "Good", f"{Fore.GREEN}"
            elif value > 20 and value <= 80:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 80 and value <= 250:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 250 and value <= 350:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_nh3(value):
            if value > 0 and  value <= 40:
                return "Good", f"{Fore.GREEN}"
            elif value > 40 and value <= 70:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 70 and value <= 150:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 150 and value <= 200:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        def evaluate_no(value):
            if value > 0 and  value <= 20:
                return "Good", f"{Fore.GREEN}"
            elif value > 20 and value <= 40:
                return "Fair", f"{Fore.LIGHTGREEN_EX}"
            elif value > 40 and value <= 60:
                return "Moderate", f"{Fore.BLUE}"
            elif  value > 60 and value <= 80:
                return "Poor", f"{Fore.LIGHTRED_EX}"
            else:
                return "Very Poor", f"{Fore.RED}"
            
        if  response.status_code == 200:
            
            clear_screen()
            display_logo()
            
            data = response.json()
            
            report = data['list'][0]['components']
            
            co = report['co']
            no = report['no']
            no2 = report['no2']
            o3 = report['o3']
            so2 = report['so2']
            pm2_5 = report['pm2_5']
            pm10 = report['pm10']
            nh3 = report['nh3']
            
            co_info,co_color = evaluate_co(co)
            no_info,no_color = evaluate_no(no)
            no2_info,no2_color = evaluate_no2(no2)
            o3_info,o3_color = evaluate_o3(o3)
            so2_info,so2_color = evaluate_so2(so2)
            pm2_5_info,pm2_5_color = evaluate_pm2_5(pm2_5)
            pm10_info,pm10_color = evaluate_pm10(pm10)
            nh3_info,nh3_color = evaluate_nh3(nh3)
            
            print("\n")
            print(Fore.WHITE + f"Location : {city_name}  |  Date :  {datetime.now().strftime('%d %b %y')}  |  Time : {datetime.now().strftime('%I:%M %p')}")
            print("\n")
            print(co_color + f"Carbon Monoxide         :   {co_info}")
            print(no_color + f"Nitrogen Dioxide        :   {no_info}")
            print(no2_color + f"Nitrogen Oxide          :   {no2_info}")
            print(o3_color + f"Ozone                   :   {o3_info}")
            print(so2_color + f"Sulfur Dioxide          :   {so2_info}")
            print(pm2_5_color + f"Particulate Matter 2.5  :   {pm2_5_info}")
            print(pm10_color + f"Particulate Matter 10   :   {pm10_info}")
            print(nh3_color + f"Nitrogen Hydride        :   {nh3_info}")
            
        else:
            print(Fore.RED + "No Internet  Connection")

    else:
        print(Fore.RED + "Incorrect Location")
        
    print("\n")
    input(Fore.RED + "Press Enter to  continue...")
    
while True:
    
    clear_screen()
    display_logo()
    choice = Options()
    
    if  choice == "1":
        city_name = input_location()
        Current_weather(city_name)
    
    elif choice ==  "2":
        city_name = input_location()
        forecast(city_name)
        
    elif choice == "3":
        city_name = input_location()
        pollution(city_name)
        
    elif choice == "4":
        exit(1)

    else:
        print(Fore.RED + "Invalid choice. Please choose a valid option.")
        print("\n")
        input(Fore.RED + "Press Enter to  continue...")
