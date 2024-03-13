import requests

url = 'http://localhost:8000/graphql'

query = """
    {
        estudianteCarrera(carrera: "Arquitectura"){
            id
            nombre
            apellido
            carrera
        }
    }
"""

query_crear = """
mutation {
        crearEstudiante(nombre: "Luis", apellido: "Almanza", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

response = requests.post(url, json={'query': query})
print(response.text)

query_update = """
mutation {
        updateEstudiante(id: 2, carrera: "Antropologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_update})
print(response_mutation.text)

query_lista = """
    {
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
response = requests.post(url, json={'query': query_lista})
print(response.text)