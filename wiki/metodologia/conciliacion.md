---
tipo: "metodologia"
titulo: "Conciliación entre CSV y análisis"
actualizada: "2026-10-05"
revision_humana: "pendiente"
---

# Conciliación entre CSV y análisis

## Cortes de referencia

| Indicador | CSV suministrado | Análisis histórico de Drive |
| --- | --- | --- |
| Registros de entrevista | 87 | 86 |
| Completadas | 73 | 56 |
| En progreso | 14 | 30 |
| Registro de prueba sin respuestas | 1 | 1 |
| Entrevistas utilizables después de excluir prueba | 86 | 85 |

Los mensajes del CSV están fechados el 2 de septiembre de 2026, aunque el nombre del archivo indica exportación del 5 de octubre. No interpretar esa fecha de nombre como fecha de entrevista. El análisis de Drive se titula con fecha 2 de septiembre y su presentación posterior conserva las métricas históricas.

## Comparación por identificador

- Los 86 identificadores del análisis aparecen en el CSV.
- E-c86d526a está solo en el CSV y cuenta con 11 respuestas del participante.
- 16 registros pasan de IN_PROGRESS en el análisis a COMPLETED en el CSV.
- 64 textos agregados son idénticos, incluido el registro de prueba vacío.
- 22 textos agregados difieren. La diferencia por sí sola no demuestra que una fuente sea cronológicamente posterior.

El caso [E-ec73ac2a](../entrevistas/E-ec73ac2a.md) conserva una sola respuesta del participante en el CSV y un texto más extenso en el análisis. Se mantiene como conflicto de versiones pendiente de aclaración. No se completó el CSV con mensajes inventados.

## Trazabilidad del análisis

Se comprobaron coincidencias literales normalizando mayúsculas, espacios y Unicode, sin reemplazar el original.

| Conjunto | Total | Con coincidencia en mensajes del CSV | Solo análisis |
| --- | --- | --- | --- |
| Codificaciones | 2301 | 2281 | 20 |
| PNI | 389 | 385 | 4 |
| Inferencias | 326 | 322 | 4 |
| Fragmentos de evidencia | 625 | 613 | 12 |

Todas las coincidencias ausentes se concentran en la entrevista de cambio organizacional señalada arriba. Las tablas PNI exportadas contienen bloques agregados después de sus 389 filas; esos bloques no se cuentan como valoraciones individuales.

## Política de uso

El CSV determina el estado y la conversación del corte actual. El análisis se conserva como versión interpretativa histórica. Sus coberturas, redes, índice de riqueza y PNI mantienen su denominador original de 86, incluido el registro de prueba. No se recalcularon coberturas con una mezcla de cortes. La nueva entrevista tiene lectura separada y no altera esas métricas.

## Detalle de los registros que difieren

| Entrevista | Estado CSV | Estado análisis | Caracteres CSV | Caracteres análisis |
| --- | --- | --- | --- | --- |
| [E-69c5925d](../entrevistas/E-69c5925d.md) | COMPLETED | IN_PROGRESS | 1517 | 1509 |
| [E-02ba0750](../entrevistas/E-02ba0750.md) | IN_PROGRESS | IN_PROGRESS | 1034 | 976 |
| [E-694ca20b](../entrevistas/E-694ca20b.md) | COMPLETED | IN_PROGRESS | 1616 | 1563 |
| [E-731d2e8a](../entrevistas/E-731d2e8a.md) | COMPLETED | IN_PROGRESS | 1112 | 954 |
| [E-b764e6c6](../entrevistas/E-b764e6c6.md) | COMPLETED | IN_PROGRESS | 2685 | 2657 |
| [E-5028ca87](../entrevistas/E-5028ca87.md) | COMPLETED | IN_PROGRESS | 2085 | 2071 |
| [E-948192ff](../entrevistas/E-948192ff.md) | IN_PROGRESS | IN_PROGRESS | 1606 | 1494 |
| [E-e248a5ec](../entrevistas/E-e248a5ec.md) | COMPLETED | IN_PROGRESS | 717 | 710 |
| [E-aba5882b](../entrevistas/E-aba5882b.md) | COMPLETED | IN_PROGRESS | 1932 | 1848 |
| [E-31613cc2](../entrevistas/E-31613cc2.md) | COMPLETED | IN_PROGRESS | 1911 | 1840 |
| [E-192e68e4](../entrevistas/E-192e68e4.md) | IN_PROGRESS | IN_PROGRESS | 1307 | 1117 |
| [E-97cc7b1b](../entrevistas/E-97cc7b1b.md) | COMPLETED | IN_PROGRESS | 1005 | 789 |
| [E-ec73ac2a](../entrevistas/E-ec73ac2a.md) | COMPLETED | COMPLETED | 55 | 1084 |
| [E-e437182e](../entrevistas/E-e437182e.md) | COMPLETED | IN_PROGRESS | 1310 | 1171 |
| [E-e260ff24](../entrevistas/E-e260ff24.md) | IN_PROGRESS | IN_PROGRESS | 1139 | 966 |
| [E-a5cc257a](../entrevistas/E-a5cc257a.md) | COMPLETED | IN_PROGRESS | 1094 | 922 |
| [E-1d40770c](../entrevistas/E-1d40770c.md) | IN_PROGRESS | IN_PROGRESS | 2228 | 1510 |
| [E-2d8836a2](../entrevistas/E-2d8836a2.md) | IN_PROGRESS | IN_PROGRESS | 773 | 218 |
| [E-1e98e539](../entrevistas/E-1e98e539.md) | COMPLETED | IN_PROGRESS | 833 | 745 |
| [E-8ac274b8](../entrevistas/E-8ac274b8.md) | COMPLETED | IN_PROGRESS | 889 | 280 |
| [E-c141b1af](../entrevistas/E-c141b1af.md) | IN_PROGRESS | IN_PROGRESS | 537 | 286 |
| [E-9f26834c](../entrevistas/E-9f26834c.md) | IN_PROGRESS | IN_PROGRESS | 633 | 453 |
| [E-c86d526a](../entrevistas/E-c86d526a.md) | COMPLETED | No incluido | 1340 | — |

[Detalle estructurado](../../datos/conciliacion.json) · [Índice](../../index.md)
