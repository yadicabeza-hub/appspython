from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    cantidad: Optional[int] = None


class Producto(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)