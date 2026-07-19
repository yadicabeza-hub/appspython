from fastapi import FastAPI, Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from database import engine, get_db
imporservidor.database, schemas
import crud

# Crear la tabla en la base de datos
models.Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="API Gestion de Productos",
    description="API para la gestión de productos",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RUTAS DE LA API (Endpoints)

@app.post("/productos/", response_model=schemas.Producto)
def create_producto(producto:schemas.ProductoCreate, db:Session= Depends(get_db)):
  return crud.crear_producto(db=db, producto=producto)

@app.get("/productos/", response_model=list[schemas.Producto])
def read_productos(skip:int=0,limit:int=100, db:Session=Depends(get_db)):
  return crud.get_productos(db=db,skip=skip,limit=limit)

@app.put("/productos/{producto_id}",response_model=schemas.Producto)
def actualizar_producto(producto_id:int,producto:schemas.ProductoUpdate,db:Session=Depends(get_db)):
  db_producto=crud.actualizar_producto(db=db, producto_id=producto_id, producto=producto)
  if db_producto is None:
    raise HTTPException(status_code=404, detail="Producto no encontrado")
  return db_producto

@app.delete("/productos/{producto_id}", response_model=schemas.Producto)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.eliminar_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto