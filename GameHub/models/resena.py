from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Resena(Base):
    __tablename__ = "resenas"

    id_resena = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="CASCADE"), nullable=False)
    id_videojuego = Column(Integer, ForeignKey("videojuegos.id_videojuego", ondelete="CASCADE"), nullable=False)
    calificacion = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=False)
    fecha_resena = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    __table_args__ = (
        CheckConstraint('calificacion >= 1 AND calificacion <= 5', name='chk_calificacion'),
        UniqueConstraint('id_usuario', 'id_videojuego', name='uq_usuario_videojuego'),
    )

    # Relaciones
    usuario = relationship("Usuario", back_populates="resenas")
    videojuego = relationship("Videojuego", back_populates="resenas")
