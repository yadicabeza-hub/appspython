# Capa de aplicaci�n (`app/`)

Codigo ejecutable del sistema. **No depende** de `spec/` ni `skill/` en tiempo de ejecucion.

## Estructura prevista (ejercicios web avanzados)

```text
app/
??? api/v1/          # Rutas y controladores
??? core/            # Config, seguridad, constantes
??? models/          # ORM
??? schemas/         # Validaci�n (Pydantic, etc.)
??? services/        # L�gica de negocio
??? main.py          # Punto de entrada
??? examples/        # Scripts educativos aislados
```

## Reglas

- Toda feature nace de un plan en `spec/planes/`; la skill solo gu�a al agente, no se importa aqu�.
- Pruebas en `tests/` (ra�z del repo), espejo l�gico de `app/`.
- Sin referencias a archivos bajo `spec/` o `skill/` desde c�digo Python.

## Ejemplos

| Script | Descripci�n |
|--------|-------------|
| `examples/hola_mundo.py` | Saludo de consola (migrado desde `python.py` ra�z) |
