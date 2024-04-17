from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre=request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error": "se requiere un nombre en los parametros de la URL."}),400,
        )
    return jsonify ({"mensaje": f"¡Hola, {nombre}!"})

@app.route('/sumar', methods=['GET'])
def sumar():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    c=a+b
    if not a or b:
        return(
            jsonify({"error": "se requiere un dato en los parametros de la URL."}),400,
        )
    return jsonify ({"mensaje": f"suma={c}"})

@app.route('/palindromo', methods=['GET'])
def palindromo():
    cadena=str(request.args.get("cadena"))
    if not cadena:
        return(
            jsonify({"error": "se requiere un dato en los parametros de la URL."}),400,
        )
    elif cadena==cadena[::-1]:
        return jsonify ({"mensaje": f"la palabra: {cadena} es palindromo"})
    else:
        return jsonify ({"mensaje": f"la palabra: {cadena} no es palindromo"})
    
if __name__ == "__main__":
    app.run()

@app.route('/contar', methods=['GET'])
def contar():
    cad=str(request.args.get("cadena"))
    vocal=str(request.args.get("vocal"))
    cd=0;
    if not cad:
        return(
            jsonify({"error": "se requiere un dato en los parametros de la URL."}),400,
        )
    for caracter in cad:
        if caracter==vocal:
            cd=cd+1

    return jsonify ({"mensaje": f"la cantidad de vocales {vocal} es {cd}"})
if __name__ == "__main__":
    app.run()