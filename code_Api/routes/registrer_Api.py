# routes/api_register_bp.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from db.models import User, SessionLocal
from uuid import uuid4

api_register_bp = Blueprint('api_register_bp', __name__)

@api_register_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    documento = data.get('documento')
    email = data.get('email')
    password = data.get('password')

    if not all([documento, email, password]):
        return jsonify({'status': 'failure', 'message': 'Todos los campos son requeridos'}), 400

    db = SessionLocal()
    try:
        # Verificar si el documento ya existe
        existing_user = db.query(User).filter_by(documento=documento).first()
        if existing_user:
            return jsonify({'status': 'failure', 'message': 'El documento ya está registrado'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User(
            id=str(uuid4()),
            documento=documento,
            email=email,
            password=hashed_password,
            client_id=str(uuid4()),
            client_secret=str(uuid4())
        )

        db.add(new_user)
        db.commit()
        return jsonify({'status': 'success', 'message': 'Usuario registrado exitosamente.'}), 200
    except Exception as e:
        db.rollback()
        return jsonify({'status': 'failure', 'message': f'Error al registrar el usuario: {str(e)}'}), 500
    finally:
        db.close()
