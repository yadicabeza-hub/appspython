# GameHub

Plataforma web académica para publicar, descargar y reseñar videojuegos independientes. 
Desarrollada bajo arquitectura MVC con separación de Backend (FastAPI) y Frontend (Fetch API).

## 1. Funcionalidades
* **Autenticación**: Registro y login seguros mediante JWT y contraseñas cifradas (bcrypt).
* **Perfiles**: Creación de perfil automático al registrarse, capacidad para subir foto de perfil.
* **Catálogo**: Publicación de juegos (incluyendo subida de archivos ZIP/RAR y Portadas), búsqueda por título, género y plataforma.
* **Comunidad**: Sistema de reseñas y calificaciones (1-5 estrellas) que calcula promedios dinámicos, asegurando reglas de negocio (ej. no reseñar juegos propios).

## 2. Tecnologías utilizadas
* **Backend**: Python 3, FastAPI, Uvicorn, SQLAlchemy, Pydantic, Passlib, python-jose.
* **Base de datos**: MariaDB (vía XAMPP), driver PyMySQL.
* **Frontend**: HTML5, CSS3 moderno, JavaScript asíncrono (Fetch API).

## 3. Requisitos previos
- Python 3.9 o superior instalado y en el PATH.
- XAMPP con el módulo de MySQL/MariaDB encendido.

## 4. Instalación
1. Asegúrate de tener XAMPP encendido (Apache y MySQL).
2. Clona o descarga este repositorio y entra a la carpeta.
3. Importa la base de datos:
   - Abre `http://localhost/phpmyadmin`.
   - Crea manualmente una nueva BD llamada `gamehub_db` si no usas el archivo directamente.
   - Ve a "Importar" y sube el archivo `sql/gamehub.sql`.
4. Abre tu terminal en la ruta del proyecto y crea un entorno virtual (En Windows):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. Renombra o copia el archivo `.env.example` a `.env` y asegúrate de que contenga lo siguiente:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=gamehub_db
   DB_USER=root
   DB_PASSWORD=
   SECRET_KEY=TU_CLAVE_SECRETA_AQUI
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   MAX_GAME_FILE_SIZE_MB=100
   ```
6. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```
7. Abre tu navegador en `http://127.0.0.1:8000/`.

## 5. Acceso a Documentación de la API (Swagger)
FastAPI genera documentación automática de manera interactiva. Visita:
- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 6. Pruebas y Seguridad
* **Postman**: Se incluyen archivos `.json` en los artefactos exportados listos para importar en Postman y probar los endpoints.
* **Pruebas automáticas**: Puedes correr las pruebas con el comando `pytest tests/`.
* **Seguridad (Aviso para producción)**: Actualmente, para fines académicos y de desarrollo en Single Page Apps, el JWT se guarda en el `localStorage`. En un entorno de producción estricto, es altamente recomendable mover este JWT a una cookie `HttpOnly` para mitigar vulnerabilidades de robo de tokens (XSS).

---
*Desarrollado para la clase de Desarrollo de Software.*
