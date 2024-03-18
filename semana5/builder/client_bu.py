import requests

url = "http://localhost:8000/pizza"

pizza = {
    "tamaño": "mediano",
    "masa": "mediana",
    "toppings": ["Jamon", "Queso", "peperoni", "oregano"]
}
response = requests.post(url, json=pizza)
print(response.json())