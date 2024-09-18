# code_Api/decorador/decorador.py

from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt
from db.models import User, SessionLocal


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        db = SessionLocal()
        try:
            verify_jwt_in_request()
            claims = get_jwt()
            current_user_id = claims['sub']
            current_user = db.query(User).filter_by(id=current_user_id).first()
            if not current_user:
                return jsonify({'message': 'Usuario no encontrado'}), 404
        except Exception as e:
            return jsonify({'message': str(e)}), 401
        finally:
            db.close()

        return f(current_user, *args, **kwargs)

    return decorated
