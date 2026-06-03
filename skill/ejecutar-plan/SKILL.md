---
name: ejecutar-plan
description: >-
  Ejecuta un plan existente en spec/planes/ por etapas: implementar en app/,
  a�adir tests, aplicar checklist de seguridad, marcar etapa en el plan antes
  de continuar. Usar solo cuando el plan y la skill ya existen.
---

# Ejecutar plan por etapas

## Prerrequisitos

- Plan activo: `spec/planes/NNN-<slug>.md` (campo **Estado** ? Cancelado).
- Haber completado `skill/orquestacion-spec-as-source/` si el plan era nuevo.

## STOP � Inicio de cada sesi�n

1. Leer `spec/norte-proyecto.md` (1 min).
2. Leer plan completo y localizar **primera etapa sin [x]**.
3. No trabajar en etapas posteriores hasta cerrar la actual.

## Ciclo por etapa (repetir)

### 1. An�lisis (sin c�digo nuevo salvo lectura)

| Paso | Acci�n |
|------|--------|
| 1.1 | Leer tareas de la etapa en el plan |
| 1.2 | Listar archivos a tocar en `app/` o `tests/` |
| 1.3 | Listar pruebas exigidas para la etapa |

### 2. Implementaci�n m�nima (`app/` y `tests/`)

| Paso | Acci�n |
|------|--------|
| 2.1 | Cambios solo al alcance de la etapa |
| 2.2 | Escribir tests definidos en el plan |
| 2.3 | Ejecutar `pytest tests/ -v` (o comando del plan) |

**Gate testing:** Todos los tests de la etapa en verde. Si falla ? corregir antes de seguir.

### 3. Seguridad

| Paso | Acci�n |
|------|--------|
| 3.1 | Recorrer `spec/checklists/seguridad.md` |
| 3.2 | Corregir hallazgos cr�ticos/altos o documentar en el plan |
| 3.3 | Anotar �tems aplicados en secci�n del plan |

**Gate seguridad:** Sin hallazgos cr�ticos abiertos.

### 4. Cierre de etapa

| Paso | Acci�n |
|------|--------|
| 4.1 | Marcar `[x]` en las tareas de la etapa dentro del plan |
| 4.2 | A�adir fila en **Registro de ejecuci�n** del plan |
| 4.3 | Si era la �ltima etapa ? **Estado: Completado** |

### 5. Siguiente etapa

Volver al **Ciclo por etapa** con la siguiente secci�n numerada del plan.

## Reglas de alcance

- No refactorizar c�digo fuera del alcance de la etapa actual.
- No a�adir dependencias no listadas en el plan sin actualizar el plan primero.
- Desviaciones: parar, actualizar plan (nueva sub-etapa o riesgo documentado), luego continuar.

## Salida esperada al usuario

Por etapa cerrada, reportar brevemente:

1. Qu� se implement�
2. Resultado de pytest
3. Seguridad: OK o excepciones documentadas
4. Siguiente etapa o cierre del plan

## Plan activo (bootstrap)

Para la sesi�n inicial del repositorio, usar:

`spec/planes/001-bootstrap-arquitectura-spec-as-source.md`

Etapa actual: leer el plan y ejecutar la primera etapa pendiente.
