import requests
from datetime import datetime, timedelta

USERNAME = "meatsack"
TOKEN = "meatsackisamazingandsuperdupersmartlikeithinksoatleastmaybekindof"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "meatsackisamazingandsuperdupersmartlikeithinksoatleastmaybekindof",
    "username": "meatsack",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# respone = requests.post(url=pixela_endpoint, json=user_params)
# print(respone.text)

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id" : "graph1",
    "name" : "Totes graph",
    "unit" : "Days",
    "type" : "float",
    "color" : "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
pixel_params = {
    "date" : today_formatted,
    "quantity" : "1.0",
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{today_formatted}"
update_pixel_params = {
    "quantity" : "10.0",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20240630"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)