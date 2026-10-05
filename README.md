# Wiki IA Grecia

Base de conocimiento de uso interno construida a partir de las entrevistas del Desayuno Empresarial Grecia, su análisis y una presentación de resultados. Sigue el patrón LLM Wiki de fuentes preservadas, páginas conectadas y reglas para mantenimiento por un agente.

[Abrir el índice de la wiki](index.md) · [Mapa de capacidades y necesidades](wiki/sintesis/capacidades-y-necesidades.md) · [Pilotos posibles](wiki/oportunidades/pilotos.md)

## Cómo comenzar

1. Abra `index.md` para navegar por entrevistas, temas, conceptos, casos, síntesis y consultas.
2. Abra la carpeta completa como bóveda en Obsidian, o use un editor Markdown. Los enlaces son relativos y funcionan dentro de la carpeta extraída.
3. Para trabajar con un agente, abra esta carpeta en Codex y pídale que lea `AGENTS.md` e `index.md` antes de consultar o añadir información.

Ejemplo de consulta al agente

> Lee AGENTS.md e index.md. ¿Qué oportunidades de integración aparecen en estas entrevistas? Distingue prácticas relatadas, necesidades y propuestas. Incluye referencias a los mensajes y señala lo que falta comprobar.

## Contenido del primer corte

| Componente | Cantidad |
| --- | --- |
| Fichas de entrevistas utilizables | 86 |
| Transcripciones del CSV | 86 |
| Textos históricos de participantes utilizables | 85 |
| Temas | 23 |
| Conceptos | 52 |
| Casos seleccionados | 10 |
| Síntesis y mapa de capacidades | 11 |
| Propuestas de pilotos | 5 |
| Consultas con respuesta de referencia | 6 |

El CSV contiene 87 registros. Se excluyó un registro de prueba sin respuestas. El análisis conserva su corte de 86 registros, que incluía esa prueba. La conciliación documenta una entrevista adicional, 16 cambios de estado y 22 diferencias de texto. No se mezclaron denominadores ni se recalcularon porcentajes sobre fuentes incompatibles.

## Buscar y comprobar la wiki

Requiere Python 3.10 o posterior y solo usa la biblioteca estándar.

```bash
python tools/wiki.py search "integración inventarios"
python tools/wiki.py search "criterio humano" --limit 8
python tools/wiki.py status
python tools/wiki.py validate
```

La búsqueda devuelve páginas y extractos con rutas; no genera respuestas con un modelo. Las respuestas interpretativas las produce el agente leyendo las páginas y sus fuentes. Esta entrega no incluye un chatbot alojado ni tareas automáticas programadas.

## Incorporar otra exportación

```bash
python tools/wiki.py stage /ruta/nuevas-entrevistas.csv
```

El comando valida el formato y crea un paquete de ingreso en `.staging/`, con hash, mensajes y comparación por ID. No modifica las fuentes ni la wiki. Después solicite al agente que procese el paquete según `AGENTS.md`, revise el resultado y conserve un nuevo corte. La deduplicación usa el ID original completo; no asigna IDs nuevos silenciosamente.

## GitHub y fuentes

Esta wiki se mantiene en el repositorio privado Universidad-Cenfotec/Wiki-IA-Grecia. `raw/restringido/` contiene los originales, nombres y correos en la copia privada completa y está excluida de Git por `.gitignore`. La capa de consulta también contiene empresas, cargos y detalles de los relatos; es de uso interno y no completamente anónima.

El paquete completo entregado conserva las fuentes restringidas para permitir reproducir y revisar el trabajo. Esos originales y el ZIP no se incorporan al repositorio. Para usar `stage`, restaure localmente `raw/restringido/entrevistas-original.csv` desde ese paquete; seguirá excluido de Git. La validación de una copia clonada señala como advertencia los originales que no estén disponibles y verifica las páginas, referencias y datos incluidos.

Drive conserva los documentos originales enlazados en el inventario de fuentes. La wiki usa snapshots textuales con huellas de contenido. No se alteraron las fuentes de Drive.

## Estado de revisión

La trazabilidad textual y los enlaces se comprueban mediante herramientas. La codificación semántica histórica y las nuevas síntesis están pendientes de revisión humana. Los resultados declarados no fueron verificados con software, datos operativos o mediciones externas.

Consulte `wiki/metodologia/criterios.md`, `wiki/metodologia/conciliacion.md` y `AGENTS.md`.
