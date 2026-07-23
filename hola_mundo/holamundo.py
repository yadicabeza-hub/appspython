from fastapi import status
from _typeshed import importlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import pymysql

# Importamos la conexión desde nuestro nuevo archivo database.py
from database import obtener_conexion

app = FastAPI()

# montar la carpeta static para archivos estaticos 
if os.path.exists("Static"):
    app.mount("/static", StaticFiles(directory="Static"), name="Static")

# ---- RUTAS PARA LOGIN ----

@app.post("/api/login")
async def login(request: Request):
    data = await request.json()
    user = data.get("usuario")
    password = data.get("contraseña") # Nota: asegúrate de enviar "contraseña" en Postman para el login

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        # Consultamos si existe el usuario con esa contraseña
        sql = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
        cursor.execute(sql, (user, password))
        
        usuario_db = cursor.fetchone()
        
        cursor.close()
        conexion.close()

        if usuario_db:
            return {"message": "login exitoso su correo es " + usuario_db['correo']}
            
    except pymysql.MySQLError as err:
        return {"message": f"Error de conexión a la BD: {err}"}
            
    return {"message": "login fallido"}

# ---- RUTAS CRUD PARA USUARIOS ----

# 1. READ ALL (Obtener todos los usuarios)
@app.get("/api/usuarios")
async def obtener_usuarios():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, usuario, correo FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return usuarios
    except pymysql.MySQLError as err:
        return {"message": f"Error de base de datos: {err}"}

# 2. READ ONE (Obtener un solo usuario por ID)
@app.get("/api/usuarios/{usuario_id}")
async def obtener_usuario(usuario_id: int):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "SELECT id, usuario, correo FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        
        if usuario:
            return usuario
        return {"message": "Usuario no encontrado"}
    except pymysql.MySQLError as err:
        return {"message": f"Error de base de datos: {err}"}

# 3. CREATE (Crear un nuevo usuario)
@app.post("/api/usuarios")
async def crear_usuario(request: Request):
    data = await request.json()
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (usuario, correo, contrasena) VALUES (%s, %s, %s)"
        cursor.execute(sql, (data.get("usuario"), data.get("correo"), data.get("contrasena")))
        conexion.commit()
        cursor.close()
        conexion.close()
        return {"message": "Usuario creado exitosamente"}
    except pymysql.MySQLError as err:
        return {"message": f"Error de base de datos: {err}"}

        class UsuarioRespuesta (UsuarioCrear)
        id:int
        
      @get("api/db-status")
      def verificar_base_de_datos():
        try:
            with obtener_conexion() as conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT 1 AS resultado")
                    cursor.fetchone()
                    return {"conexion": "correcta"}
        except pymysql.MySQLError as error:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Error de conexión a la base de datos: {error}"
        )


# 4. UPDATE (Actualizar un usuario existente)
@app.put("/api/usuarios/{usuario_id}")
async def actualizar_usuario(usuario_id: int, request: Request):
    data = await request.json()
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        # Validamos si enviaron nueva contraseña o solo actualizan datos básicos
        if "contrasena" in data:
            sql = "UPDATE usuarios SET usuario = %s, correo = %s, contrasena = %s WHERE id = %s"
            valores = (data.get("usuario"), data.get("correo"), data.get("contrasena"), usuario_id)
        else:
            sql = "UPDATE usuarios SET usuario = %s, correo = %s WHERE id = %s"
            valores = (data.get("usuario"), data.get("correo"), usuario_id)
            
        cursor.execute(sql, valores)
        conexion.commit()
        
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        
        if filas_afectadas > 0:
            return {"message": "Usuario actualizado exitosamente"}
        return {"message": "Usuario no encontrado o sin cambios"}
        
    except pymysql.MySQLError as err:
        return {"message": f"Error de base de datos: {err}"}

# 5. DELETE (Eliminar un usuario)
@app.delete("/api/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: int):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (usuario_id,))
        conexion.commit()
        
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        
        if filas_afectadas > 0:
            return {"message": "Usuario eliminado exitosamente"}
        return {"message": "Usuario no encontrado"}
    except pymysql.MySQLError as err:
        return {"message": f"Error de base de datos: {err}"}

# ---- RUTA PRINCIPAL (HTML) ----
@app.get("/", response_class=HTMLResponse)
def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()