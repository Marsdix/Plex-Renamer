# Plex Renamer — Redesign UI

## Decisiones de diseño

### Estilo global
- Glassmorphism dark
- Fondo: gradiente `#0d1117 → #12091a → #1a1f2e` en todas las páginas
- Blobs ambient: 2 esferas difusas rose/fucsia por página, `filter: blur(40px)`
- Acento: gradiente `#f43f5e → #ec4899 → #d946ef`
- Glass cards: `background: rgba(255,255,255,0.06)`, `border: 1px solid rgba(255,255,255,0.1)`, `backdrop-filter: blur(12px)`
- Tipografía: Fredoka One (títulos) + Baloo 2 (body) — sin cambios
- CSS: consolidar en `styles_global.css` + overrides mínimos por página

### Header (todas las páginas)
- Fondo `rgba(255,255,255,0.04)` con `backdrop-filter: blur`
- `border-bottom: 1px solid rgba(244,63,94,0.35)`
- Botón Inicio/Salir: glass pill con borde rose

### Index — lista 2 columnas
- Grid 2×3 (6 filas), cada tile: glass card horizontal con icono FA + label + subtítulo
- Hover: border rose + glow sutil

### Páginas de formulario
Afecta: crear_peliculas, crear_series, crear_documentales, agregar_extras, renombrar_series

- Izquierda ~55%: glass card con form. Inputs: border rose en focus. Submit: gradiente rose→fuchsia
- Derecha ~45%: imagen de poster (placeholder por sección). Preparado para swap TMDB futuro
- Alerts: glass verde/rojo en lugar de Bootstrap default

### Footer
- Fondo `rgba(255,255,255,0.03)`, border-top rose, texto `rgba(255,255,255,0.35)`

## Pendiente (fase 2)
- Integración TMDB API para posters aleatorios en páginas de formulario
- Usuario necesita crear API key en themoviedb.org
