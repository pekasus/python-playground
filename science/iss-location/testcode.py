import requests
from datetime import datetime

MY_LAT = 35.468491
MY_LON = -97.521263
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# print(data)
# print(latitude, longitude)
#

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
