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

# Usage
Upon running the application, you will see a logo and a menu with the following options:

1. Current Weather Forecast
2. 5-Days Forecast
3. Air Pollution Forecast
4. Exit

![image](https://github.com/user-attachments/assets/e8efa5e4-ff88-4376-a904-4a27a45050aa)

Select an option by entering the corresponding number and follow the prompts to enter the desired location.

![image](https://github.com/user-attachments/assets/7121ecc3-e80d-4a47-89c0-ef42c776c005)


# Example Commands
 To get the current weather for New York:

     Enter your choice: 1
     Enter the Location: New York

To check air pollution in Los Angeles:

     Enter your choice: 3
     Enter the Location: Los Angeles

# Error Handling
If the application encounters an invalid location or there is no internet connection, it will display an appropriate error message.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bug reports.

# Contact
For any inquiries or support, please contact the project maintainer at jitin.k.sengar@gmail.com.
