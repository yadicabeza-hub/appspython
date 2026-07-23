from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear(usuario: schemas.Usuario,
          db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/usuarios", response_model=List[schemas.UsuarioResponse])
def listar(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)

@app.get("/usuarios/{id}", response_model=schemas.UsuarioResponse)
def buscar(id: int,
           db: Session = Depends(get_db)):
    usuario = crud.obtener_usuario(db, id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{id}", response_model=schemas.UsuarioResponse)
def actualizar(id: int,
                usuario: schemas.Usuario,
                db: Session = Depends(get_db)):
    usuario_actualizado = crud.actualizar_usuario(db, id, usuario)
    if not usuario_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return usuario_actualizado

@app.delete("/usuarios/{id}")
def eliminar(id: int,
             db: Session = Depends(get_db)):
    usuario = crud.eliminar_usuario(db, id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}