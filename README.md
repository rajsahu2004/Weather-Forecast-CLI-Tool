# Weather Forecast CLI Tool

This is a command-line tool that accepts a city name and returns the current weather forecast using the OpenWeatherMap API.

## Prerequisites

- Python 3.x installed
- OpenWeatherMap API key

## Installation

1. Clone the repository:

        git clone https://github.com/rajsahu2004/Weather-Forecast-CLI-Tool.git

2. Navigate to the project directory:

        cd weather-forecast-cli

3. Install the required dependencies:

        pip install -r requirements.txt

## Usage

Run the `weather.py` script followed by the name of the city you want to get the weather forecast for.

        python weather.py CITY_NAME

Replace `CITY_NAME` with the actual name of the city. Make sure to set your OpenWeatherMap API key as an environment variable named `API_KEY` or provide it directly in the `weather.py` script.

The tool will display the current weather conditions, temperature, humidity, and wind speed for the specified city.

## Example

Here's an example of running the command-line tool by providing the city name as "Chandigarh"

        python weather.py Chandigarh

The tool will make a request to the OpenWeatherMap API and fetch the current weather forecast for Chandigarh. It will then display the weather conditions, temperature, humidity, and wind speed for the city.

### Example output:

        *****Chandigarh*****
        Weather: Clear
        Temperature: 27.15
        Humidity: 65
        Wind Speed: 2.57

### Demo Video

![Demo Video](media/videos/demo.mp4)

## API Key

To use the OpenWeatherMap API, you need an API key. If you don't have one, you can sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
