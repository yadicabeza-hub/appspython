import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from database import Base, get_db

# Crear BD en memoria para testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_registro_usuario():
    response = client.post(
        "/api/auth/registro",
        json={"nombre_usuario": "testuser", "correo": "test@test.com", "contrasena": "123456"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre_usuario"] == "testuser"
    assert "id_usuario" in data

def test_login_usuario():
    # Registrar primero
    client.post(
        "/api/auth/registro",
        json={"nombre_usuario": "testuser", "correo": "test@test.com", "contrasena": "123456"}
    )
    # Hacer login
    response = client.post(
        "/api/auth/login",
        data={"username": "testuser", "password": "123456"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
