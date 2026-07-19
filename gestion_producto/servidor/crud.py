from sqlalchemy.orm import session
import models, schemas

# 1.Crear un producto
def crear_producto(db:session, producto:schemas.ProductoCreate):
    db_producto=models.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        cantidad=producto.cantidad
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# Obtener los productos
def get_productos(db:session,skip: int=0,limit:int=100):
  return db.query(models.Producto).offset(skip).limit(limit).all()
# Obtener un solo registro por id
def get_producto(db:session, producto_id:int):
  return db.query(models.Producto).filter(models.Producto.id==producto_id).first()
# Actualizar un producto
def actualizar_producto(db:session, producto_id:int, producto:schemas.ProductoUpdate):
  db_producto=get_producto(db,producto_id=producto_id)
  if db_producto is None:
    return None
  db_producto.nombre=producto.nombre
  db_producto.descripcion=producto.descripcion
  db_producto.precio=producto.precio
  db_producto.cantidad=producto.cantidad
  db.commit()
  db.refresh(db_producto)
  return db_producto

# Eliminar un producto
def eliminar_producto(db:session, producto_id:int):
  db_producto=get_producto(db,producto_id=producto_id)
  if db_producto is None:
    return None
  db.delete(db_producto)
  db.commit()
  return db_producto