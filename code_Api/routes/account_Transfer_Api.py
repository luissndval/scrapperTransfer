from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from uuid import uuid4

from code_Api.decorador.decorador import token_required
from db.models import SessionLocal, ClientData

api_guardar_datos_cliente_bp = Blueprint('api_guardar_datos_cliente_bp', __name__)

@api_guardar_datos_cliente_bp.route('/guardar_datos_cliente', methods=['POST'])
@token_required
def guardar_datos_cliente(current_user):
    data = request.get_json()
    tipo_cuenta = data.get('TipoCuenta')
    tipo_doc = data.get('TipoDoc')
    documento = data.get('documento')
    email = data.get('email')

    if not all([tipo_cuenta, tipo_doc, documento, email]):
        return jsonify({'status': 'failure', 'message': 'Todos los campos son requeridos'}), 400

    db = SessionLocal()
    try:
        # Verificar si ya existe una entrada con el mismo documento y tipo_cuenta
        existing_data = db.query(ClientData).filter_by(documento=documento, tipo_cuenta=tipo_cuenta).first()
        if existing_data:
            return jsonify({'status': 'failure', 'message': 'Ya existe una cuenta asociada a este documento y tipo de cuenta.'}), 400

        # Crear nuevo registro en ClientData
        client_data = ClientData(
            id=str(uuid4()),
            tipo_cuenta=tipo_cuenta,
            tipo_doc=tipo_doc,
            documento=documento,
            email=email,
            created_by=current_user.id  # Asociar con el usuario autenticado
        )

        # Guardar el registro en la base de datos
        db.add(client_data)
        db.commit()
        return jsonify({'status': 'success', 'message': 'Datos guardados exitosamente.'}), 200
    except Exception as e:
        db.rollback()
        return jsonify({'status': 'failure', 'message': f'Error al guardar los datos: {str(e)}'}), 500
    finally:
        db.close()