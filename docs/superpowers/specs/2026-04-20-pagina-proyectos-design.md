# Pagina de Proyectos - RL Metafusion

## Objetivo

Crear una pagina dedicada en `/proyectos/` que muestre los proyectos realizados por RL Metafusion con galeria de fotos y descripcion detallada.

## Arquitectura

### Templates

- **`templates/base.html`** - Template base con header, footer, Tailwind config, meta tags y scripts compartidos
- **`templates/index.html`** - Refactorizar para heredar de `base.html`
- **`templates/proyectos.html`** - Nueva pagina de proyectos, hereda de `base.html`

### URL

- `path('proyectos/', TemplateView.as_view(template_name='proyectos.html'), name='proyectos')`

### Datos

- HTML estatico, sin modelos Django ni base de datos
- Solo el proyecto "Almacen Logistico Requena" con las 6 imagenes existentes

## Layout de la pagina `/proyectos/`

1. **Header** - Heredado de `base.html`
2. **Banner** - Titulo "Nuestros Proyectos", subtitulo, fondo gris claro, padding top para compensar header fijo
3. **Proyecto destacado** - Seccion con:
   - Titulo: "Almacen Logistico - Requena"
   - Tipo de servicio: "Estructura metalica / Montaje industrial"
   - Ubicacion: "Requena, Peru"
   - Descripcion del trabajo realizado
   - Galeria de 6 fotos en grid responsivo (1 col mobile, 2 col tablet, 3 col desktop) con efecto hover zoom
4. **CTA** - "Tienes un proyecto? Contactanos" con boton a WhatsApp o seccion contacto
5. **Footer** - Heredado de `base.html`

## Navegacion

- Actualizar link "Proyectos" en nav del header para apuntar a `/proyectos/` en lugar de `#proyectos`
- Mantener link `#proyectos` en la landing para la seccion existente como preview
- En la seccion de proyectos de la landing, agregar boton "Ver todos los proyectos" que lleve a `/proyectos/`

## Estilo visual

- Mismos colores: `primary: #2D2D2D`, `accent: #F5A900`
- Misma tipografia y espaciado de la landing
- Galeria con efecto hover (zoom + overlay con info)
- Responsive: mobile-first
