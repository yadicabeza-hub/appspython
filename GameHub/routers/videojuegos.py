from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models.usuario import Usuario
from models.videojuego import Videojuego
from schemas.videojuego_schema import VideojuegoCreate, VideojuegoUpdate, VideojuegoResponse
from dependencies.autenticacion import obtener_usuario_actual
from services.archivos import guardar_archivo, eliminar_archivo

router = APIRouter()

UPLOAD_PORTADAS_DIR = "static/uploads/portadas"
UPLOAD_JUEGOS_DIR = "static/uploads/videojuegos"

@router.post("", response_model=VideojuegoResponse, status_code=status.HTTP_201_CREATED)
def crear_videojuego(
    videojuego_in: VideojuegoCreate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    nuevo_juego = Videojuego(
        **videojuego_in.model_dump(),
        id_usuario=current_user.id_usuario
    )
    db.add(nuevo_juego)
    db.commit()
    db.refresh(nuevo_juego)
    return nuevo_juego

@router.get("", response_model=List[VideojuegoResponse])
def listar_videojuegos(
    db: Session = Depends(get_db),
    titulo: Optional[str] = Query(None),
    genero: Optional[str] = Query(None),
    plataforma: Optional[str] = Query(None),
    estado: Optional[str] = Query(None),
    pagina: int = Query(1, ge=1),
    limite: int = Query(10, ge=1, le=100)
):
    query = db.query(Videojuego).filter(Videojuego.activo == True)
    
    if titulo:
        query = query.filter(Videojuego.titulo.ilike(f"%{titulo}%"))
    if genero:
        query = query.filter(Videojuego.genero == genero)
    if plataforma:
        query = query.filter(Videojuego.plataforma == plataforma)
    if estado:
        query = query.filter(Videojuego.estado == estado)
        
    offset = (pagina - 1) * limite
    return query.offset(offset).limit(limite).all()

@router.get("/mis-publicaciones", response_model=List[VideojuegoResponse])
def mis_videojuegos(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juegos = db.query(Videojuego).filter(Videojuego.id_usuario == current_user.id_usuario).all()
    return juegos

@router.get("/{id_videojuego}", response_model=VideojuegoResponse)
def obtener_videojuego(id_videojuego: int, db: Session = Depends(get_db)):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
    return juego

@router.put("/{id_videojuego}", response_model=VideojuegoResponse)
def actualizar_videojuego(
    id_videojuego: int,
    videojuego_in: VideojuegoUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
        
    if juego.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso para editar este videojuego")
        
    for var, value in vars(videojuego_in).items():
        if value is not None:
            # Convertir HttpUrl a str
            if var == 'enlace_descarga' and value is not None:
                setattr(juego, var, str(value))
            else:
                setattr(juego, var, value)
            
    db.commit()
    db.refresh(juego)
    return juego

@router.delete("/{id_videojuego}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_videojuego(
    id_videojuego: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
        
    if juego.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar este videojuego")
        
    # Eliminar archivos físicos
    eliminar_archivo(juego.portada)
    eliminar_archivo(juego.archivo_juego)
    
    db.delete(juego)
    db.commit()
    return None

@router.post("/{id_videojuego}/portada", response_model=VideojuegoResponse)
def subir_portada(
    id_videojuego: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego or juego.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso sobre este videojuego")
        
    extensiones_validas = ["jpg", "jpeg", "png", "webp"]
    nuevo_nombre = guardar_archivo(file, UPLOAD_PORTADAS_DIR, extensiones_validas, is_image=True)
    
    eliminar_archivo(juego.portada)
    juego.portada = f"/{UPLOAD_PORTADAS_DIR}/{nuevo_nombre}"
    
    db.commit()
    db.refresh(juego)
    return juego

@router.post("/{id_videojuego}/archivo", response_model=VideojuegoResponse)
def subir_archivo(
    id_videojuego: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego or juego.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso sobre este videojuego")
        
    extensiones_validas = ["zip", "rar"]
    nuevo_nombre = guardar_archivo(file, UPLOAD_JUEGOS_DIR, extensiones_validas, is_image=False)
    
    eliminar_archivo(juego.archivo_juego)
    juego.archivo_juego = f"/{UPLOAD_JUEGOS_DIR}/{nuevo_nombre}"
    
    db.commit()
    db.refresh(juego)
    return juego
