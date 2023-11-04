import requests


# Write a program that fetches and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/.
# The user should only be shown the joke text.
url = 'https://api.chucknorris.io/jokes/random';
response = requests.get(url);
if response.status_code == 200:
    print(response.json()['value']);
else:
    print('error');


# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation. You must register for the service to receive the API key required for making API requests.
# Furthermore, find out how you can convert Kelvin degrees into Celsius.
municipalityName = input("input name of a municipality: ");
appid = '54c740c16be729af0594cec1a230322b&units=metric';
url = f'https://api.openweathermap.org/data/2.5/weather?q={municipalityName}&APPID={appid}&units=metric';
response = requests.get(url);
if response.status_code == 200:
    # weather condition description text and temperature in Celsius degrees.
    data = response.json();
    weatherDescription = data['weather'][0]['description'];
    temperature = data['main']['temp']
    print(f"weather condition is '{weatherDescription}' and temperature is {temperature} in Celsius degrees");
else:
    print('not found location');
