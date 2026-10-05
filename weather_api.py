import requests

# City to search for
city = "London"

# Free public weather API
url = f"https://wttr.in/{city}?format=j1"

try:
    # Get data from the API
    response = requests.get(url)
    response.raise_for_status()

    # Convert JSON response into Python data
    data = response.json()

    # Process the weather information
    current_weather = data["current_condition"][0]

    temperature = current_weather["temp_C"]
    feels_like = current_weather["FeelsLikeC"]
    humidity = current_weather["humidity"]
    description = current_weather["weatherDesc"][0]["value"]

    # Display useful output
    print("===== Weather Report =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description}")

except requests.exceptions.RequestException as error:
    print("Unable to connect to the API.")
    print(f"Error: {error}")

except (KeyError, IndexError):
    print("The API returned unexpected data.")