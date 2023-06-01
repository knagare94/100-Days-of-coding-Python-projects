import requests
from datetime import datetime


GENDER = "MALE"
WEIGHT_KG = "62"
HEIGHT_CM = "175"
AGE = "22"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0ae747fd6cb07116fc2636454d362994/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

API_KEY = "4de530456a825d167404c9aefa89ebb4"
APP_ID = "1ec14232"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

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

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            "testappa",
            "Hacker@123",
        )
    )

    print(sheet_response.text)
