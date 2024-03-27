from http.server import HTTPServer, BaseHTTPRequestHandler
import json

products = {}


class Chocolate:
    def __init__(self, chocolate_type, weight, taste, relleno):
        self.candy_type = chocolate_type
        self.weight = weight
        self.taste= taste
        self.relleno = relleno

class Tabletas(Chocolate):
    def __init__(self, weight, taste):
        super().__init__("Tableta", weight, taste)


class Bombones(Chocolate):
    def __init__(self, weight, taste, relleno):
        super().__init__("Bombon", weight, taste, relleno)

class Trufas(Chocolate):
    def __init__(self, weight, taste, relleno):
        super().__init__("Trufa", weight, taste, relleno)


class ChocolateFactory:
    @staticmethod
    def create_chocolate(chocolate_type, weight, taste, relleno):
        if chocolate_type == "tableta":
            return Tabletas(weight, taste)
        elif chocolate_type == "bombon":
            return Trufas(weight, taste, relleno)
        elif chocolate_type == "trufa":
            return Trufas(weight, taste, relleno)
        else:
            raise ValueError("Tipo de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateServices:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        chocolate_type = data.get("chocolate_type", None)
        weight = data.get("weight", None)
        taste = data.get("taste", None)
        relleno =data.get("relleno", None)

        chocolate = self.factory.create_chocolate(
            chocolate_type,weight,taste,relleno
        )
        products[len(products) + 1] = chocolate
        return chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in products.items()}

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in products:
            chocolate = products[chocolate_id]
            weight = data.get("weight", None)
            taste = data.get("taste", None)
            relleno = data.get("relleno", None)
            if weight:
                chocolate.weight = weight
            if taste:
                chocolate.taste = taste
            if relleno:
                chocolate.relleno = relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in products:
            del products[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:
            return None


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_service = ChocolateServices()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_service.list_chocolates()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_service.update_chocolate(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()