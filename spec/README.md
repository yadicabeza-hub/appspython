# Capa de especificaci�n (`spec/`)

Esta carpeta es la **fuente de verdad** para la orquestaci�n del agente de IA. No contiene l�gica de aplicaci�n.

## Contenido

| Ruta | Prop�sito |
|------|-----------|
| `norte-proyecto.md` | Visi�n, principios y l�mites del sistema |
| `planes/` | Planes detallados por solicitud (una spec por feature o cambio) |
| `checklists/` | Capas transversales: testing y seguridad |

## Convenci�n de nombres

```
planes/NNN-<slug-descriptivo>.md
```

Ejemplo: `planes/001-bootstrap-arquitectura-spec-as-source.md`

## Flujo obligatorio del agente

1. Leer `norte-proyecto.md`.
2. Localizar o crear el plan en `planes/` para la solicitud actual.
3. Cargar la skill correspondiente en `skill/` (mismo slug o referencia expl�cita en el plan).
4. **No modificar `app/`** hasta completar an�lisis del plan y definir pruebas en el plan.
5. Ejecutar por etapas; marcar cada etapa en el plan antes de avanzar.

## Plantilla de plan

Cada plan debe incluir:

- Objetivo
- Alcance (in / out)
- Pasos de implementaci�n (etapas numeradas)
- Capa de testing (unitarias + funcionales por etapa)
- Capa de seguridad (checklist aplicado)
- Riesgos y supuestos
- Referencia a skill: `skill/<nombre>/SKILL.md`
