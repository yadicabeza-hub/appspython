import os
import uuid
import shutil
from fastapi import UploadFile, HTTPException
from config import settings

def guardar_archivo(file: UploadFile, directorio: str, extensiones_validas: list, is_image: bool = False) -> str:
    # Validar extensión
    ext = file.filename.split(".")[-1].lower()
    if ext not in extensiones_validas:
        raise HTTPException(status_code=400, detail=f"Formato no soportado. Debe ser: {', '.join(extensiones_validas)}")
        
    # El tamaño en FastAPI UploadFile se lee consumiendo o confiando en content-length o limitando en Spooler.
    # Por simplicidad aquí lo validamos leyendo un chunk si quisieramos, pero en UploadFile 
    # se suele hacer con middleware o comprobando el tamaño tras el volcado si es grande.
    # Asumimos una aproximación leyendo el header de content-length si existe (no siempre es fiable)
    # o leyendo su tamaño tras guardar y borrándolo si excede, pero para este demo lo dejamos simple 
    # o leyendo todo en memoria lo cual no es ideal.
    # En FastAPI, la mejor manera de restringir tamaño es en Nginx, pero se pide configurarlo en env.
    
    file.file.seek(0, 2)
    tamanio_bytes = file.file.tell()
    file.file.seek(0)
    
    tamanio_mb = tamanio_bytes / (1024 * 1024)
    if not is_image and tamanio_mb > settings.MAX_GAME_FILE_SIZE_MB:
        raise HTTPException(status_code=413, detail=f"El archivo excede el tamaño máximo permitido de {settings.MAX_GAME_FILE_SIZE_MB}MB")

    # Generar nombre único
    nuevo_nombre = f"{uuid.uuid4().hex}.{ext}"
    ruta_guardado = os.path.join(directorio, nuevo_nombre)
    
    with open(ruta_guardado, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return nuevo_nombre

def eliminar_archivo(ruta_relativa: str):
    if not ruta_relativa:
        return
    # Convertir ruta como /static/uploads/... a ruta local
    ruta_local = ruta_relativa.lstrip("/")
    if os.path.exists(ruta_local):
        os.remove(ruta_local)
