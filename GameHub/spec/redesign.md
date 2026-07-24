# Spec: Rediseño Visual de GameHub (Google Play Store Style)

## 1. Objetivo del Rediseño
Transformar la apariencia de la plataforma GameHub para ofrecer una experiencia de usuario moderna, limpia e inspirada en la Google Play Store, preservando la identidad de GameHub y todas las funcionalidades del backend existentes.

## 2. Alcance Funcional
**Funcionalidades que deben conservarse intactas:**
- Autenticación: Registro, Login y Logout.
- Gestión de Perfiles: Visualización y edición (recientemente implementada).
- Videojuegos: Publicación (datos + archivos `.zip`/`.rar` y portadas), listado, detalle y descargas.
- Reseñas: Calificación de 1 a 5 estrellas, unicidad por usuario/juego.
- Búsqueda y Filtros.

**Nuevas Funcionalidades Frontend:**
- Búsqueda avanzada con retención de términos.
- Filtros interactivos por género, plataforma y estado.
- Interfaz gráfica para manejo de estados de carga (Loading), vacío (No data) y error.
- Sistema de previsualización de imágenes antes de subir.

## 3. Alcance Visual
- **Colores:** Principal `#01875F` (GameHub Green), Secundario `#1A73E8` (Play Blue), Fondo `#F8F9FA`, Tarjetas `#FFFFFF`, Textos `#202124` y `#5F6368`. Bordes `#DADCE0`.
- **Estructura:** Navbar superior fija con buscador integrado, carrusel de destacados, sistema de chips para categorías, grilla de tarjetas responsive.
- **Tarjetas:** Imagen de portada proporcional 16:9 o ancha, título truncado a 1 línea, puntuación destacada con estrella amarilla, precio o botón de acción rápido.
- **Página de Detalle:** Hero section estilo Play Store con icono grande, título gigante, creador, tags de calificación/descargas, botón verde llamativo para descargar.

## 4. Archivos a Modificar
**CSS:**
- `static/css/estilos.css` (Reescritura completa manteniendo el nombre)

**HTML (Plantillas Jinja2):**
- `templates/index.html` (Rediseño de home con hero y categorías)
- `templates/videojuegos.html` (Filtros interactivos y grilla moderna)
- `templates/detalle_juego.html` (Ficha técnica estilo Play Store)
- `templates/publicar_juego.html` (Formulario en columnas con drag&drop y preview)
- `templates/perfil.html` (Perfil del desarrollador/jugador y sus juegos)
- `templates/registro.html` & `templates/login.html` (Formularios centrados, limpios, con elevación)
- `templates/mis_juegos.html` (Dashboard personal)

**JavaScript:**
- `static/js/videojuegos.js` (Lógica de vista previa y estados de carga)
- `static/js/api.js` (Manejo de errores mejorado y loaders globales si aplica)
- `static/js/resenas.js` (Estrellas interactivas en reseñas)

## 5. Criterios de Aceptación
1. El diseño debe ser 100% responsive (Mobile, Tablet, Desktop).
2. Los colores, sombras y radios de borde deben coincidir con las variables definidas en la Skill.
3. Todas las llamadas a la API REST deben funcionar sin modificaciones en los Routers (FastAPI).
4. El formulario de publicación debe mostrar un preview de la portada seleccionada.
5. El sistema de reseñas debe integrarse fluidamente debajo de los detalles del juego.
6. Accesibilidad cumplida: contraste validado, etiquetas semánticas y navegación manejable.
