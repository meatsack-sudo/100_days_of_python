import requests
import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

API_KEY = config["owm"]["api_key"]
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": 41.642370,
    "lon": -93.517740,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
print(f"Status Code: {response.status_code}\n")

timestamp = response.json()["list"]

days_condition = []

will_rain = False

for data in timestamp:

    if data["weather"][0]["id"] < 700:
        #print(f"{data["weather"][0]["description"]}\n")
        will_rain = True
        days_condition.append(data["weather"][0]["description"])

if will_rain:
    print("Bring an Umbrella")
#print(response.json())



