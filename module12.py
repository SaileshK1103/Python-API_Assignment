# 1. Write a program that fetches and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.


'''
import requests
def random_joke():
    try:
        api_url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(api_url)
        response.raise_for_status()
        joke_data = response.json()
        print (joke_data['value'])
    except requests.exceptions.RequestException as e:
        return (f"Error parsing JSON: {e}")

random_joke()

'''
import requests

# 2. Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality and then prints out
# the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation. You must register for the service to receive the API key required
# for making API requests. Furthermore, find out how you can convert Kelvin degrees into Celsius.

from __init__ import weather_info

def get_weather(municipality, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            condition = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            print(f"Weather Condition: {condition}")
            print(f"Temperature: {temperature}°C")
        else:
            print("Failed to load weather data. Please try again")
    except requests.exceptions.RequestException as e:
        print(f"Error API request: {e}")

if __name__ == "__main__":
    api_key = weather_info()
    municipality = input("Enter Municipality: ")
    get_weather(municipality, api_key)
