from sqlalchemy.orm import Session
from models import Producto
from shemas import ProductoCreate, ProductoUpdate


def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()


def crear_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def actualizar_producto(db: Session, producto_id: int, producto_actualizado: ProductoUpdate):
    db_producto = obtener_producto(db, producto_id)
    if db_producto is None:
        return None

    for key, value in producto_actualizado.model_dump(exclude_unset=True).items():
        setattr(db_producto, key, value)

    db.commit()
    db.refresh(db_producto)
    return db_producto


def delete_producto(db: Session, producto_id: int):
    db_producto = obtener_producto(db, producto_id)
    if db_producto is None:
        return None

    db.delete(db_producto)
    db.commit()
    return db_producto