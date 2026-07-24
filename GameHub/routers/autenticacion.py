from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from database import get_db
from models.usuario import Usuario
from models.perfil import Perfil
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from schemas.token_schema import Token
from services.seguridad import obtener_hash_contrasena, verificar_contrasena, crear_token_acceso
from dependencies.autenticacion import obtener_usuario_actual

router = APIRouter()

@router.post("/registro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registro_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Validar que no exista correo o nombre_usuario
    db_user_email = db.query(Usuario).filter(Usuario.correo == usuario.correo).first()
    db_user_name = db.query(Usuario).filter(Usuario.nombre_usuario == usuario.nombre_usuario).first()
    
    if db_user_email:
        raise HTTPException(status_code=409, detail="El correo electrónico ya está registrado.")
    if db_user_name:
        raise HTTPException(status_code=409, detail="El nombre de usuario ya está en uso.")
        
    hashed_pwd = obtener_hash_contrasena(usuario.contrasena)
    nuevo_usuario = Usuario(
        nombre_usuario=usuario.nombre_usuario,
        correo=usuario.correo,
        contrasena_hash=hashed_pwd
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    # Crear automáticamente un perfil vacío asociado al usuario
    nuevo_perfil = Perfil(id_usuario=nuevo_usuario.id_usuario)
    db.add(nuevo_perfil)
    db.commit()
    
    return nuevo_usuario

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # OAuth2 usa 'username' pero nuestro modelo es nombre_usuario, podemos buscar por nombre o correo
    usuario = db.query(Usuario).filter(
        (Usuario.nombre_usuario == form_data.username) | (Usuario.correo == form_data.username)
    ).first()
    
    if not usuario or not verificar_contrasena(form_data.password, usuario.contrasena_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = crear_token_acceso(data={"sub": usuario.nombre_usuario})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UsuarioResponse)
def get_me(current_user: Usuario = Depends(obtener_usuario_actual)):
    return current_user
