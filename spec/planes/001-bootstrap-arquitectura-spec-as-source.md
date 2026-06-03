# Plan 001 - Bootstrap arquitectura spec-as-source

**Estado:** Completado  
**Skill:** `skill/orquestacion-spec-as-source/SKILL.md`  
**Solicitud:** Establecer framework de orquestacion IA (spec / skill / app) sin acoplar capas.

---

## Objetivo

Instalar en el repositorio la estructura y reglas del enfoque **spec-as-source**, de modo que todo desarrollo futuro pase por planificacion (`spec/`), ejecucion guiada (`skill/`) e implementacion aislada (`app/`), con capas obligatorias de testing y seguridad.

## Alcance

### Incluido

- Carpetas `spec/`, `skill/`, `app/` con documentacion y convenciones.
- Norte del proyecto y checklists transversales.
- Skills maestras de orquestacion y ejecucion por etapas.
- Esqueleto de `app/` y ubicacion de ejemplo previo (`python.py` -> `app/examples/`).
- Carpeta `tests/` con prueba minima de humo del esqueleto.
- Actualizacion de `README.md` raiz describiendo las tres capas.

### Excluido

- API web completa, FastAPI/Django en produccion.
- CI/CD, Docker, despliegue.
- Migracion masiva de ejercicios aun no planificados.

## Pasos de implementacion

### Etapa 1 - Capa spec (orquestacion)

| # | Tarea | Validacion |
|---|--------|------------|
| 1.1 | `spec/README.md`, `norte-proyecto.md` | Archivos presentes y enlazados |
| 1.2 | Checklists `testing.md`, `seguridad.md` | Listas completas y referenciadas en README spec |
| 1.3 | Este plan `001-bootstrap-...` | Secciones Objetivo-Riesgos completas |

**Testing etapa 1:** Revision documental - no hay codigo; criterio: plan autocontenido y checklists referenciables.  
**Seguridad etapa 1:** Checklist seguridad creado; sin secretos en spec.

- [x] Etapa 1 completada

### Etapa 2 - Capa skill

| # | Tarea | Validacion |
|---|--------|------------|
| 2.1 | `skill/orquestacion-spec-as-source/SKILL.md` | Frontmatter + flujo spec-first |
| 2.2 | `skill/ejecutar-plan/SKILL.md` | Tareas por etapa + gates testing/seguridad |
| 2.3 | `skill/README.md` | Indice de skills del repo |

**Testing etapa 2:** Agente puede seguir skill sin ambiguedad (revision de pasos numerados).  
**Seguridad etapa 2:** Skill prohibe escribir secretos y exige checklist antes de cerrar etapa.

- [x] Etapa 2 completada

### Etapa 3 - Capa app (esqueleto)

| # | Tarea | Validacion |
|---|--------|------------|
| 3.1 | `app/README.md` con reglas de no acoplamiento a spec/skill | Documentado |
| 3.2 | Mover `python.py` -> `app/examples/hola_mundo.py` (UTF-8 corregido) | Script ejecutable |
| 3.3 | Reservar estructura futura `api/`, `core/`, etc. (solo en README app) | Sin codigo prematuro |

**Testing etapa 3:** `tests/test_examples_hola_mundo.py` - prueba de salida por import.  
**Seguridad etapa 3:** Ejemplo sin datos sensibles; sin `eval`/`exec` de input externo.

- [x] Etapa 3 completada

### Etapa 4 - Cierre bootstrap

| # | Tarea | Validacion |
|---|--------|------------|
| 4.1 | README raiz actualizado | Diagrama spec / skill / app |
| 4.2 | Marcar plan como Completado | Todas las etapas [x] |
| 4.3 | `requirements-dev.txt` minimo (pytest) | `pytest` pasa |

**Testing etapa 4:** `pytest tests/ -v` exit code 0.  
**Seguridad etapa 4:** `.gitignore` incluye `.env`, `__pycache__`, `.venv`.

- [x] Etapa 4 completada

## Capa de testing (resumen del plan)

| Etapa | Unitarias | Funcionales |
|-------|-----------|-------------|
| 1 | N/A (docs) | N/A |
| 2 | N/A (docs) | N/A |
| 3 | Test salida `hola_mundo` | N/A |
| 4 | Suite pytest raiz | N/A |

## Capa de seguridad (resumen del plan)

- Checklist completo en `spec/checklists/seguridad.md`.
- Bootstrap: sin endpoints expuestos; ejemplo local solo.
- `.gitignore` ampliado en etapa 4.

## Riesgos y supuestos

| Riesgo | Mitigacion |
|--------|------------|
| Agente salta spec y codifica directo | Skills con gate explicito "STOP si no hay plan" |
| Duplicacion README vs spec | README raiz = resumen; detalle en `spec/` |
| Confusion skill repo vs `~/.cursor/skills` | `skill/README.md` aclara que skills del proyecto viven aqui |

**Supuestos:**

- Python 3.10+ disponible en el entorno del desarrollador.
- Cursor (u otro agente) puede leer rutas `spec/` y `skill/` del workspace.
- Proximas features crearan `002-...`, `003-...` en `planes/`.

## Registro de ejecucion

| Fecha | Etapa | Agente / nota |
|-------|-------|----------------|
| 2026-05-22 | 1 | Plan y checklists creados |
| 2026-05-22 | 2-4 | Skills, app/examples, tests, README, pytest OK |
