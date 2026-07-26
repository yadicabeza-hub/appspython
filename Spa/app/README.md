# Oasis Spa - Website

Este es el repositorio del sitio web de **Oasis Spa**, un centro de relajación y bienestar. El proyecto ha sido desarrollado siguiendo las especificaciones de diseño y requisitos técnicos estipulados.

## Características Principales

*   **Diseño Premium y Minimalista:** Estética relajante, paleta de colores basada en verdes suaves, beiges, tonos madera y azul claro.
*   **Responsive Design:** Optimizado para pantallas desde 320px hasta 1440px (Mobile First).
*   **Secciones Completas:** Hero, Servicios, Beneficios, Nosotros, Galería, Testimonios, Paquetes, Reservas y Contacto.
*   **Tecnologías Vanilla:** Desarrollado sin frameworks de terceros, garantizando un rendimiento óptimo.

## Tecnologías Utilizadas

*   **HTML5 Semántico:** Uso de etiquetas correctas (`header`, `nav`, `main`, `section`, `article`, `footer`) para SEO y accesibilidad.
*   **CSS3 Vanilla:** Uso extensivo de variables CSS, Flexbox, Grid Layout, animaciones suaves y transiciones.
*   **JavaScript Vanilla:** 
    *   Menú hamburguesa responsivo.
    *   Header dinámico al hacer scroll.
    *   Scroll suave entre secciones.
    *   Animaciones al revelar contenido (`IntersectionObserver`).
    *   Validación de formulario en el lado del cliente (sin recargar la página).
    *   Botón de "Volver arriba".

## Estructura de Archivos

```
app/
├── index.html       # Estructura principal y contenido
├── css/
│   └── styles.css   # Estilos globales y diseño responsivo
├── js/
│   └── script.js    # Lógica interactiva
└── README.md        # Documentación
```

## Instrucciones para Ejecutar

Para visualizar el sitio web, no necesitas configurar ningún servidor complejo (a menos que desees simular un entorno de producción). 

Simplemente abre el archivo `index.html` en cualquier navegador web moderno (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge).

```bash
# Ejemplo abriendo desde la terminal de Windows:
start index.html
```

## Decisiones de Diseño

*   **Glassmorphism:** Se utilizó un efecto sutil de desenfoque (`backdrop-filter: blur`) en el header al hacer scroll para mantenerlo siempre visible sin obstruir el contenido subyacente.
*   **Tipografía:** Se eligieron fuentes modernas de Google Fonts: *Playfair Display* para encabezados (aporta elegancia) y *Outfit* para cuerpo de texto (limpieza y legibilidad).
*   **Interacciones:** Las micro-animaciones (hover effects en botones, tarjetas levantándose al hacer hover) se implementaron para dar vida al sitio web, reforzando la sensación premium.

## SEO y Accesibilidad

Se incluyeron meta-etiquetas para Open Graph y Twitter Cards, descripciones ALT en todas las imágenes y un correcto contraste de colores. El formulario es accesible por teclado (`focus-visible`).
