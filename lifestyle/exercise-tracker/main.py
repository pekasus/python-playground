import requests
from datetime import datetime

APP_ID = "bf33899a"
with open("pass.txt", "r") as f:
    API_KEY = f.read()

with open("pass2.txt", "r") as f:
    SHEET_ID = f.read()

with open("pass3.txt", "r") as f:
    SHEET_AUTH = f.read()

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = f"https://api.sheety.co/{SHEET_ID}/myWorkouts/workouts"

query = input("What activity did you do? ")
GENDER = "male"
WEIGHT_KG = 88.0
HEIGHT_CM = 182
AGE = 42

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

post_dict = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=post_dict, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# POST REQUEST WITHOUT AUTH
# sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)

sheet_header = {
    "Authorization": f"Bearer {SHEET_AUTH}"
}

sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)
