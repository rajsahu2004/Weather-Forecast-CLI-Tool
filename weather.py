import requests
import sys
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

# Get weather data from OpenWeatherMap API
def get_weather_data(city, api_key):
    """_summary_

    Args:
        city (string): Name of the city you want to know the weather of
        api_key (string): API Key of the Openweather account

    Returns:
        object: weather data 
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data =  response.json()
        return weather_data
    else:
        # print(f'\033[91mError: {response.status_code} \033[00m')
        sys.exit(1)

def parse_weather(weather_data):
    """_summary_

    Args:
        weather_data (object) : weather data
    """
    try:
        weather = weather_data['weather'][0]['main']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        print(f'*****{weather_data["name"]}*****')
        print(f'Weather: {weather}')
        print(f'Temperature: {temperature}')
        print(f'Humidity: {humidity}')
        print(f'Wind Speed: {wind_speed}')
    except:
        print('\033[91mError: Invalid response from the API.\033[00m')
        sys.exit(1)
        
        
def main():
    if len(sys.argv) < 2:
        print('\033[91mError: Please provide a city name.\033[00m')
        sys.exit(1)
    
    city = sys.argv[1]
    api_key = os.getenv('API_KEY')
    weather_data = get_weather_data(city, api_key)
    parse_weather(weather_data)
    
if __name__ == '__main__':
    main()