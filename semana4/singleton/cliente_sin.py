import requests

url = "http://localhost:8000/"

# GET /player
response = requests.request(method="GET", url=url + "player")
print(response.text)

response = requests.request(method="POST", url=url + "player/damage", json={"damage": 25})
print(response.text)