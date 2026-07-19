from sqlalchemy import Column, Integer, String, Float
from servidor.database import Base


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)