import requests
from datetime import datetime
import smtplib

MY_LAT = 35.468491 # Your latitude
MY_LON = -97.521263 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LON-5 <= iss_longitude <= MY_LON+5:
    iss_near = True
else:
    iss_near = False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow().hour

def send_email(message):
    my_gmail = "NyetWork001@gmail.com"
    my_yahoo = "NyetWork001@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        with open("emailpass.txt", "r") as f:
            password = f.read()

        connection.login(my_gmail, password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_yahoo,
                            msg=f"Subject:ISS is near!\n\n{message}")

# iss_near = True # DEBUG
if iss_near:
    if time_now < sunrise or time_now > sunset:
        message = f"ISS is at {iss_latitude}, {iss_longitude}."
        send_email(message)

