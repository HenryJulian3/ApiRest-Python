from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuración de Swagger
SWAGGER_URL = '/swagger'  # Ruta donde estará la documentación
API_URL = '/static/swagger.json'  # Ubicación del archivo swagger.json
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Endpoint "Hola Mundo"
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hola Mundo API REST")

if __name__ == '__main__':
    app.run(debug=True)
