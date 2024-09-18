import os
import sys

from flask import Flask
from flask_jwt_extended import JWTManager
from routes import api_guardar_datos_cliente_bp
from routes import api_send_money_bp
from routes import api_register_bp
from routes import api_login_bp
from routes import api_obtener_datos_bp
# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Cambia esto por una clave secreta segura
app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Asegúrate de que el token esté en los headers
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'

jwt = JWTManager(app)

# Registrar las rutas de los blueprints
# app.register_blueprint(api_get_saldo_bp, url_prefix='/api')
app.register_blueprint(api_send_money_bp, url_prefix='/api')
app.register_blueprint(api_guardar_datos_cliente_bp, url_prefix='/api')
app.register_blueprint(api_register_bp, url_prefix='/api')
app.register_blueprint(api_login_bp, url_prefix='/api')
app.register_blueprint(api_obtener_datos_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
