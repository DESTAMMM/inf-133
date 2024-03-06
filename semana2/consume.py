from zeep import Client      
from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
) 

Result = client.serviceNumberToWords(5) 
print(result)

def saludar(nombre):    
    return "Hola,{ }!".format(nombre)

dispatcher =SoapDispatcher(
    "Ejemplo-soap-server",  
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace="http://localhost"

)
dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str}
    args={"nombre":str}
)

server=HTTPServer(("0.0.0.0",8000), SOAPHandler)
server.dispatcher=dispatcher
print("Server SOAP iniciado en http://localhost:8000/")
sever.serve_forever()