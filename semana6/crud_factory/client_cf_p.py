import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type": "tableta",
    "weight": "600 g",
    "taste": "chocolate blanco"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "bombon",
    "weight": "300 g",
    "taste": "chocolate negro",
    "relleno": "durazno"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "trufa",
    "weight": "300 g",
    "taste": "chocolate negro",
    "relleno": "frutilla"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

response = requests.get(url=url)
print(response.json())