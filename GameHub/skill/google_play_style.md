# Skill: Sistema de Diseño Google Play Store Style

## 1. Variables Globales (Tokens de Diseño)
```css
:root {
  --color-primary: #01875F; /* GameHub Green */
  --color-secondary: #1A73E8; /* Play Blue */
  --color-background: #F8F9FA;
  --color-surface: #FFFFFF;
  --color-text-primary: #202124;
  --color-text-secondary: #5F6368;
  --color-border: #DADCE0;
  --color-warning: #F4B400; /* Para estrellas */
  --color-danger: #D93025;
  
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  
  --shadow-sm: 0 1px 2px 0 rgba(60,64,67,0.3), 0 1px 3px 1px rgba(60,64,67,0.15);
  --shadow-md: 0 1px 3px 0 rgba(60,64,67,0.3), 0 4px 8px 3px rgba(60,64,67,0.15);
  --shadow-hover: 0 2px 6px 2px rgba(60,64,67,0.15), 0 1px 2px 0 rgba(60,64,67,0.3);
  
  --font-family: 'Roboto', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
```

## 2. Tipografía
- Títulos: Fuente sin remates, pesos `500` y `700`, color `--color-text-primary`.
- Cuerpos de texto: Peso `400`, tamaño base `14px` o `16px`, color `--color-text-secondary`.

## 3. Botones (Chips y CTAs)
- **Primary:** Fondo `--color-primary`, texto blanco, border-radius `--radius-md` o `--radius-xl` (para el CTA principal estilo descargar).
- **Secondary / Chips:** Fondo `transparent`, borde `--color-border`, texto `--color-text-secondary`. En hover o activo, fondo tintado o borde azul.
- Sin subrayados. Transiciones de `0.2s ease` en `background-color` y `box-shadow`.

## 4. Tarjetas (Cards)
- Fondo `--color-surface`, borde suave o inexistente (`--shadow-sm`), radius `--radius-md`.
- Layout: Portada superior (aspect ratio 16:9, `object-fit: cover`), contenido inferior con padding `12px` o `16px`.
- Interacción: `cursor: pointer`, cambio a `--shadow-hover` al pasar el mouse.

## 5. Formularios y Entradas
- Inputs: Borde sólido `--color-border`, radius `--radius-sm`, padding interno amplio, color de texto `--color-text-primary`.
- En estado `focus`, borde azul `--color-secondary` y outline transparente (estilo Material Design 3 simplificado).

## 6. Reglas de Accesibilidad y Responsive
- Evitar desplazamientos horizontales en mobile configurando `overflow-x: hidden` en el `body`.
- Las cuadrículas deben usar CSS Grid con `repeat(auto-fill, minmax(250px, 1fr))`.
- La navbar en pantallas menores a `768px` debe ocultar los enlaces y mostrar un menú hamburguesa o posicionarlos abajo (en este caso colapsables).
