
import requests

# We need coordinates to get weather data
latitude = 28.6712909   # ghaziabad latitude
longitude = 77.4672862   # ghaziabad longitude

# weather function block
def get_weather(latitude,longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

    # Make the request
    response = requests.get(url)
    data = response.json()
    temperature = data["current"]["temperature_2m"]
    return f"temperature in ghaziabad = {temperature}"

ghaziabad = get_weather(28.64,77.48)
delhi = get_weather(28.38,77.12)
tokyo = get_weather(35.65,139.83)
print(f"ghaziabad temperature = {ghaziabad}")
print(f"delhi temperature = {delhi}")
print(f"tokyo temperature = {tokyo}")

#weather is good
