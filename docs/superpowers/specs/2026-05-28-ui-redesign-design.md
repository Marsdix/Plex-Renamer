# Plex Renamer — Redesign UI

## Decisiones de diseño (refinado con UI/UX Pro Max)

### Tokens del sistema
```css
:root {
  /* Backgrounds — no usar #000000 puro (OLED smear) */
  --bg-deep: #0a0a0f;
  --bg-base: #12091a;
  --bg-elevated: #1a1f2e;

  /* Surface glass */
  --surface: rgba(255, 255, 255, 0.06);
  --surface-hover: rgba(255, 255, 255, 0.09);
  --border: rgba(255, 255, 255, 0.08);

  /* Foreground */
  --fg: #EDEDEF;
  --fg-muted: #8A8F98;

  /* Acento — Rose / Fuchsia */
  --accent-1: #f43f5e;
  --accent-2: #ec4899;
  --accent-3: #d946ef;
  --accent-gradient: linear-gradient(135deg, var(--accent-1), var(--accent-2), var(--accent-3));
  --accent-glow: rgba(244, 63, 94, 0.2);
  --accent-border: rgba(244, 63, 94, 0.35);

  /* Sistema */
  --radius: 16px;
  --radius-sm: 10px;
  --easing: cubic-bezier(0.16, 1, 0.3, 1);
  --transition: 200ms var(--easing);
}
```

### Estilo global
- Glassmorphism dark cinemática (Modern Dark / Cinema)
- Fondo: `linear-gradient(135deg, var(--bg-deep), var(--bg-base), var(--bg-elevated))`
- Blobs ambient: 2-3 esferas difusas rose/fucsia con `filter: blur(40-60px)`, `opacity: 0.08-0.12`
- Glass cards: `background: var(--surface)`, `backdrop-filter: blur(12px)`, `border: 1px solid var(--border)`
- Tipografía: Fredoka One (display) + Baloo 2 (body) — mantener actual
- CSS: consolidar 8 CSS separados en `styles_global.css` + overrides mínimos por página

### Header (todas las páginas)
- Glass: `background: rgba(255,255,255,0.04)` + `backdrop-filter: blur(20px)`
- `border-bottom: 1px solid var(--accent-border)`
- Botón Inicio/Salir: glass pill con borde rose, hover anima

### Index — lista 2 columnas
- Grid 2×3 (6 tiles), cada tile: glass card horizontal con icono FA + label + subtítulo
- Hover: border rose activo + glow sutil + `transform: translateY(-2px)`
- Transición: `var(--transition)`

### Páginas de formulario (5 templates)
Aplicar a: crear_peliculas, crear_series, crear_documentales, agregar_extras, renombrar_series

- **Izquierda ~55%**: glass card con form
  - Inputs: `background: rgba(255,255,255,0.04)`, `border: 1px solid var(--border)`, focus `border-color: var(--accent-2)` + glow
  - Submit: `background: var(--accent-gradient)`, hover `transform: translateY(-1px)`
- **Derecha ~45%**: poster placeholder con glass frame + glow rose. Preparado para swap TMDB
- Alerts: glass tinted (verde `rgba(34,197,94,0.1)` o rojo `rgba(244,63,94,0.1)`)

### Footer
- Glass: `background: rgba(255,255,255,0.03)`, `border-top: 1px solid var(--accent-border)`
- Texto `color: var(--fg-muted)`

## Reglas obligatorias (UI/UX Pro Max checklist)

### Accesibilidad (CRITICAL)
- [ ] Contraste texto 4.5:1 mínimo (verificar todos los pares fg/bg)
- [ ] Focus rings visibles 2-4px (no remover `outline`)
- [ ] `aria-label` en botones icon-only
- [ ] Form labels asociados (`<label for="...">`), no placeholder-only
- [ ] `prefers-reduced-motion`: desactivar blobs ambient + reducir transiciones

### Touch & Interaction
- [ ] `cursor: pointer` en todos los clickables
- [ ] Transiciones hover 150-300ms con `var(--easing)`
- [ ] No relying en hover-only (touch alternative)

### Performance
- [ ] Backdrop-filter: usar con moderación (costoso en mobile)
- [ ] Imágenes posters: lazy load, dimensiones declaradas (evitar CLS)
- [ ] Animaciones: solo `transform` y `opacity`, no `width/height/top/left`

### Iconografía
- [ ] Font Awesome ya integrado — mantener
- [ ] Nunca emoji como icono estructural
- [ ] Tamaños consistentes (16/20/24px)
- [ ] Stroke consistente

### Responsive
- [ ] Breakpoints: 375 / 768 / 1024 / 1440
- [ ] Mobile-first
- [ ] No horizontal scroll
- [ ] Base body 16px (evita auto-zoom iOS)

### Forms
- [ ] Submit: loading state → success/error feedback
- [ ] Validación onBlur (no solo submit)
- [ ] Error inline near campo
- [ ] Required indicators

## Anti-patterns que evitar
- Pure `#000000` (OLED smear) → usar `#0a0a0f` mínimo
- Mixing flat + skeuomorphic styles
- Emoji como icono estructural
- Animar `width/height` (causa reflow)
- Placeholder como label
- Errores solo arriba del form
- Inline hex en componentes (usar tokens)

## Fase 2 pendiente
- Integración TMDB API para posters aleatorios (películas vs series)
- Usuario necesita crear API key gratuita en themoviedb.org primero
