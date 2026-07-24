import pytest
from fastapi.testclient import TestClient
from .test_usuarios import client

def test_publicar_videojuego():
    # 1. Registrar y loguear
    client.post("/api/auth/registro", json={"nombre_usuario": "dev", "correo": "dev@test.com", "contrasena": "123456"})
    resp_login = client.post("/api/auth/login", data={"username": "dev", "password": "123456"})
    token = resp_login.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Publicar juego
    juego_data = {
        "titulo": "Mi Super Juego",
        "descripcion": "Descripción de prueba",
        "genero": "RPG",
        "plataforma": "PC",
        "estado": "terminado"
    }
    
    response = client.post("/api/videojuegos", json=juego_data, headers=headers)
    assert response.status_code == 201
    assert response.json()["titulo"] == "Mi Super Juego"

def test_listar_videojuegos():
    response = client.get("/api/videojuegos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
