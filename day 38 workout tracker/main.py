import requests
from datetime import datetime, timedelta

#If this was ever going to run in prod these constants would need to be put into an env variable.
NUTRITIONIX_APP_ID = "3a399ec8"
NUTRITIONIX_API_KEY = "58a805278ef538b8aa7fbd9506589890"
SHEETY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

nutritionix_host_domain = "https://trackapi.nutritionix.com"
nutritionix_endpoint = "/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/4eb3e425f8c9d43b430d4b9317fe8142/myWorkoutsPython/workouts"
sheety_header = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}

now = datetime.now()
todays_date = now.strftime("%m-%d-%Y")
the_time = now.strftime("%H:%M:%S")

headers = {
    "x-app-id" : NUTRITIONIX_APP_ID,
    "x-app-key" : NUTRITIONIX_API_KEY
}

query = input("What workout did you do today? ")

params = {
    "query" : query,
    "weight_kg" : 99.8,
    "height_cm" : 177.8,
    "age" : 30
}

nutritionix_response = requests.post(url=nutritionix_host_domain+nutritionix_endpoint, json=params, headers=headers)
nutritionix_data = nutritionix_response.json()

sheety_response = requests.get(url=sheety_endpoint, headers=sheety_header)

if sheety_response.status_code == 200:
    sheety_rows_data = sheety_response.json()
    next_available_row = sheety_rows_data["workouts"][-1]["id"] + 1
else:
    print(f"Failed to fetch data. Status Code: {sheety_response.status_code}")

for workout in nutritionix_data["exercises"]:

    spreadsheet_data = {
        "workout" : {
            "date" : todays_date,
            "time" : the_time,
            "exercise" : workout["user_input"].title(),
            "duration" : workout["duration_min"],
            "calories" : workout["nf_calories"],
            "id" : next_available_row,
        }
    }

    sheety_add_row = requests.post(url=sheety_endpoint, json=spreadsheet_data, headers=sheety_header)