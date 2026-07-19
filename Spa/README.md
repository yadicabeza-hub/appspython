# 🐍 AppsPython - Programación Web Avanzada

¡Bienvenido a **AppsPython**! Este es un **repositorio educativo** diseñado específicamente para el aprendizaje, desarrollo y perfeccionamiento de habilidades en **programación web avanzada utilizando Python**.

Aquí encontrarás una colección curada de ejercicios, proyectos y prácticas que exploran conceptos avanzados del desarrollo web backend y full-stack con Python.

---

## 🎯 Enfoque del Repositorio

Este espacio está estructurado para servir como una guía práctica y avanzada en el ecosistema web de Python. Los ejercicios están orientados a:

*   **Desarrollo de APIs Robustas:** Creación de servicios RESTful y GraphQL rápidos, seguros y escalables utilizando frameworks modernos como FastAPI, Flask y Django.
*   **Arquitectura de Software y Patrones de Diseño:** Implementación de patrones de diseño limpios, inyección de dependencias y separación de responsabilidades.
*   **Gestión de Bases de Datos:** Integración y optimización de bases de datos relacionales y no relacionales mediante ORMs (SQLAlchemy, Tortoise ORM, MongoEngine) y consultas optimizadas.
*   **Seguridad y Autenticación:** Implementación de JWT (JSON Web Tokens), OAuth2, hashing de contraseñas y control de acceso basado en roles (RBAC).
*   **Pruebas Automatizadas:** Creación de suites de pruebas robustas utilizando pytest, mocks y pruebas de integración para asegurar la calidad del código.
*   **Procesamiento Asíncrono:** Uso eficiente de `asyncio`, tareas en segundo plano y colas de mensajería (Celery/Redis).

---

## 🚀 Tecnologías Destacadas

*   **Lenguaje Principal:** Python 3.10+
*   **Frameworks Web:** FastAPI, Django, Flask.
*   **Bases de Datos & ORMs:** PostgreSQL, SQLite, SQLAlchemy, Tortoise ORM.
*   **Herramientas de Soporte:** Docker, Pytest, Pydantic, Celery, Redis.

---

## 📚 Propósito Educativo

Cada ejercicio y proyecto dentro de este repositorio incluye:
1.  **Código Limpio (Clean Code):** Adhesión estricta a PEP 8 y buenas prácticas de tipado estático (`mypy`).
2.  **Explicaciones Detalladas:** Documentación interna y comentarios que explican el *porqué* de cada decisión técnica.
3.  **Retos y Extensiones:** Propuestas de mejora para que puedas continuar explorando y expandiendo tus conocimientos de manera autónoma.

---

## 🛠️ Configuración Inicial y Cómo Empezar

Para comenzar a trabajar con los ejercicios de este repositorio localmente, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/yadicabeza-hub/appspython.git
cd appspython
```

### 2. Crear y activar un entorno virtual
Es altamente recomendable utilizar un entorno virtual para aislar las dependencias del proyecto:

*   **En Windows (PowerShell/CMD):**
    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1   # En PowerShell
    # o bien:
    .venv\Scripts\activate.bat   # En CMD
    ```
*   **En macOS/Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### 3. Instalar dependencias
Una vez activado el entorno virtual, instala las herramientas de desarrollo y dependencias necesarias:
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

---

## Arquitectura spec-as-source (IA + aplicación)

El repositorio separa **orquestación para el agente de IA** del **código ejecutable**:

```text
appspython/
├── spec/                     # Fuente de verdad: planes, norte, checklists
│   ├── norte-proyecto.md     # Visión y límites del sistema
│   ├── planes/               # Un plan por solicitud (NNN-slug.md)
│   └── checklists/           # Testing y seguridad transversales
├── skill/                    # Skills del proyecto para ejecutar planes
│   ├── orquestacion-spec-as-source/
│   └── ejecutar-plan/
├── app/                      # Aplicación (sin importar spec/ ni skill/)
│   └── examples/             # Scripts educativos
├── tests/                    # Pytest (espejo de app/)
├── requirements-dev.txt      # pytest, etc.
└── README.md
```

### Flujo obligatorio para cada solicitud

1. **Planificar** en `spec/planes/` (objetivo, alcance, etapas, tests, seguridad).
2. **Skill** en `skill/` alineada al plan; el agente no codifica en `app/` hasta terminar el paso 1.
3. **Ejecutar** por etapas con `skill/ejecutar-plan/`, validando checklists antes de avanzar.
4. **Implementar** solo en `app/` y `tests/`.

Detalle: `spec/README.md`, `skill/README.md`, plan bootstrap: `spec/planes/001-bootstrap-arquitectura-spec-as-source.md`.

---

## Estructura de la aplicación (`app/`)

Para ejercicios web avanzados se adopta arquitectura limpia por capas (ver `app/README.md`):

```text
app/
├── api/v1/          # Endpoints
├── core/            # Config y seguridad
├── models/          # ORM
├── schemas/         # Validación
├── services/        # Lógica de negocio
└── main.py          # Entrada
tests/               # Pruebas unitarias y de API
```

---

> [!NOTE]
> Este repositorio es un recurso dinámico y en constante evolución. Los módulos de ejercicios se actualizan para reflejar las últimas tendencias y mejores prácticas de la industria en desarrollo web con Python.
