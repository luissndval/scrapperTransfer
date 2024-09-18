# db/models.py

from sqlalchemy import Column, String, Float, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = 'sqlite:///data.db'

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True)
    documento = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    client_id = Column(String, unique=True)
    client_secret = Column(String, unique=True)
    saldo = Column(Float, default=0.0)
    tipo_cuenta = Column(String)  # Asegúrate de que este campo esté definido
    tipo_doc = Column(String)  # Asegúrate de que este campo esté definido

    client_data = relationship("ClientData", back_populates="owner")

class ClientData(Base):
    __tablename__ = 'client_data'

    id = Column(String, primary_key=True, index=True)
    tipo_cuenta = Column(String)
    tipo_doc = Column(String)
    documento = Column(String)
    email = Column(String)
    created_by = Column(String, ForeignKey('users.id'))

    owner = relationship("User", back_populates="client_data")
Base.metadata.create_all(bind=engine)
