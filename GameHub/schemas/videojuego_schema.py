from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

class VideojuegoBase(BaseModel):
    titulo: str = Field(..., max_length=150)
    descripcion: str
    genero: str = Field(..., max_length=80)
    plataforma: str = Field(..., max_length=80)
    version: Optional[str] = Field(None, max_length=30)
    estado: Optional[str] = Field('terminado', pattern="^(desarrollo|demo|beta|terminado)$")
    enlace_descarga: Optional[HttpUrl] = None

class VideojuegoCreate(VideojuegoBase):
    pass

class VideojuegoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=150)
    descripcion: Optional[str] = None
    genero: Optional[str] = Field(None, max_length=80)
    plataforma: Optional[str] = Field(None, max_length=80)
    version: Optional[str] = Field(None, max_length=30)
    estado: Optional[str] = Field(None, pattern="^(desarrollo|demo|beta|terminado)$")
    enlace_descarga: Optional[HttpUrl] = None
    activo: Optional[bool] = None

class VideojuegoResponse(VideojuegoBase):
    id_videojuego: int
    id_usuario: int
    portada: Optional[str] = None
    archivo_juego: Optional[str] = None
    fecha_publicacion: datetime
    activo: bool

    class Config:
        from_attributes = True
