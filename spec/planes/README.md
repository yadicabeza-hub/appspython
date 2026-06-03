# Template - Creador de planes (spec/planes/)

Usa esta plantilla para crear nuevo plan: `spec/planes/NNN-<slug>.md`

---

```markdown
# Plan NNN - <Título descriptivo>

**Fecha de creación:** [fecha]  
**Estado:** 🔵 Planificación  
**Agente responsable:** IA/Dev  

---

## 📌 Objetivo

[Qué se logra con este plan. Una frase clara.]

Ejemplo: "Crear endpoint de autenticación con JWT que valide credenciales y retorne token seguro."

---

## 📊 Alcance

### Módulos/Archivos a tocar
- `app/api/` - [qué cambios]
- `app/models/` - [qué cambios]
- `app/services/` - [qué cambios]
- `tests/` - [nuevas pruebas]

### Fuera de alcance
- [Qué NO hacemos en este plan]

### Supuestos
- [Qué asumimos que es verdadero]

---

## 🛣️ Pasos de implementación

### Etapa 1 - [Título breve]
**Descripción:** [Qué se implementa]

**Cambios esperados:**
- [ ] Archivo/módulo 1
- [ ] Archivo/módulo 2

**Testing:**
- [ ] Test unitario: [qué valida]
- [ ] Test funcional: [qué valida]

**Seguridad:**
- [ ] [Aplicar checklist item 1]
- [ ] [Aplicar checklist item 2]

**Status:** ⭕ Pendiente

---

### Etapa 2 - [Título breve]
**Descripción:** [Qué se implementa]

[Repetir estructura de Etapa 1]

**Status:** ⭕ Pendiente

---

[Agregar más etapas según sea necesario]

---

## 🧪 Testing (aplicar spec/checklists/testing.md)

Por cada etapa:

| Etapa | Tipo | Objetivo | Entrada | Salida esperada | Status |
|-------|------|----------|---------|-----------------|--------|
| 1 | Unitaria | Validar [qué] | [dato] | [resultado] | ⭕ |
| 1 | Funcional | Validar [qué] | [HTTP request] | [código + cuerpo] | ⭕ |
| 2 | Unitaria | Validar [qué] | [dato] | [resultado] | ⭕ |

---

## 🔒 Seguridad (aplicar spec/checklists/seguridad.md)

- [ ] **Entradas y validación:** [decisión]
- [ ] **Secretos y configuración:** [decisión]
- [ ] **Autenticación/autorización:** [decisión]
- [ ] **Datos y persistencia:** [decisión]
- [ ] **HTTP y API:** [decisión]
- [ ] **Dependencias:** [decisión]

---

## ⚠️ Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|--------|-----------|
| [Riesgo 1] | Alta/Media/Baja | Alto/Medio/Bajo | [Cómo lo evitamos] |
| [Riesgo 2] | - | - | - |

---

## 🎯 Skill de ejecución

**Usar:** `skill/ejecutar-plan/SKILL.md` o `skill/<slug>/SKILL.md`

---

## 📝 Progreso

### Etapa 1
- [ ] Tarea iniciada
- [ ] Código escrito
- [ ] Tests ejecutados (resultado: [pass/fail])
- [ ] Seguridad validada
- [ ] Documentado en archivo: [ruta]

**Finalización:** 🟡 En progreso

### Etapa 2
- [ ] Pendiente

---

## 🔗 Referencias

- Norte del proyecto: `spec/norte-proyecto.md`
- Testing: `spec/checklists/testing.md`
- Seguridad: `spec/checklists/seguridad.md`
- Skill: `skill/ejecutar-plan/SKILL.md`

---

**Última actualización:** [fecha]  
**Siguiente acción:** [qué sigue]
```

---

## 📋 Instrucciones de uso

1. **Copiar template** a `spec/planes/NNN-<slug>.md`
2. **Reemplazar** [placeholders] con valores específicos
3. **Completar** todas las secciones (no dejar en blanco)
4. **Gate:** Plan listo cuando:
   - ✅ Todas las etapas numeradas
   - ✅ Testing definido (spec/checklists/testing.md)
   - ✅ Seguridad revisada (spec/checklists/seguridad.md)
   - ✅ Riesgos identificados
   - ✅ Sin código de app dentro (solo pseudológica)

---

**Ejemplo de nombre de plan:**
- `001-setup-fastapi-inicial.md`
- `002-autenticacion-jwt.md`
- `003-crud-usuarios.md`

Use números secuenciales para orden claro.
