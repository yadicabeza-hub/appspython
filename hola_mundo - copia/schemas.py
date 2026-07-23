from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    correo: str

class UsuarioResponse(Usuario):
    id: int

    model_config = {"from_attributes": True}