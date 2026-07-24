from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.usuario import Usuario
from schemas.usuario_schema import UsuarioResponse, UsuarioUpdate
from dependencies.autenticacion import obtener_usuario_actual
from services.seguridad import obtener_hash_contrasena

router = APIRouter()

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(
    id_usuario: int, 
    usuario_in: UsuarioUpdate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    if current_user.id_usuario != id_usuario:
        raise HTTPException(status_code=403, detail="No autorizado a actualizar este usuario")
        
    if usuario_in.correo:
        existe_correo = db.query(Usuario).filter(Usuario.correo == usuario_in.correo, Usuario.id_usuario != id_usuario).first()
        if existe_correo:
            raise HTTPException(status_code=409, detail="El correo ya está en uso")
            
    if usuario_in.nombre_usuario:
        existe_username = db.query(Usuario).filter(Usuario.nombre_usuario == usuario_in.nombre_usuario, Usuario.id_usuario != id_usuario).first()
        if existe_username:
            raise HTTPException(status_code=409, detail="El nombre de usuario ya está en uso")
            
    if usuario_in.nombre_usuario:
        current_user.nombre_usuario = usuario_in.nombre_usuario
    if usuario_in.correo:
        current_user.correo = usuario_in.correo
    if usuario_in.contrasena:
        current_user.contrasena_hash = obtener_hash_contrasena(usuario_in.contrasena)
        
    db.commit()
    db.refresh(current_user)
    return current_user

@router.delete("/{id_usuario}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(
    id_usuario: int, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    if current_user.id_usuario != id_usuario:
        raise HTTPException(status_code=403, detail="No autorizado a eliminar este usuario")
        
    db.delete(current_user)
    db.commit()
    return None
