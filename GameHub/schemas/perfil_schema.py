from pydantic import BaseModel, Field
from typing import Optional

class PerfilBase(BaseModel):
    nombre_completo: Optional[str] = Field(None, max_length=120)
    biografia: Optional[str] = None
    pais: Optional[str] = Field(None, max_length=80)
    sitio_web: Optional[str] = Field(None, max_length=255)
    tipo_usuario: Optional[str] = Field('jugador', pattern="^(jugador|desarrollador|ambos)$")

class PerfilUpdate(PerfilBase):
    pass

class PerfilResponse(PerfilBase):
    id_perfil: int
    id_usuario: int
    fotografia: Optional[str] = None

    class Config:
        from_attributes = True
