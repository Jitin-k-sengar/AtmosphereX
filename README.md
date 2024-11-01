# Overview
This application provides real-time weather forecasts, 5-day weather predictions, and air pollution data for any specified location. It utilizes the OpenWeatherMap API to fetch data and displays it in a user-friendly format.

# Features
Current Weather Forecast: Get the current weather conditions including temperature, humidity, wind speed, and more.
5-Days Forecast: View detailed weather forecasts for the next five days.
Air Pollution Forecast: Check the air quality index and pollution levels for various components like CO, NO2, O3, PM2.5, and PM10.
User -Friendly Interface: The application includes a simple command-line interface that guides users through their options.

# Requirements
* Python 3.x
* Required libraries:
    - requests
    - colorama
    - python-dotenv

# Setup Instructions
1. Clone the repository:

    git clone <repository-url>
    cd <repository-directory>
    
2. Install the required libraries:

    pip install requests colorama python-dotenv
   
3. Create a .env file in the root directory of the project and add your OpenWeatherMap API key:

    API_KEY=your_api_key_here
   
4. Run the application:
    python main.py


# Usage
Upon running the application, you will see a logo and a menu with the following options:

1. Current Weather Forecast
2. 5-Days Forecast
3. Air Pollution Forecast
4. Exit

![image](https://github.com/user-attachments/assets/e8efa5e4-ff88-4376-a904-4a27a45050aa)

Select an option by entering the corresponding number and follow the prompts to enter the desired location.

![image](https://github.com/user-attachments/assets/7121ecc3-e80d-4a47-89c0-ef42c776c005)



