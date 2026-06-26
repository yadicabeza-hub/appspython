# Objetivo
Desarrollar una aplicación web interactiva que exponga las fases del Ciclo de Vida del Desarrollo de Software (SDLC). La plataforma permitirá consultar información de cada fase y gestionar "Proyectos" ficticios, rastreando su avance a través de las diferentes etapas del ciclo de vida.

# Alcance
**Incluye:**
- **Arquitectura:** Patrón Modelo-Vista-Controlador (MVC) utilizando **Python con Flask**.
- **Base de Datos:** SQLite (mediante SQLAlchemy ORM) para gestionar la persistencia de las fases y los proyectos.
- **Funcionalidades Principales:**
  1. Visualización de información detallada de cada fase del SDLC (Planificación, Análisis, Diseño, Implementación, Pruebas, Despliegue, Mantenimiento).
  2. CRUD de Proyectos (Crear proyecto, asignar fase, actualizar fase, eliminar proyecto).
- **Diseño UI:** Interfaz moderna, responsiva y estética (HTML5, CSS3, animaciones dinámicas sutiles).

**No Incluye:**
- Autenticación o roles de usuario complejos (para mantener el enfoque en la arquitectura MVC y el ciclo de vida).
- Despliegue en servidores en la nube (se ejecutará de forma local en `app/`).

# Arquitectura y Diseño de Base de Datos
Implementaremos **MVC** estructurado en la carpeta `app/`:
- **Modelos (`app/models/`):** Clases `Phase` (Catálogo de fases) y `Project` (Proyectos rastreados).
- **Vistas (`app/templates/` y `app/static/`):** Plantillas Jinja2 y archivos estáticos (CSS/JS) para renderizar la UI.
- **Controladores (`app/controllers/` o rutas):** Lógica de negocio que conecta los modelos con las vistas.

**Esquema de Base de Datos Propuesto:**
- `Phase` table: `id`, `name`, `description`, `icon`.
- `Project` table: `id`, `name`, `description`, `current_phase_id` (Foreign Key a Phase), `created_at`.

# Pasos de Implementación (High-Level)
1. **Configuración del Entorno (`app/`):** Inicializar Flask, configurar SQLAlchemy y estructurar los directorios MVC.
2. **Implementación de Modelos (Base de Datos):** Crear las clases `Phase` y `Project`, y generar el script de migración/seed inicial de las 7 fases del SDLC.
3. **Implementación de Controladores:** Crear las rutas para listar fases, crear proyectos y actualizar estados.
4. **Desarrollo de Vistas (UI/UX):** Construir la interfaz de usuario priorizando un diseño visual de alta calidad.
5. **Testing & Seguridad:** Ejecutar las capas de validación.

# Riesgos y Supuestos
- **Riesgo:** Acoplamiento de la lógica de negocio en las rutas. -> **Mitigación:** Separar explícitamente los controladores y los modelos para respetar el patrón MVC puro.
- **Supuesto:** Se cuenta con Python instalado en el entorno local (windows) para ejecutar la aplicación.

# Capa de Testing
- **Pruebas Unitarias:** Pruebas automatizadas sobre los Modelos (`models.py`) para verificar la inserción y relaciones en la base de datos (usando `pytest`).
- **Pruebas Funcionales:** Pruebas sobre los endpoints principales para validar que la creación y actualización de proyectos retorne los códigos HTTP correctos.

# Capa de Seguridad
- [ ] Prevención de SQL Injection a través del uso estricto del ORM (SQLAlchemy).
- [ ] Validación de entradas en los formularios (evitar campos vacíos o tipos de datos incorrectos al crear proyectos).
- [ ] Protección contra XSS al renderizar datos en las plantillas (Jinja2 auto-escape).
