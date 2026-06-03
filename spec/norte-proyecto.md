# Norte del proyecto ? AppsPython

## Visi�n

Repositorio educativo para **programaci�n web avanzada con Python**, donde el desarrollo lo gu�a un agente de IA bajo el enfoque **spec-as-source**: planificar antes de codificar, ejecutar por etapas y validar con testing y seguridad en cada paso.

## Principios no negociables

1. **Spec primero**: toda solicitud genera o actualiza un plan en `spec/planes/` antes de tocar `app/`.
2. **Skill como ejecutor**: la skill en `skill/` traduce el plan en tareas peque?as; el agente no improvisa fuera de la skill activa.
3. **Separaci�n de capas**: `spec/` y `skill/` no importan ni acoplan c�digo de `app/` (sin dependencias cruzadas hacia frameworks).
4. **Ejecuci�n progresiva**: una etapa a la vez; no avanzar sin validaci�n de la etapa anterior.
5. **Calidad transversal**: testing y seguridad son obligatorios en cada plan, no opcionales al final.

## Alcance del producto (app/)

- APIs y servicios web con Python (FastAPI, Flask, Django seg�n el ejercicio).
- Arquitectura por capas: `api/`, `core/`, `models/`, `schemas/`, `services/`.
- Pruebas con pytest bajo `tests/` (hermano de `app/`, no dentro de `spec/` ni `skill/`).

## Fuera de alcance (por ahora)

- Despliegue a producci�n automatizado.
- Secretos o credenciales en el repositorio.
- L�gica de negocio embebida en archivos de `spec/` o `skill/`.

## Criterios de �xito de una solicitud

- [ ] Plan aprobado o revisado en `spec/planes/`.
- [ ] Skill creada o actualizada en `skill/`.
- [ ] Cambios en `app/` alineados al plan, sin desviaciones no documentadas.
- [ ] Pruebas definidas y ejecutadas seg�n el plan.
- [ ] Checklist de seguridad aplicado y hallazgos resueltos o documentados.

## Referencia r�pida para el agente

| Pregunta | D�nde mirar |
|----------|-------------|
| ?Qu� estamos construyendo y por qu�? | Este archivo |
| ?Qu� hacer en esta solicitud? | `spec/planes/<plan-activo>.md` |
| ?C�mo ejecutarlo paso a paso? | `skill/<skill>/SKILL.md` |
| ?C�mo validar tests? | `spec/checklists/testing.md` + plan activo |
| ?C�mo validar seguridad? | `spec/checklists/seguridad.md` + plan activo |
