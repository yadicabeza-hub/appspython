from app.examples.hola_mundo import mensaje_saludo


def test_mensaje_saludo_contiene_nombre_y_edad():
    texto = mensaje_saludo()
    assert "Yadira" in texto
    assert "Cabeza" in texto
    assert "30" in texto
    assert texto.startswith("Hola,")
    assert "a\u00f1os" in texto
