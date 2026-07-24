def test_registro_usuario(client):
    response = client.post(
        "/api/auth/registro",
        json={"nombre_usuario": "testuser", "correo": "test@test.com", "contrasena": "123456"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nombre_usuario"] == "testuser"
    assert "id_usuario" in data

def test_login_usuario(client):
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
