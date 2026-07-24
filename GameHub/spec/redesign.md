# GameHub Indie Platform Redesign

## 1. Objetivo
Transformar la apariencia visual y la experiencia de usuario de GameHub para convertirla en una plataforma moderna de videojuegos independientes, inspirada visualmente en sitios como itch.io, pero manteniendo la identidad propia del proyecto. El sistema debe verse profesional, centrado en los creadores y los juegos.

## 2. Alcance
Se rediseñará por completo el frontend (HTML, CSS y adaptaciones en JS) conservando 100% la arquitectura existente: Python, FastAPI, MySQL, XAMPP, Jinja2 y la API REST. No se modificarán las rutas del backend ni las tablas de la base de datos. Se conservarán los identificadores HTML utilizados por el JavaScript actual para evitar romper la lógica.

## 3. Arquitectura Existente
- Backend: FastAPI, MySQL.
- Frontend: HTML renderizado con Jinja2, CSS Vanilla, JavaScript Vanilla (Fetch API).
- Autenticación: Tokens JWT almacenados en `localStorage`.

## 4. Páginas que se modificarán
- `templates/index.html` (Inicio)
- `templates/videojuegos.html` (Catálogo)
- `templates/detalle_juego.html` (Ficha del juego)
- `templates/publicar_juego.html` (Formulario de publicación)
- `templates/perfil.html` (Perfil del usuario)
- `templates/mis_juegos.html` (Dashboard del creador)
- `templates/login.html` & `templates/registro.html` (Autenticación)

## 5. Componentes Reutilizables
- **Navbar (Barra Superior):** Extraída a `templates/base.html`, compacta, con buscador y llamada a la acción principal ("Publicar juego").
- **Game Card (Tarjeta de Juego):** Estructura unificada para mostrar portadas, meta datos (género/plataforma), etiquetas, y calificación.
- **Botones y Formularios:** Estilos estándar para campos de entrada y botones de acción primaria/secundaria.

## 6. Diseño Responsive
- **Puntos de quiebre:** 1024px, 768px, 480px.
- La barra lateral de filtros en escritorio pasará a ser un panel desplegable o se integrará fluidamente en móvil.
- Cuadrícula adaptable desde 4 columnas hasta 1 columna.

## 7. Accesibilidad
- Uso correcto de etiquetas semánticas (`<nav>`, `<main>`, `<article>`, `<section>`).
- Alto contraste entre texto y fondo.
- Navegabilidad sin solapamientos en dispositivos pequeños.

## 8. Estados Visuales y Validación
- **Estados de Carga:** Indicadores visuales (spinners) mientras se obtienen datos.
- **Estados Vacíos:** Mensajes amigables si no hay juegos en el catálogo o en el perfil.
- **Estados de Error:** Manejo visual de fallos en llamadas a la API sin romper la interfaz.
- **Validación de Formularios:** Prevención de envíos dobles, deshabilitación de botones durante la carga, validación de previsualización de imágenes.

## 9. Funcionalidades a Conservar
- Registro, login y logout.
- Perfil (edición, cambio de foto).
- Publicación de juegos con subida de archivos (.zip/.rar) y portadas.
- Catálogo y búsqueda.
- Ficha de juego, comentarios y calificaciones.
- Eliminación de videojuegos propios.

## 10. Pruebas y Criterios de Aceptación
- Todas las pruebas de `tests/` deben pasar.
- La navegación debe ser fluida sin duplicación de la barra superior.
- Las imágenes de portada deben previsualizarse al seleccionarlas en el formulario de publicación.
- La obtención de calificaciones en el catálogo debe ser paralela y no bloquear la carga principal.
- No debe haber errores en la consola del navegador.
