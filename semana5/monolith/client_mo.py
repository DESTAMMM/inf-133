import requests
url = "http://localhost:8000/posts"

response = requests.get(f"{url}")

print(response.text)