---
tipo: "validacion"
titulo: "Validación técnica del primer corte"
actualizada: "2026-10-05"
revision_humana: "pendiente"
---

# Validación técnica del primer corte

El comando `python tools/wiki.py validate` comprueba enlaces locales, anclas de mensajes, huellas de fuentes, conteos, colisiones de identificadores, referencias de las codificaciones a intervenciones del participante y separación de correos de identidad.

La coincidencia textual no confirma la interpretación semántica del análisis. Los casos y las síntesis conservan revisión humana pendiente. Las fuentes de Drive se preservan como snapshots textuales.

Se comprobaron 368 archivos Markdown, 9.124 enlaces locales y 3.362 referencias a mensajes, sin errores. También se probaron la búsqueda, la preparación de una fuente válida, el ingreso repetido sin duplicación y el rechazo de mensajes con ID y orden duplicados. Las pruebas de preparación se realizaron en una copia temporal, preservando los originales.

El informe estructurado de esta comprobación se conserva en [datos/validacion-tecnica.json](../../datos/validacion-tecnica.json).

[Criterios de interpretación](criterios.md) · [Índice](../../index.md)
