# routes/api_login_bp.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from db.models import User, SessionLocal

api_login_bp = Blueprint('api_login_bp', __name__)

@api_login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    db = SessionLocal()
    user = db.query(User).filter_by(email=email).first()

    # Verificar si el usuario existe y la contraseña es correcta
    if user and check_password_hash(user.password, password):
        # Crear el token con el claim "sub"
        additional_claims = {"sub": user.id}
        access_token = create_access_token(identity=email, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Credenciales incorrectas'}), 401
