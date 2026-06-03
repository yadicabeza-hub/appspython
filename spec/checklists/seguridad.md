# Checklist � Capa de seguridad

Aplicar al **dise�o** (en el plan) y al **cierre de cada etapa** en `app/`.

## Entradas y validaci�n

- [ ] Toda entrada externa validada (esquemas Pydantic, formularios, query params).
- [ ] L�mites de tama�o y tipos acotados; sin confianza en datos del cliente.
- [ ] Sanitizaci�n de salida que se renderice en HTML (si aplica).

## Secretos y configuraci�n

- [ ] Sin API keys, passwords ni tokens en el c�digo ni en `spec/` / `skill/`.
- [ ] Variables sensibles solo v�a entorno (`.env` ignorado por git; `.env.example` sin valores reales).
- [ ] `DEBUG=False` y configuraci�n restrictiva documentada para entornos no locales.

## Autenticaci�n y autorizaci�n (cuando aplique)

- [ ] Contrase�as con hashing fuerte (bcrypt/argon2), nunca en texto plano.
- [ ] Tokens con expiraci�n y revocaci�n consideradas en el dise�o.
- [ ] RBAC o permisos m�nimos necesarios por endpoint.
- [ ] Rate limiting considerado en endpoints p�blicos sensibles.

## Datos y persistencia

- [ ] Consultas parametrizadas / ORM; sin SQL concatenado con input de usuario.
- [ ] Principio de m�nimo privilegio en credenciales de BD.
- [ ] Datos personales: solo campos necesarios; logs sin PII.

## HTTP y API

- [ ] HTTPS asumido en despliegue; cookies `Secure`/`HttpOnly` si se usan sesiones.
- [ ] CORS restringido a or�genes expl�citos, no `*` en producci�n.
- [ ] Cabeceras: `Content-Security-Policy`, `X-Content-Type-Options`, etc. seg�n stack.
- [ ] Mensajes de error gen�ricos al cliente; detalle solo en logs internos.

## Dependencias

- [ ] Versiones fijadas en `requirements.txt` / lockfile.
- [ ] Revisi�n de vulnerabilidades conocidas (`pip audit` o equivalente) antes de cerrar feature.

## Bloqueo de avance

**No pasar a la siguiente etapa** si hay hallazgo cr�tico o alto sin mitigaci�n documentada en el plan.

## Registro en el plan

- �tems del checklist aplicados (s�/no + nota breve).
- Riesgos aceptados temporalmente y plan de remediaci�n.
