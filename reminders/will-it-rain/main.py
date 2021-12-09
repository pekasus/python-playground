import requests

with open("pass.txt", "r") as f:
    api_key = f.read()

lat = 35.4676
lon = -97.5164

# lat = -12.138180 # Brazil
# lon = -49.168129 # Brazil

city_name = "Oklahoma City"
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
url_base = "http://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url_base, params=parameters)
weather_data = response.json()
hourly_data = weather_data['hourly']
for hour in hourly_data[0:12]:
    hour_id = hour['weather'][0]['id']
    print(hour_id)
    if hour_id < 700:
        print("Bring an umbrella")
        break

