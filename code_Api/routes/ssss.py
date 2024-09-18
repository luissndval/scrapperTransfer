import json
import os
import subprocess

from flask import Blueprint, request, jsonify

# Obtener la ruta principal (subir dos niveles desde el archivo actual)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
USER_DATA_FILE = os.path.join(DATA_DIR, 'user_data.json')
SALDO_FILE = os.path.join(DATA_DIR, 'saldo.json')

api_get_saldo_bp = Blueprint('api_get_saldo_bp', __name__)

@api_get_saldo_bp.route('/consultar_saldo', methods=['POST'])
def consultar_saldo():
    data = request.get_json()
    tipo_cuenta = data.get('TipoCuenta')
    tipo_doc = data.get('TipoDoc')
    documento = data.get('documento')
    password = data.get('password')

    # Almacenar los datos en un archivo temporal
    user_data = {
        'tipo_cuenta': tipo_cuenta,
        'tipo_doc': tipo_doc,
        'documento': documento,
        'password': password
    }

    with open(USER_DATA_FILE, 'w') as f:
        json.dump(user_data, f)

    try:
        # Ejecutar la automatización para obtener el saldo
        result = subprocess.run(['behave', 'ScrapTransfer/features/get_Saldo.feature'], capture_output=True, text=True, check=True)
        message = result.stdout

        # Leer el saldo desde el archivo temporal
        with open(SALDO_FILE, 'r') as f:
            saldo_data = json.load(f)
            saldo_value = saldo_data.get('saldo', 'Saldo no encontrado')

    except subprocess.CalledProcessError as e:
        message = f"Error al ejecutar Behave: {e.output}"
        saldo_value = None
    except Exception as e:
        message = f"Error inesperado: {str(e)}"
        saldo_value = None

    return jsonify({
        'status': 'success' if saldo_value is not None else 'failure',
        'amount_available': saldo_value
    }), 200 if saldo_value is not None else 500