# OVA "Caminantes del Galeras: Interculturalidad y Convivencia"

Objeto Virtual de Aprendizaje (OVA) para el grado 4-2 del Liceo De La Merced Maridíaz (Pasto, Nariño).
Hace parte del trabajo de grado de la Maestría en Educación (Corporación Universitaria Iberoamericana),
autores: Juan Carlos Cuarán Muñoz y Johan Sebastián Bolaños Noguera. Línea: Interculturalidad.
Categorías del proyecto: interculturalidad, respeto por la diversidad, convivencia y OVA.
Público: niños de ~9-10 años. Todo el texto de la interfaz va en español, sencillo y amable.

## Estructura
- `src/index.template.html` — TODO el código (HTML + CSS + JS en un solo archivo). Editar aquí.
  Contiene el marcador `/*__ASSETS__*/` donde se inyectan los medios.
- `media/` — imágenes (.jpg) y videos (.mp4 H.264, comprimidos) sacados de la presentación
  "San_Juan_de_Pasto.pptx" de los autores. Cada archivo se expone en JS como `IMG.<nombre>` o `VID.<nombre>`.
  Videos: `pasto` (iglesias de Pasto), `carnaval` (Pasto aéreo + carnaval), `guanena` (La Guaneña).
- `build.py` — genera `caminantes-del-galeras.html` (autocontenido, ~7 MB). Ejecutar: `python build.py`.
- `caminantes-del-galeras.html` — resultado final. No editar a mano.

## Flujo de pantallas (S.step)
1. `avatar` — crear avatar (niño/niña, piel, ojos, cabello, 7 peinados, camiseta, nombre).
2. `companion` — elegir compañero: Inti Jojoa (quillacinga), Yeison Quiñones (afro del Pacífico),
   Valentina Burbano (mestiza de Pasto), Samuel Guerrero (Liceo Maridíaz).
3. `quiz` — diagnóstico "Descubriendo Juntos" (10 ítems Sí / A veces / No).
4. `learn` — 4 tarjetas volteables con las categorías.
5. `map` — mapa SVG con 5 estaciones progresivas.
6. `zone:cocha` (sopa de letras dialecto nariñense), `zone:lajas` (crucigrama de valores),
   `zone:pasto` (video, emparejar platos típicos, barniz de Pasto), `zone:carnaval` (rompecabezas de carroza),
   `zone:galeras` (video narrado + La Guaneña).
7. `pact` — Gran Pacto del Galeras (valores + compromiso).
8. `cert` — certificado SVG con el avatar; descarga PNG vía capacidad `downloads` e impresión; panel docente.

## Detalles técnicos
- Estado en el objeto global `S`, guardado en localStorage (clave `caminantes-galeras-v1`).
- Avatares generados con `avatarInner()` / `avatarSVG()` (SVG puro, sin imágenes externas).
- Mini-videos narrados con `miniVideo()` (ilustración SVG + subtítulos + speechSynthesis en español).
- Puntos con `award(clave, puntos, mensaje)`; cada clave se otorga una sola vez.
- Contenido de cada estación en el objeto `ZONES` (textos, preguntas `mcqBlock`, requisitos `req`).
- Se publica como artifact de claude.ai: sin peticiones de red; solo se permiten scripts de cdnjs/jsdelivr
  y fuentes de Google Fonts. Medios siempre incrustados. Límite de 16 MB para el archivo final.
- Estilo: paleta inspirada en el barniz de Pasto (rojo #D7263D, oro #F4B400, turquesa #0E8C98,
  verde #2E8B57, tinta #1B2A41); fuentes Baloo 2 (títulos) y Nunito (texto); soporta modo oscuro.

## Pendientes / ideas
- Guardar las respuestas del diagnóstico y los compromisos de todo el grupo en un solo lugar
  para el análisis de resultados (capítulo 4 del trabajo de grado).
- Posible cuestionario de salida (pos-test) para comparar con el diagnóstico.
