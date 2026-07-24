from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ResenaBase(BaseModel):
    calificacion: int = Field(..., ge=1, le=5)
    comentario: str

class ResenaCreate(ResenaBase):
    pass

class ResenaUpdate(BaseModel):
    calificacion: Optional[int] = Field(None, ge=1, le=5)
    comentario: Optional[str] = None

class ResenaResponse(ResenaBase):
    id_resena: int
    id_usuario: int
    id_videojuego: int
    fecha_resena: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True

class CalificacionPromedioResponse(BaseModel):
    id_videojuego: int
    promedio: float
    total_resenas: int
