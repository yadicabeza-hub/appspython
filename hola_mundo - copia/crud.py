from sqlalchemy.orm import Session
import models
import schemas

# Crear
def crear_usuario(db: Session, usuario: schemas.Usuario):

    nuevo = models.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


# Leer todos
def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()


# Leer uno
def obtener_usuario(db: Session, id: int):
    return db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()


# Actualizar
def actualizar_usuario(db: Session, id: int, usuario: schemas.Usuario):

    actualizar = db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()

    if actualizar:

        actualizar.nombre = usuario.nombre
        actualizar.correo = usuario.correo

        db.commit()
        db.refresh(actualizar)

    return actualizar


# Eliminar
def eliminar_usuario(db: Session, id: int):

    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == id
    ).first()

    if usuario:
        db.delete(usuario)
        db.commit()

    return usuario