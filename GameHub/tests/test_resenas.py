import pytest
from fastapi.testclient import TestClient
from .test_usuarios import client

def test_no_puedes_resenar_tu_propio_juego():
    # Usuario A
    client.post("/api/auth/registro", json={"nombre_usuario": "userA", "correo": "A@test.com", "contrasena": "123456"})
    tokenA = client.post("/api/auth/login", data={"username": "userA", "password": "123456"}).json()["access_token"]
    
    # Crea un juego
    juego_resp = client.post("/api/videojuegos", json={
        "titulo": "JuegoA", "descripcion": "Desc", "genero": "FPS", "plataforma": "PC"
    }, headers={"Authorization": f"Bearer {tokenA}"})
    
    id_juego = juego_resp.json()["id_videojuego"]
    
    # Intenta reseñar (Debe fallar)
    resp_resena = client.post(f"/api/videojuegos/{id_juego}/resenas", json={
        "calificacion": 5, "comentario": "¡Buenísimo!"
    }, headers={"Authorization": f"Bearer {tokenA}"})
    
    assert resp_resena.status_code == 403
    assert "propio videojuego" in resp_resena.json()["detail"]
