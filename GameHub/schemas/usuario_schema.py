from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    nombre_usuario: str = Field(..., max_length=50)
    correo: EmailStr = Field(..., max_length=120)

class UsuarioCreate(UsuarioBase):
    contrasena: str = Field(..., min_length=6, max_length=100)

class UsuarioUpdate(BaseModel):
    nombre_usuario: Optional[str] = Field(None, max_length=50)
    correo: Optional[EmailStr] = Field(None, max_length=120)
    contrasena: Optional[str] = Field(None, min_length=6, max_length=100)

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fecha_registro: datetime
    estado: bool

    class Config:
        from_attributes = True
