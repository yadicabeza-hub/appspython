# Estado del Framework spec-as-source - AppsPython

**Fecha:** 25 de mayo de 2026  
**Estado:** ✅ Completo y operativo

---

## 📋 Estructura de carpetas

```
appspython/
├── .instructions.md              ← Instrucciones personalizadas del agente
├── AGENTS.md                     ← Guía rápida (referencia inicial)
├── README.md                     ← Documentación del repositorio
├── app/                          ← CÓDIGO REAL (espacio seguro para implementación)
├── tests/                        ← Pruebas espejo de app/
├── spec/                         ← CAPA DE ORQUESTACIÓN (plans, diseño)
│   ├── norte-proyecto.md         ← Visión, principios, criterios de éxito
│   ├── planes/                   ← Plans activos (NNN-<slug>.md)
│   ├── checklists/
│   │   ├── testing.md            ← Validación de pruebas por etapa
│   │   └── seguridad.md          ← Validación de seguridad por etapa
│   └── README.md
├── skill/                        ← SKILLS DE EJECUCIÓN (cómo ejecutar)
│   ├── orquestacion-spec-as-source/
│   │   └── SKILL.md              ← Guía de 4 fases (A, B, C, D)
│   ├── ejecutar-plan/
│   │   └── SKILL.md              ← Ejecución por etapas (hoja de ruta)
│   └── README.md
└── spa-system/                   ← Sistema específico (no crítico)
```

---

## 🎯 Visión del proyecto (norte-proyecto.md)

**Repositorio educativo** para **programación web avanzada con Python**, donde:
- El desarrollo lo **guía un agente de IA** bajo **spec-as-source**
- **Planificar antes de codificar**
- **Ejecutar por etapas**
- **Validar con testing y seguridad** en cada paso

### Principios no negociables
1. **Spec primero:** toda solicitud → plan en `spec/planes/` antes de tocar `app/`
2. **Skill como ejecutor:** la skill en `skill/` traduce plan → tareas; no improvisación
3. **Separación de capas:** `spec/` y `skill/` NO acopladas a frameworks de `app/`
4. **Ejecución progresiva:** una etapa a la vez; validar antes de avanzar
5. **Calidad transversal:** testing y seguridad obligatorios en cada plan

---

## 🔄 Flujo de trabajo (spec-as-source)

### Fase A - Contexto (lectura)
- Leer `spec/norte-proyecto.md`
- Explorar `spec/planes/` ← ¿existe plan relacionado?
- Explorar `app/` y `tests/` sin modificar

**Gate:** Nada modificado. Solo lectura.

### Fase B - Planificación (escritura en spec/)
Crear `spec/planes/NNN-<slug>.md` con:
- Objetivo, Alcance, Pasos de implementación
- Testing por etapa (ver `spec/checklists/testing.md`)
- Seguridad por etapa (ver `spec/checklists/seguridad.md`)
- Riesgos y supuestos
- Skill de ejecución

**Gate:** Plan aprobable; etapas claras.

### Fase C - Skill de ejecución
- Crear skill en `skill/` o usar `skill/ejecutar-plan/SKILL.md`
- Dividir cada etapa en tareas ≤ 15 minutos
- Enlazar tareas al plan (Etapa X → T1, T2, T3)

**Gate:** Skill alineada al plan.

### Fase D - Handoff a ejecución
- Comunicar: plan + skill listos
- Ejecutar por etapas
- Validar testing y seguridad antes de avanzar

**Gate:** No avanzar sin validación completa de etapa anterior.

---

## ✅ Checklists de validación

### Testing (`spec/checklists/testing.md`)
Aplicar **por cada etapa** antes de marcar completada:
- [ ] Objetivo de prueba descrito
- [ ] Tipo indicado (unitaria, integración, E2E)
- [ ] Datos y fixtures documentados
- [ ] Criterio de aceptación medible
- Ejecutar: `pytest tests/ -v`

### Seguridad (`spec/checklists/seguridad.md`)
Aplicar al **diseño** (plan) y **cierre de etapa**:
- [ ] Validación de entradas
- [ ] Secretos fuera de código (`.env`)
- [ ] Autenticación/autorización si aplica
- [ ] Consultas parametrizadas (sin SQL inyectable)
- [ ] Headers de seguridad HTTP
- [ ] Dependencias auditadas

---

## 📁 Planes existentes

Ver `spec/planes/` para planes previos. Referencia:
- `001-bootstrap-arquitectura-spec-as-source.md` (si existe) - Plan de inicialización

**Para crear nuevo plan:** `NNN-<slug>.md` (NNN = número secuencial)

---

## 🚀 Cómo usar esto

### Solicitud nueva
1. Seguir Fases A, B, C, D
2. Crear plan en `spec/planes/NNN-<slug>.md`
3. Invocar skill de ejecución
4. Ejecutar por etapas, validando en cada gate

### Solicitud de seguimiento
1. Leer plan existente en `spec/planes/`
2. Ubicar etapa incompleta o nueva
3. Ejecutar skill desde esa etapa
4. Registrar progreso en plan

---

## 🛡️ Separación de capas (NO NEGOCIABLE)

```
┌─────────────────────────────────┐
│ spec/ + skill/ (Orquestación)   │
│ - Planes, diseño, requerimientos│
│ - SIN acoplamiento a frameworks │
│ - SIN código de negocio         │
└─────────────────────────────────┘
            ↓ (guía)
┌─────────────────────────────────┐
│ app/ (Código Real)              │
│ - FastAPI, Flask, Django        │
│ - Modelos, schemas, services    │
│ - INDEPENDIENTE de spec/skill/  │
└─────────────────────────────────┘
            ↓ (valida)
┌─────────────────────────────────┐
│ tests/ (Pruebas)                │
│ - Espejo de app/                │
│ - Unitarias, integración, E2E   │
└─────────────────────────────────┘
```

---

## 📞 Referencia rápida del agente

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué estamos construyendo? | `spec/norte-proyecto.md` |
| ¿Qué hacer en esta solicitud? | `spec/planes/<plan-activo>.md` |
| ¿Cómo ejecutarlo paso a paso? | `skill/<skill>/SKILL.md` |
| ¿Cómo validar tests? | `spec/checklists/testing.md` + plan |
| ¿Cómo validar seguridad? | `spec/checklists/seguridad.md` + plan |
| ¿Dónde programo? | `app/` (después de plan aprobado) |

---

## ⚠️ Bloqueos de avance

**NO avanzar a siguiente etapa si:**
- ❌ Tests fallidos
- ❌ Faltan tests donde el plan los exige
- ❌ Hallazgo de seguridad crítico/alto sin documentación
- ❌ Etapa anterior sin registrar resultado

**Si hay bloqueador:** Documentar en plan y comunicar al usuario.

---

## 🚫 Anti-patrones (PROHIBIDO)

- Crear código en `app/` sin plan activo
- Omitir testing o seguridad "para después"
- Lógica de negocio en `spec/` o `skill/`
- Importar o acoplar `app/` a `spec/` o `skill/`
- Desviaciones no documentadas del plan

---

**Marco completo:** spec-as-source v1.0  
**Próximo paso:** Await para nueva solicitud con plan activo.
