from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Perfil(Base):
    __tablename__ = "perfiles"

    id_perfil = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), unique=True, nullable=False)
    nombre_completo = Column(String(120), nullable=True)
    fotografia = Column(String(255), nullable=True)
    biografia = Column(Text, nullable=True)
    pais = Column(String(80), nullable=True)
    sitio_web = Column(String(255), nullable=True)
    tipo_usuario = Column(Enum('jugador', 'desarrollador', 'ambos'), default='jugador')

    # Relación
    usuario = relationship("Usuario", back_populates="perfil")
