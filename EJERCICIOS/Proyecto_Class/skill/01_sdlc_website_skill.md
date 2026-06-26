# Skill: Desarrollo de Arquitectura y Funcionalidad SDLC

## Contexto
**Basado en:** `spec/01_sdlc_website_plan.md`
**Objetivo:** Construir el backend (Flask, SQLite, MVC) y frontend (HTML/CSS) del sistema de seguimiento SDLC.

## Tareas a Ejecutar
- [x] **Fase 1: Preparación**
  - [x] Generar este archivo de skill.
  - [x] Inicializar artefacto de tareas (`task.md`).
- [x] **Fase 2: Arquitectura Base (Backend)**
  - [x] Crear estructura de directorios (`models`, `controllers`, `templates`, `static`).
  - [x] Escribir `requirements.txt` (Flask, Flask-SQLAlchemy, pytest).
  - [x] Configurar aplicación principal (`run.py` y configuración de BD).
- [x] **Fase 3: Modelos (Base de Datos)**
  - [x] Implementar modelo `Phase` (Fases del SDLC).
  - [x] Implementar modelo `Project` (Proyectos).
  - [x] Crear script para inicializar la base de datos con las 7 fases del SDLC.
- [x] **Fase 4: Controladores y Vistas**
  - [x] Implementar `controllers/routes.py` (Lógica de negocio).
  - [x] Crear `templates/base.html` (Plantilla maestra).
  - [x] Crear `templates/index.html` (Vista de fases del SDLC).
  - [x] Crear `templates/projects.html` (Gestor CRUD de proyectos).
  - [x] Aplicar estilos premium en `static/style.css`.
- [x] **Fase 5: Testing y Seguridad**
  - [x] Implementar un test básico en `tests/test_models.py`.
  - [x] Aplicar validación y protección XSS/SQLi (implícito por Flask/SQLAlchemy).
