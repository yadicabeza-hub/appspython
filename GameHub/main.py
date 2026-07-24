from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="GameHub API",
    description="API REST para la plataforma GameHub",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción se debe limitar a los dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear estructura de carpetas estáticas si no existen
UPLOAD_DIRS = [
    "static/uploads/perfiles",
    "static/uploads/portadas",
    "static/uploads/videojuegos"
]
for d in UPLOAD_DIRS:
    os.makedirs(d, exist_ok=True)

# Configuración de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

from routers import autenticacion, usuarios, perfiles, videojuegos, resenas
app.include_router(autenticacion.router, prefix="/api/auth", tags=["Autenticación"])
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(perfiles.router, prefix="/api/perfiles", tags=["Perfiles"])
app.include_router(videojuegos.router, prefix="/api/videojuegos", tags=["Videojuegos"])
app.include_router(resenas.router, prefix="/api", tags=["Reseñas"])

# Configuración de Plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Rutas del Frontend
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/registro", response_class=HTMLResponse)
def registro_page(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@app.get("/perfil", response_class=HTMLResponse)
def perfil_page(request: Request):
    return templates.TemplateResponse("perfil.html", {"request": request})

@app.get("/videojuegos", response_class=HTMLResponse)
def videojuegos_page(request: Request):
    return templates.TemplateResponse("videojuegos.html", {"request": request})

@app.get("/mis_juegos", response_class=HTMLResponse)
def mis_juegos_page(request: Request):
    return templates.TemplateResponse("mis_juegos.html", {"request": request})

@app.get("/detalle_juego", response_class=HTMLResponse)
def detalle_juego_page(request: Request):
    return templates.TemplateResponse("detalle_juego.html", {"request": request})

@app.get("/publicar_juego", response_class=HTMLResponse)
def publicar_juego_page(request: Request):
    return templates.TemplateResponse("publicar_juego.html", {"request": request})
