# Capa de skills (`skill/`)

Skills **del proyecto** para que el agente de IA ejecute planes definidos en `spec/`. No son skills globales de Cursor (`~/.cursor/skills-cursor/`).

## Uso

1. Leer el plan activo en `spec/planes/`.
2. Abrir la skill indicada en el campo **Skill** del plan.
3. Seguir tareas en orden; no saltar etapas.

## Skills disponibles

| Skill | Cu�ndo usarla |
|-------|----------------|
| `orquestacion-spec-as-source/` | Cualquier solicitud nueva: crear plan + skill antes de `app/` |
| `ejecutar-plan/` | Implementar un plan ya existente por etapas |

## Crear una skill nueva

- Carpeta: `skill/<nombre-kebab>/SKILL.md`
- Frontmatter YAML: `name`, `description`
- Tareas peque�as, cada una con: entrada, acci�n, salida, gate testing/seguridad
- Referenciar plan: `spec/planes/NNN-<slug>.md`

## Regla de desacoplamiento

Las skills **no deben**:

- Importar m�dulos desde `app/`
- Contener c�digo de producci�n de la aplicaci�n
- Acoplarse a FastAPI, Django u otro framework (solo mencionar rutas gen�ricas)
