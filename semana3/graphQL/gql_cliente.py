import requests

query = """
    {
        estudiante(nombre, id:2){
            nombre
        }
        estudiante(id:2,nombre, apellido){
            nombre 
            apellido
        }
    }
"""
url = 'http://localhost:8000/graphql'

response = requests.post(url, json={'query': query})
print(response.text)