# Bitácora de Wiki IA Grecia

## [2026-10-05] ingest | Corte inicial de entrevistas y análisis

Fuentes consultadas CSV exportado el 5 de octubre, análisis de Drive del 2 de septiembre y presentación de resultados. Los mensajes del CSV están fechados el 2 de septiembre. Referencia de arquitectura LLM Wiki de Karpathy.

## [2026-10-05] reconcile | Versiones y cobertura

87 registros CSV, 86 utilizables tras excluir una prueba. El análisis incluye 86 registros con la prueba. Una entrevista adicional en CSV, 16 cambios de estado y 22 diferencias de texto. Un caso tiene más contenido en la fuente analítica que en el CSV. Se mantienen fuentes separadas.

## [2026-10-05] compile | Primera wiki conectada

86 fichas y transcripciones, 85 textos históricos, 23 temas, 52 conceptos, 10 casos, 11 síntesis, 5 propuestas de pilotos y 6 consultas de referencia. Codificaciones históricas conservadas como automáticas, pendientes de revisión humana. Cuatro lecturas añadidas para la entrevista nueva sin modificar coberturas históricas.

## [2026-10-05] query | Consultas iniciales

Se conservaron seis respuestas de referencia sobre tareas, soluciones propias, capacitación, pilotos, verificación y datos faltantes. Cada respuesta remite a síntesis y casos con mensajes de respaldo.

## [2026-10-05] validation | Comprobación técnica

Verificación de enlaces, anclas, conteos y huellas mediante tools/wiki.py validate. El informe se conserva en wiki/metodologia/validacion-tecnica.md. La clasificación humana y la verificación externa de resultados siguen pendientes.

## [2026-10-05] publish | Repositorio privado Wiki-IA-Grecia

Destino indicado por el usuario Universidad-Cenfotec/Wiki-IA-Grecia. Se incorpora la capa de consulta, las fuentes textuales seudonimizadas, las reglas y las herramientas. Se excluyen raw/restringido/, los originales con campos de nombre y correo, el ZIP y archivos temporales. El historial conserva el commit inicial del repositorio.
