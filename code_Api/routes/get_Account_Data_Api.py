import os
import subprocess
from flask import Blueprint, jsonify
from db.models import User, ClientData, SessionLocal
from code_Api.decorador.decorador import token_required

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, r'ScrapTransfer\features\get_Saldo.feature')



client_data_global = []
api_obtener_datos_bp = Blueprint('api_obtener_datos_bp', __name__)

@api_obtener_datos_bp.route('/obtener_datos_cliente', methods=['GET'])
@token_required
def obtener_datos_cliente(current_user):
    global client_data_global
    db = SessionLocal()
    try:
        # Obtener los datos del cliente asociados con el usuario autenticado
        client_data = db.query(ClientData).filter_by(created_by=current_user.id).all()
        if not client_data:
            return jsonify({'status': 'failure', 'message': 'No se encontraron datos para el usuario autenticado.'}), 404

        user = db.query(User).filter_by(id=current_user.id).first()
        if not user:
            return jsonify({'status': 'failure', 'message': 'No se encontró el usuario.'}), 404

        # Serializar los datos para enviarlos en la respuesta
        client_data_global = [{
            'id': data.id,
            'tipo_cuenta': data.tipo_cuenta,
            'tipo_doc': data.tipo_doc,
            'documento': data.documento,
            'email': data.email,
            'password': user.password  # Asegúrate de que el campo 'password' esté presente en el usuario
        } for data in client_data]

        return_=client_data_global = [{
            'id': data.id,
            'tipo_cuenta': data.tipo_cuenta,
            'tipo_doc': data.tipo_doc,
            'documento': data.documento,
            'email': data.email,
        } for data in client_data]
        try:
            result = subprocess.run(
                ['behave',
                 'C:\\Users\\Sandoval\\Desktop\\Trabajo\\Codigo\\ScrapperTransfer\\ScrapTransfer\\features\\get_Saldo.feature'],
                capture_output=True, text=True, check=True
            )
            print("Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error output:", e.stderr)
            return jsonify({'status': 'failure', 'message': f'Error al ejecutar behave: {e.stderr}'}), 500

    except Exception as e:
        return jsonify({'status': 'failure', 'message': f'Error al obtener los datos: {str(e)}'}), 500
    finally:
        db.close()