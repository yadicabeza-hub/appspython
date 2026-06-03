# Ejemplo minimo de consola - AppsPython

_nombre_ = "Yadira"
_apellido_ = "Cabeza"
_edad_ = "30"


def mensaje_saludo() -> str:
    return (
        f"Hola, mi nombre es {_nombre_} {_apellido_} y tengo {_edad_} a\u00f1os."
    )


if __name__ == "__main__":
    print(mensaje_saludo())
