from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Videojuego(Base):
    __tablename__ = "videojuegos"

    id_videojuego = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    titulo = Column(String(150), nullable=False, index=True)
    descripcion = Column(Text, nullable=False)
    genero = Column(String(80), nullable=False, index=True)
    plataforma = Column(String(80), nullable=False)
    version = Column(String(30), nullable=True)
    estado = Column(Enum('desarrollo', 'demo', 'beta', 'terminado'), default='terminado')
    portada = Column(String(255), nullable=True)
    archivo_juego = Column(String(255), nullable=True)
    enlace_descarga = Column(String(500), nullable=True)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)

    # Relaciones
    usuario = relationship("Usuario", back_populates="videojuegos")
    resenas = relationship("Resena", back_populates="videojuego", cascade="all, delete-orphan")
