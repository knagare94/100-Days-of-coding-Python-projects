import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "tester123"
TOKEN = "b6fbf5bbf56bf6f65b6fb6f6fb6f"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()


post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometer did you cycle today? "),
}

# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)

update_endpoint = f"{post_endpoint}/20230218"

update_config = {
    "quantity": "4"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
