from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load variables from .env file
api_key = os.getenv("API_KEY")

city_name = "Mathura"

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}")

data = response.json()
#print(data)

total = len(data['list'])

for i in range(total):
    print(data['list'][i]['dt_txt'])


