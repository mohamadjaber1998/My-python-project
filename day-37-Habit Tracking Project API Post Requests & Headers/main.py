import requests
from datetime import datetime

TOKEN = "322kn3morn23r23rno2"
USERNAME = "iammohamadjaber"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime(year=2022, month=10, day=19)

post_pixel = f"{graph_endpoint}/graph1"

post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6"
}

# response = requests.post(url=post_pixel, json=post_pixel_params, headers=headers)
# print(response.text)

edite_pixel = f"{post_pixel}/20221019"

edite_pixel_params = {
    "quantity": "2"
}

response = requests.delete(url=edite_pixel, json=edite_pixel_params, headers=headers)
print(response.text)
