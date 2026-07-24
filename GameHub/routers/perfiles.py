from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import os
import uuid
import shutil

from database import get_db
from models.usuario import Usuario
from models.perfil import Perfil
from schemas.perfil_schema import PerfilResponse, PerfilUpdate
from schemas.videojuego_schema import VideojuegoResponse
from dependencies.autenticacion import obtener_usuario_actual

router = APIRouter()

UPLOAD_PERFILES_DIR = "static/uploads/perfiles"

@router.get("/{id_usuario}", response_model=PerfilResponse)
def obtener_perfil(id_usuario: int, db: Session = Depends(get_db)):
    perfil = db.query(Perfil).filter(Perfil.id_usuario == id_usuario).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return perfil

@router.put("/me", response_model=PerfilResponse)
def actualizar_mi_perfil(
    perfil_in: PerfilUpdate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    perfil = db.query(Perfil).filter(Perfil.id_usuario == current_user.id_usuario).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
        
    for var, value in vars(perfil_in).items():
        if value is not None:
            setattr(perfil, var, value)
            
    db.commit()
    db.refresh(perfil)
    return perfil

@router.post("/me/fotografia", response_model=PerfilResponse)
def subir_fotografia(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    perfil = db.query(Perfil).filter(Perfil.id_usuario == current_user.id_usuario).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
        
    # Validar extensión
    extensiones_validas = ["jpg", "jpeg", "png", "webp"]
    ext = file.filename.split(".")[-1].lower()
    if ext not in extensiones_validas:
        raise HTTPException(status_code=400, detail="Formato de imagen no soportado")
        
    # Eliminar foto anterior si existe
    if perfil.fotografia:
        old_path = os.path.join(UPLOAD_PERFILES_DIR, perfil.fotografia.split("/")[-1])
        if os.path.exists(old_path):
            os.remove(old_path)
            
    # Guardar nueva foto
    nuevo_nombre = f"{uuid.uuid4().hex}.{ext}"
    ruta_guardado = os.path.join(UPLOAD_PERFILES_DIR, nuevo_nombre)
    
    with open(ruta_guardado, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    perfil.fotografia = f"/static/uploads/perfiles/{nuevo_nombre}"
    db.commit()
    db.refresh(perfil)
    
    return perfil

@router.get("/{id_usuario}/videojuegos", response_model=List[VideojuegoResponse])
def obtener_videojuegos_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    return usuario.videojuegos
