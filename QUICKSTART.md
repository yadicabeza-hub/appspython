# 🚀 ARRANQUE RÁPIDO - Próxima solicitud

**Fecha:** 25 de mayo de 2026

---

## ✅ Marco spec-as-source: LISTO

Tu agente IA está configurado para seguir el flujo:

```
Solicitud → Fase A (contexto) → Fase B (plan) → Fase C (skill) → Fase D (ejecución)
                     ↓              ↓             ↓               ↓
                  Lectura      spec/planes/   skill/          app/ 
                            + testing.md    executable      + tests/
                            + seguridad.md
```

---

## 📂 Archivos de referencia (ya creados)

| Archivo | Propósito |
|---------|-----------|
| `.instructions.md` | Instrucciones personalizadas del agente |
| `FRAMEWORK.md` | Estado y estructura completa |
| `spec/norte-proyecto.md` | Visión y principios |
| `spec/checklists/testing.md` | Validación de pruebas |
| `spec/checklists/seguridad.md` | Validación de seguridad |
| `spec/planes/README.md` | Template de planes |
| `skill/orquestacion-spec-as-source/SKILL.md` | Guía de 4 fases |
| `skill/ejecutar-plan/SKILL.md` | Ejecución por etapas |

---

## 🎯 Cuando recibas nueva solicitud

### 1. Agente IA lee:
```
1. Este archivo (próxima solitud)
2. .instructions.md (cómo proceder)
3. spec/norte-proyecto.md (contexto)
```

### 2. Agente clasifica:
- ¿Existe plan para esta solicitud?
  - **SÍ** → ir a Fase D (ejecución)
  - **NO** → iniciar Fase A (contexto)

### 3. Agente crea plan (Fase B):
```bash
# Crear archivo
spec/planes/NNN-<slug>.md

# Incluir
- Objetivo, Alcance, Pasos
- Testing por etapa
- Seguridad por etapa
- Riesgos
```

### 4. Agente prepara skill (Fase C):
```bash
# Usar por defecto
skill/ejecutar-plan/SKILL.md

# O crear
skill/<slug>/SKILL.md (si es especializada)
```

### 5. Agente comunica:
```
✅ Plan creado: spec/planes/NNN-<slug>.md
✅ Skill lista: skill/ejecutar-plan/SKILL.md
📋 Etapas: [listar]
🔗 Referencias: [checklists aplicados]

¿Procedo con Fase D (ejecución)?
```

---

## ⚠️ Reglas de oro

```
❌ PROHIBIDO               ✅ OBLIGATORIO
─────────────────────────────────────────
Sin plan → código          Plan → Skill → Código
Omitir testing/security    Testing + Security en cada etapa
Lógica negocio en spec/    Lógica negocio en app/
Desviar del plan           Documentar cambios
```

---

## 📊 Métricas de progreso

Por cada solicitud:
- [ ] Plan creado en `spec/planes/`
- [ ] Etapas con testing definido
- [ ] Etapas con seguridad revisada
- [ ] Skill de ejecución lista
- [ ] Cada etapa ejecutada y validada
- [ ] Tests pasando: `pytest tests/ -v`
- [ ] Progreso registrado en plan

---

## 🔗 Referencia rápida (1 minuto)

| Necesito | Voy a |
|----------|-------|
| Crear nuevo plan | `cp spec/planes/README.md spec/planes/NNN-<slug>.md` |
| Leer norte | `cat spec/norte-proyecto.md` |
| Ver checklist testing | `cat spec/checklists/testing.md` |
| Ver checklist seguridad | `cat spec/checklists/seguridad.md` |
| Ver instrucciones agente | `cat .instructions.md` |
| Ver skill ejecución | `cat skill/ejecutar-plan/SKILL.md` |

---

## 🎬 Ejemplo de flujo completo

### Solicitud: "Crear endpoint POST /usuarios"

**Fase A - Contexto**
- Leer norte, explorar app/, revisar planes existentes
- Anotar: "Base de datos no existe, necesitamos modelo User"

**Fase B - Planificación**
- Crear `spec/planes/002-crud-usuarios.md`
- 4 etapas: modelo → schema → servicio → endpoint
- Testing por etapa (unitaria, funcional)
- Seguridad: validación, hashing, RBAC

**Fase C - Skill**
- Usar `skill/ejecutar-plan/SKILL.md`
- Tareas: ≤15 min cada una
- T1 = modelo, T2 = schema, T3 = servicio, T4 = endpoint

**Fase D - Ejecución**
- Ejecutar T1 → test → avanzar
- Ejecutar T2 → test → avanzar
- Ejecutar T3 → test → avanzar
- Ejecutar T4 → test → avanzar
- Etapa 1 completada ✅

---

## 💡 Tips

1. **Antes de abrir editor:** Lee el plan (no te lo saltees)
2. **Testing primero:** Escribe test antes que código (si aplica)
3. **Pequeñas tareas:** Divide en increments ≤15 min
4. **Gate cada etapa:** No avances sin validación completa
5. **Documenta cambios:** Registra en plan al terminar etapa

---

## 📞 Si hay dudas

1. Releer `spec/norte-proyecto.md` (principios)
2. Releer `.instructions.md` (procedimiento)
3. Releer `spec/checklists/testing.md` o `seguridad.md` (validaciones)
4. Comunicar bloqueos al usuario con contexto

---

**Marco:** spec-as-source v1.0  
**Estado:** ✅ Operativo y listo para primera solicitud  
**Próximo:** Await nueva solicitud con este flujo

---

*Creado: 25 de mayo de 2026*
