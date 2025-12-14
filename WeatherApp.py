import requests

def get_weather_data(city, api_key, units="metric"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            print("Error:", data.get("message", "Could not fetch weather data"))
            return None
        
        return data
    except requests.exceptions.RequestException:
        print("Network error! Please check your internet connection.")
        return None

def display_weather(data, units):
    temp_unit = "°C" if units == "metric" else "°F"
    
    city = data['name']
    weather = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    humidity = data['main']['humidity']

    print("\n---------- Current Weather ----------")
    print("===================================")
    print(f"City:       {city}")
    print(f"Condition:  {weather}")
    print(f"Temperature: {temp}{temp_unit}")
    print(f"Humidity:   {humidity}%")
    print("===================================\n")

def main():
    print("---------- Simple Weather App ----------")
    
    city = input("Enter city name: ").strip()
    
    if not city:
        print("Please enter a valid city name.")
        return
    choice = input("Choose temperature unit(celcuis (C) or fahrenheit (F)): ").lower()
    units = "metric" if choice == "c" else "imperial"
    
    api_key = "473d8398adb887317292e14aab16b750"
    
    data = get_weather_data(city, api_key, units)
    
    if data:
        display_weather(data, units)

main()
