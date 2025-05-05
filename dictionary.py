weather_data = {
    "New York" : 22,
    "London" : 18,
    "Tokyo" : 25,
    "Mumbai":30
}

city = input("Enter the name of the city: ")

if city in weather_data:
    print(f"{city} is {weather_data[city]} Celcius right now.")
else:
    print("City not found in the weather data.") 