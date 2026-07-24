# Skill: Sistema de Diseño GameHub Indie Style

## 1. Variables Globales (Tokens de Diseño)
```css
:root {
    --color-primary: #fa5c5c;
    --color-primary-dark: #d94848;
    --color-primary-soft: #fff0f0;

    --color-background: #f4f4f4;
    --color-surface: #ffffff;
    --color-surface-dark: #252525;

    --color-text: #222222;
    --color-text-secondary: #666666;
    --color-text-light: #ffffff;

    --color-border: #dddddd;
    --color-success: #2e8b57;
    --color-warning: #e0a100;
    --color-danger: #c0392b;

    --radius-small: 4px;
    --radius-medium: 8px;
    --radius-large: 12px;

    --shadow-small: 0 1px 3px rgba(0, 0, 0, 0.08);
    --shadow-medium: 0 4px 14px rgba(0, 0, 0, 0.12);

    --font-main: "Inter", "Segoe UI", Arial, sans-serif;
}
```

## 2. Reglas Estilísticas

- **Diseño compacto:** Optimizar el espacio para mostrar la mayor cantidad de contenido sin saturar la vista.
- **Estilo de plataforma indie:** Inspirado en itch.io. Diseño limpio, centrado en el contenido de los creadores.
- **Portadas protagonistas:** Las imágenes de los juegos son el elemento principal de las tarjetas. Deben usar `object-fit: cover`.
- **Tarjetas rectangulares:** Bordes moderadamente redondeados (`--radius-medium`), sombras discretas (`--shadow-small`).
- **Etiquetas pequeñas:** Tags para género y plataforma deben ser compactos, estilo "pill" con colores suaves.
- **Botones llamativos:** El color coral/rojo (`--color-primary`) se reserva para acciones principales (Publicar Juego, Descargar).
- **Evitar bordes excesivos:** No usar formas tipo píldora grandes en botones que no lo ameriten, mantener un radio moderado.
- **Evitar copiar a Google Play:** No usar sombras pesadas ni tarjetas flotantes con grandes márgenes.

## 3. Reglas Técnicas
- **Separación de responsabilidades:** Separar correctamente HTML, CSS y JavaScript.
- **No estilos inline:** Todo el estilo debe estar en `estilos.css` a través de clases, no en el atributo `style` de HTML.
- **Reutilización:** Definir clases de componentes (`.btn`, `.game-card`, `.tag`, `.form-group`) y reusarlas en toda la aplicación.
- **Identificadores intocables:** No modificar los `id` requeridos por la lógica JavaScript (`api.js`, `videojuegos.js`, `resenas.js`, `autenticacion.js`).
