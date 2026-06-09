---
name: orquestacion-spec-as-source
description: >-
  Orquesta solicitudes nuevas bajo spec-as-source: leer norte, crear o
  actualizar plan en spec/, crear skill de ejecuci�n, prohibir c�digo en app/
  hasta planificar. Usar en toda solicitud de feature o cambio estructural.
---

# Orquestaci�n spec-as-source

## STOP � Antes de programar

Si **no existe** un plan en `spec/planes/` para la solicitud actual:

1. **Detener** cualquier edici�n en `app/`.
2. Completar las fases de este documento.
3. Solo entonces invocar `skill/ejecutar-plan/SKILL.md`.

## Fase A � Contexto (solo lectura)

| Tarea | Acci�n | Salida |
|-------|--------|--------|
| A.1 | Leer `spec/norte-proyecto.md` | Resumen mental: visi�n y l�mites |
| A.2 | Leer plan existente si hay slug relacionado en `spec/planes/` | �Extender plan o nuevo NNN? |
| A.3 | Explorar `app/` y `tests/` **sin modificar** | Estado actual anotado |

**Gate:** Ning�n archivo en `app/` modificado en Fase A.

## Fase B � Planificaci�n (escritura en spec/)

| Tarea | Acci�n | Salida |
|-------|--------|--------|
| B.1 | Asignar ID: siguiente `NNN` en `spec/planes/` | Nombre archivo `NNN-<slug>.md` |
| B.2 | Redactar plan con: Objetivo, Alcance, Pasos, Testing, Seguridad, Riesgos | Plan completo |
| B.3 | Por cada etapa del plan, definir pruebas (ver `spec/checklists/testing.md`) | Tabla tests en el plan |
| B.4 | Aplicar `spec/checklists/seguridad.md` al dise�o | Secci�n seguridad en el plan |
| B.5 | Indicar skill de ejecuci�n: nueva o `ejecutar-plan` | Campo **Skill** en el plan |

**Gate:** Plan revisable; etapas numeradas; sin c�digo de aplicaci�n en el plan (solo pseudol�gica o rutas futuras).

## Fase C � Skill de ejecuci�n

| Tarea | Acci�n | Salida |
|-------|--------|--------|
| C.1 | Crear `skill/<slug-ejecucion>/SKILL.md` o usar `ejecutar-plan` | Skill referenciada en el plan |
| C.2 | Dividir implementaci�n en tareas ? 15 min cada una | Lista ordenada con gates |
| C.3 | Enlazar cada tarea a etapa del plan | IDs alineados (ej. Etapa 2 ? T2.x) |

**Gate:** Skill no importa ni menciona rutas internas de frameworks salvo como texto gen�rico ("capa api").

## Fase D � Handoff a ejecuci�n

| Tarea | Acci�n | Salida |
|-------|--------|--------|
| D.1 | Informar al usuario: plan + skill listos | Rutas exactas |
| D.2 | Preguntar solo si alcance es ambiguo cr�tico | Una pregunta concreta m�ximo |
| D.3 | Abrir `skill/ejecutar-plan/SKILL.md` con el plan activo | Ejecuci�n por etapas |

## Anti-patrones (prohibido)

- Crear endpoints o modelos en `app/` antes de B.5.
- Un solo archivo monol�tico sin etapas en el plan.
- Omitir testing o seguridad "para despu�s".
- Copiar l�gica de negocio dentro de `skill/`.

## Referencias

- Norte: `spec/norte-proyecto.md`
- Checklists: `spec/checklists/testing.md`, `spec/checklists/seguridad.md`
- Bootstrap: `spec/planes/001-bootstrap-arquitectura-spec-as-source.md`
