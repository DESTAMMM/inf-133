from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estudiantes=[
    {
        "id":1,
        "nombre": "Pedrito",
        "apellido": "Almanza"
    }
]
class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        id self.path=='/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headerds()
            self.sen

