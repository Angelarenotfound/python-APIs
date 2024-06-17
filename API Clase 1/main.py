from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario para almacenar los datos
datos = {}

# Definimos la ruta y método para recibir datos
@app.route('/guardar', methods=['GET'])
def guardar_datos():
    # Obtenemos los parámetros de la solicitud
    id = request.args.get('ID')
    param1 = request.args.get('p1')
    param2 = request.args.get('p2')

    # Verificamos si se proporcionaron todos los parámetros necesarios
    if id is None or param1 is None or param2 is None:
        return jsonify({'error': 'Faltan parámetros'}), 400

    # Guardamos los datos en el diccionario
    datos[id] = {
        'p1': param1,
        'p2': param2
    }

    return jsonify({'mensaje': 'Datos guardados correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=15750)
