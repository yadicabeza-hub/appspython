from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_usuario = Column(String(50), unique=True, index=True, nullable=False)
    correo = Column(String(120), unique=True, index=True, nullable=False)
    contrasena_hash = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    estado = Column(Boolean, default=True)

    # Relaciones
    perfil = relationship("Perfil", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    videojuegos = relationship("Videojuego", back_populates="usuario", cascade="all, delete-orphan")
    resenas = relationship("Resena", back_populates="usuario", cascade="all, delete-orphan")
