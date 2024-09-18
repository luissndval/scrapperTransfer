from sqlalchemy.orm import Session
from .models import User  # Asegúrate de que este archivo exista y contenga el modelo User
from uuid import uuid4

def get_user(db: Session, user_id: str):
    """Obtiene un usuario por su ID."""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: User):
    """Crea un nuevo usuario en la base de datos."""
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    """Obtiene un usuario por su correo electrónico."""
    return db.query(User).filter(User.email == email).first()

def generate_unique_client_id(db: Session) -> str:
    """Genera un client_id único para un nuevo usuario."""
    while True:
        client_id = str(uuid4())
        if not db.query(User).filter_by(client_id=client_id).first():
            return client_id

def generate_unique_client_secret(db: Session) -> str:
    """Genera un client_secret único para un nuevo usuario."""
    while True:
        client_secret = str(uuid4())
        if not db.query(User).filter_by(client_secret=client_secret).first():
            return client_secret
