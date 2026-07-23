from pathlib import Path
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from pydantic import BaseModel, EmailStr
import pymysql
from database import get_connection

app = FastAPI(title="MyApp User Management API")
BASE_DIR = Path(__file__).resolve().parent
VIEWS_DIR = BASE_DIR / "views"

# ---- MODELOS PYDANTIC ----

class LoginRequest(BaseModel):
    usuario: str
    contrasena: str

class UsuarioCreate(BaseModel):
    usuario: str
    correo: EmailStr
    contrasena: str

class UsuarioUpdate(BaseModel):
    usuario: str
    correo: EmailStr
    contrasena: str | None = None  # Contraseña opcional al actualizar

# ---- RUTAS PARA SERVIR VISTAS HTML ----

@app.get("/", response_class=HTMLResponse)
def index_view():
    index_path = VIEWS_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="Vista no encontrada")
    return index_path.read_text(encoding="utf-8")

@app.get("/login", response_class=HTMLResponse)
def login_view():
    login_path = VIEWS_DIR / "login.html"
    if not login_path.exists():
        raise HTTPException(status_code=404, detail="Vista no encontrada")
    return login_path.read_text(encoding="utf-8")

@app.get("/registro", response_class=HTMLResponse)
def registro_view():
    registro_path = VIEWS_DIR / "registro.html"
    if not registro_path.exists():
        raise HTTPException(status_code=404, detail="Vista no encontrada")
    return registro_path.read_text(encoding="utf-8")

@app.get("/usuarios", response_class=HTMLResponse)
def usuarios_view():
    usuarios_path = VIEWS_DIR / "usuarios.html"
    if not usuarios_path.exists():
        raise HTTPException(status_code=404, detail="Vista no encontrada")
    return usuarios_path.read_text(encoding="utf-8")

# ---- RUTAS API REST ----

# 1. API LOGIN
@app.post("/api/login")
async def login(login_data: LoginRequest):
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                # Buscar usuario por nombre y contraseña
                sql = "SELECT id, usuario, correo FROM usuarios WHERE usuario = %s AND contrasena = %s"
                cursor.execute(sql, (login_data.usuario, login_data.contrasena))
                usuario_db = cursor.fetchone()

        if usuario_db:
            return {
                "message": "Login exitoso",
                "usuario": usuario_db["usuario"],
                "correo": usuario_db["correo"]
            }

    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de conexión a la base de datos: {err}"
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas"
    )

# 2. READ ALL (Obtener todos los usuarios)
@app.get("/api/usuarios")
async def obtener_usuarios():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id, usuario, correo FROM usuarios")
                usuarios = cursor.fetchall()
        return usuarios
    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de base de datos: {err}"
        )

# 3. READ ONE (Obtener un solo usuario por ID)
@app.get("/api/usuarios/{usuario_id}")
async def obtener_usuario(usuario_id: int):
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sql = "SELECT id, usuario, correo FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                usuario = cursor.fetchone()

        if usuario:
            return usuario
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de base de datos: {err}"
        )

# 4. CREATE / REGISTER (Crear un nuevo usuario)
@app.post("/api/usuarios")
async def crear_usuario(user_data: UsuarioCreate):
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                # Verificar si el correo o usuario ya existe
                cursor.execute("SELECT id FROM usuarios WHERE usuario = %s OR correo = %s", (user_data.usuario, user_data.correo))
                if cursor.fetchone():
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="El nombre de usuario o correo ya se encuentra registrado"
                    )
                
                sql = "INSERT INTO usuarios (usuario, correo, contrasena) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_data.usuario, user_data.correo, user_data.contrasena))
            conexion.commit()
        return {"message": "Usuario creado exitosamente"}
    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de base de datos: {err}"
        )

# 5. UPDATE (Actualizar un usuario existente)
@app.put("/api/usuarios/{usuario_id}")
async def actualizar_usuario(usuario_id: int, user_data: UsuarioUpdate):
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                # Verificar duplicados para otro usuario
                cursor.execute("SELECT id FROM usuarios WHERE (usuario = %s OR correo = %s) AND id != %s", (user_data.usuario, user_data.correo, usuario_id))
                if cursor.fetchone():
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="El nombre de usuario o correo ya está en uso por otro usuario"
                    )

                if user_data.contrasena:
                    sql = "UPDATE usuarios SET usuario = %s, correo = %s, contrasena = %s WHERE id = %s"
                    valores = (user_data.usuario, user_data.correo, user_data.contrasena, usuario_id)
                else:
                    sql = "UPDATE usuarios SET usuario = %s, correo = %s WHERE id = %s"
                    valores = (user_data.usuario, user_data.correo, usuario_id)
                
                cursor.execute(sql, valores)
                filas_afectadas = cursor.rowcount
            conexion.commit()

        if filas_afectadas > 0:
            return {"message": "Usuario actualizado exitosamente"}
        
        # Si no hubo cambios en la consulta pero existe
        return {"message": "No se realizaron cambios"}

    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de base de datos: {err}"
        )

# 6. DELETE (Eliminar un usuario)
@app.delete("/api/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: int):
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                filas_afectadas = cursor.rowcount
            conexion.commit()

        if filas_afectadas > 0:
            return {"message": "Usuario eliminado exitosamente"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    except pymysql.MySQLError as err:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de base de datos: {err}"
        )

# 7. DB STATUS CHECK
@app.get("/api/db-status")
def verificar_base_de_datos():
    try:
        with get_connection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT 1 AS resultado")
                cursor.fetchone()
        return {"conexion": "correcta"}
    except pymysql.MySQLError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error de conexión a la base de datos: {error}"
        )
