import requests
import json

def get_weather(api_key, city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    city = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    print(f"Weather in {city}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    api_key = "5612d31dcb3ea7ba3ebf4ee673e8a990"  # Replace with your API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if  __name__== "__main__":
       main()