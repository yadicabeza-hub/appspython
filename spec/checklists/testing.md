# Checklist � Capa de testing

Aplicar en **cada etapa** del plan activo antes de marcar la etapa como completada.

## Definici�n (en el plan)

- [ ] Objetivo de la prueba descrito (qu� comportamiento se garantiza).
- [ ] Tipo indicado: unitaria, integraci�n o funcional (E2E/API).
- [ ] Datos de prueba y fixtures documentados (sin secretos reales).
- [ ] Criterio de aceptaci�n medible (entrada ? salida esperada).

## Unitarias (`tests/` espejo de `app/`)

- [ ] Una responsabilidad por test.
- [ ] Sin dependencia de red ni BD real salvo que el plan lo exija con mocks.
- [ ] Casos: camino feliz, vac�o/nulo, error esperado.
- [ ] Cobertura de reglas de negocio en `services/` antes que en rutas.

## Funcionales / API

- [ ] Cliente de prueba (TestClient de FastAPI, cliente Flask/Django seg�n stack).
- [ ] C�digos HTTP y cuerpo de respuesta verificados.
- [ ] Autenticaci�n/autorizaci�n probada si aplica al plan.
- [ ] Headers de seguridad relevantes comprobados cuando existan.

## Ejecuci�n

```bash
# Desde la ra�z del repo, con venv activo
pip install -r requirements-dev.txt   # cuando exista
pytest tests/ -v
```

## Bloqueo de avance

**No pasar a la siguiente etapa del plan** si:

- Falla alg�n test de la etapa actual.
- No hay tests donde el plan los exige.
- Los tests dependen de estado manual no reproducible.

## Registro en el plan

Al cerrar una etapa, anotar en el plan:

- Comando ejecutado
- Resultado (pass/fail)
- Tests a�adidos o modificados (rutas)
