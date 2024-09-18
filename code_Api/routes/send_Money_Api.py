import json
import os
import subprocess

from flask import Blueprint, request, jsonify

# Obtener la ruta principal (subir dos niveles desde el archivo actual)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
USER_DATA_FILE = os.path.join(DATA_DIR, 'user_data.json')
SALDO_FILE = os.path.join(DATA_DIR, 'saldo.json')

api_send_money_bp = Blueprint('api_send_money_bp', __name__)


@api_send_money_bp.route('/send_money', methods=['POST'])
def send_money():
    data = request.get_json()

    # Datos de la transferencia
    destination_account = data.get('destination_account')
    amount_to_send = data.get('amount_to_send')
    send_email_to = data.get('send_email_to')

    # Leer los datos de inicio de sesión desde el archivo temporal
    try:
        with open(USER_DATA_FILE, 'r') as f:
            user_data = json.load(f)

        tipo_cuenta = user_data['tipo_cuenta']
        tipo_doc = user_data['tipo_doc']
        documento = user_data['documento']
        password = user_data['password']

        result = subprocess.run(['behave', 'ScrapTransfer/features/send_Money.feature'], capture_output=True, text=True,
                                check=True)
        message = result.stdout

    except FileNotFoundError:
        return jsonify({"error": "No se encontraron los datos de inicio de sesión"}), 400
    except json.JSONDecodeError:
        return jsonify({"error": "Error al decodificar los datos de inicio de sesión"}), 400


    # Aquí agregarías la lógica para iniciar sesión en el banco y realizar la transferencia
    # Utilizando `tipo_cuenta`, `tipo_doc`, `documento`, `password`, `destination_account`, `amount_to_send`, y `token`

    response = {
        "message": "Transferencia realizada exitosamente",
        "details": {
            "destination_account": destination_account,
            "amount_to_send": amount_to_send,
            "send_email_to": send_email_to,
        }
    }
    return jsonify(response)
