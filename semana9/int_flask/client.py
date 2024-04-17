import requests

url='http://localhost:5000'

response = requests.get(url)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)


nombre="Juan"
url1=url+f"/saludar?nombre={nombre}"
response1 = requests.get(url1)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response1.text)
else:
    print("Error al conectar con el servidor:", response.status_code)


url2=url+f"/sumar?a=5&b=3"
response2 = requests.get(url2)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response2.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

url3=url+f"/palindromo?cadena=reconocer"
response3 = requests.get(url3)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response3.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

url4=url+f"/contar?cadena=exepciones&vocal=e"
response4 = requests.get(url4)
if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response4.text)
else:
    print("Error al conectar con el servidor:", response.status_code)