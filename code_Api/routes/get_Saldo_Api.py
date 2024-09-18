import json
from flask import Blueprint, request, jsonify
from code_Api.decorador.decorador import token_required
from db.models import SessionLocal, User
import subprocess

api_get_saldo_bp = Blueprint('api_get_saldo_bp', __name__)

@api_get_saldo_bp.route('/consultar_saldo', methods=['GET'])
@token_required
def consultar_saldo(current_user):
    db = SessionLocal()
    try:
        # Obtener los datos del usuario desde la base de datos
        user = db.query(User).filter_by(id=current_user.id).first()
        if not user:
            return jsonify({'status': 'failure', 'message': 'No se encontraron datos del cliente.'}), 400

        # Crear la estructura de datos del usuario
        user_data = {
            'tipo_cuenta': user.tipo_cuenta,
            'tipo_doc': user.tipo_doc,
            'documento': user.documento,
            'password': user.password
        }

        # Ejecutar la automatización para obtener el saldo pasando los datos del usuario
        result = subprocess.run(
            ['behave', 'ScrapTransfer/features/get_Saldo.feature'],
            input=json.dumps(user_data),
            capture_output=True,
            text=True,
            check=True
        )
        message = result.stdout

        # Obtener el saldo desde la salida del script (o cambiar este proceso para actualizar directamente en la DB)
        saldo_value = extract_saldo_from_message(message)  # Implementa esta función según cómo obtengas el saldo

        # Actualizar el saldo en la base de datos
        if saldo_value is not None:
            user.saldo = saldo_value
            db.commit()

        return jsonify({
            'status': 'success' if saldo_value is not None else 'failure',
            'data': user_data,
            'saldo_value': saldo_value if saldo_value is not None else 'Saldo no encontrado'
        }), 200 if saldo_value is not None else 500

    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'failure', 'message': f'Error al ejecutar Behave: {e.output}'}), 500
    except Exception as e:
        return jsonify({'status': 'failure', 'message': f'Error inesperado: {str(e)}'}), 500
    finally:
        db.close()

def extract_saldo_from_message(message):
    # Implementa esta función para extraer el saldo desde el mensaje de salida del script Behave
    # Esto depende de cómo el saldo es reportado en el mensaje
    try:
        # Ejemplo de extracción; ajusta según el formato del mensaje
        for line in message.splitlines():
            if "Saldo:" in line:
                return line.split(":")[1].strip()
    except Exception as e:
        return None
