from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from database import get_db
from models.usuario import Usuario
from models.videojuego import Videojuego
from models.resena import Resena
from schemas.resena_schema import ResenaCreate, ResenaUpdate, ResenaResponse, CalificacionPromedioResponse
from dependencies.autenticacion import obtener_usuario_actual

router = APIRouter()

@router.post("/videojuegos/{id_videojuego}/resenas", response_model=ResenaResponse, status_code=status.HTTP_201_CREATED)
def crear_resena(
    id_videojuego: int,
    resena_in: ResenaCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
        
    if juego.id_usuario == current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No puedes reseñar tu propio videojuego")
        
    resena_existente = db.query(Resena).filter(
        Resena.id_usuario == current_user.id_usuario,
        Resena.id_videojuego == id_videojuego
    ).first()
    if resena_existente:
        raise HTTPException(status_code=409, detail="Ya has reseñado este videojuego. Puedes editar tu reseña.")
        
    nueva_resena = Resena(
        **resena_in.model_dump(),
        id_usuario=current_user.id_usuario,
        id_videojuego=id_videojuego
    )
    db.add(nueva_resena)
    db.commit()
    db.refresh(nueva_resena)
    return nueva_resena

@router.get("/videojuegos/{id_videojuego}/resenas", response_model=List[ResenaResponse])
def listar_resenas(id_videojuego: int, db: Session = Depends(get_db)):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
        
    return db.query(Resena).filter(Resena.id_videojuego == id_videojuego).all()

@router.get("/videojuegos/{id_videojuego}/calificacion", response_model=CalificacionPromedioResponse)
def obtener_calificacion_promedio(id_videojuego: int, db: Session = Depends(get_db)):
    juego = db.query(Videojuego).filter(Videojuego.id_videojuego == id_videojuego).first()
    if not juego:
        raise HTTPException(status_code=404, detail="Videojuego no encontrado")
        
    resultado = db.query(
        func.avg(Resena.calificacion).label('promedio'),
        func.count(Resena.id_resena).label('total')
    ).filter(Resena.id_videojuego == id_videojuego).first()
    
    promedio = round(resultado.promedio, 2) if resultado.promedio else 0.0
    return {
        "id_videojuego": id_videojuego,
        "promedio": promedio,
        "total_resenas": resultado.total
    }

@router.get("/resenas/{id_resena}", response_model=ResenaResponse)
def obtener_resena(id_resena: int, db: Session = Depends(get_db)):
    resena = db.query(Resena).filter(Resena.id_resena == id_resena).first()
    if not resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
    return resena

@router.put("/resenas/{id_resena}", response_model=ResenaResponse)
def actualizar_resena(
    id_resena: int,
    resena_in: ResenaUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    resena = db.query(Resena).filter(Resena.id_resena == id_resena).first()
    if not resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
        
    if resena.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso para editar esta reseña")
        
    if resena_in.calificacion is not None:
        resena.calificacion = resena_in.calificacion
    if resena_in.comentario is not None:
        resena.comentario = resena_in.comentario
        
    db.commit()
    db.refresh(resena)
    return resena

@router.delete("/resenas/{id_resena}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_resena(
    id_resena: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(obtener_usuario_actual)
):
    resena = db.query(Resena).filter(Resena.id_resena == id_resena).first()
    if not resena:
        raise HTTPException(status_code=404, detail="Reseña no encontrada")
        
    if resena.id_usuario != current_user.id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar esta reseña")
        
    db.delete(resena)
    db.commit()
    return None
