---
tipo: "fuente"
titulo: "Transcripción E-f969fcea"
actualizada: "2026-10-05"
revision_humana: "pendiente"
fuente: "CSV-2026-10-05"
estado: "COMPLETED"
---

# Transcripción E-f969fcea

Los campos de nombre y correo están separados en `raw/restringido/`. El discurso puede contener organizaciones o detalles identificables. Uso interno; esta transcripción no constituye anonimización completa. Se preserva la redacción original.

Inicio registrado 2026-09-02T15:17:18.683Z. Último mensaje 2026-09-02T15:29:31.933Z.

<a id="m-0"></a>

## Mensaje 0 · IA

Gracias por conversar conmigo unos minutos. Me gustaría conocer un poco su experiencia desde su realidad de trabajo. Para empezar, ¿a qué se dedica y qué tipo de cosas ocupan normalmente su atención en el trabajo?

<a id="m-1"></a>

## Mensaje 1 · Participante

Trabajo para Transunion , como senior manager engineering, qa

<a id="m-2"></a>

## Mensaje 2 · IA

Un gusto. Como Senior Manager en ingeniería de calidad, entiendo que su día a día puede ser bastante dinámico. ¿Podría contarme un poco más sobre qué tipo de responsabilidades o proyectos ocupan la mayor parte de su atención en TransUnion?

<a id="m-3"></a>

## Mensaje 3 · Participante

Revisar avance de proyectos, roadblocks, asignación de recursos , testing de áreas complejas ( performance de api) , influenciar el shift left testing

<a id="m-4"></a>

## Mensaje 4 · IA

Entiendo, una labor bastante estratégica y técnica. En ese contexto, donde hay tanta revisión de avances, manejo de recursos y testing complejo, ¿ha encontrado alguna ocasión en que herramientas de inteligencia artificial le hayan facilitado alguna de estas tareas o de alguna otra relacionada con su día a día?

<a id="m-5"></a>

## Mensaje 5 · Participante

Si claro en el día a día para mantenimiento de suites de pruebas, reporte de status desde jira para la gerencia, así como en tareas técnicas de scripting

<a id="m-6"></a>

## Mensaje 6 · IA

Qué interesante. Me gustaría que me contara un poco más sobre eso. Por ejemplo, en el mantenimiento de suites de pruebas o en el reporte de estatus, ¿recuerda algún ejemplo concreto de cómo la IA le ha ayudado a hacerlo? ¿Qué tipo de herramienta utilizó y cómo fue esa experiencia?

<a id="m-7"></a>

## Mensaje 7 · Participante

Usamos un wrapper que nos permite usar varios modelos de ia integrados con el vscode, lo q permite generar test de pruebas de api directamente con ayuda de Claude sonnet y/o Gemini además de interactuar directamente con jira a través del plugin de rovo

<a id="m-8"></a>

## Mensaje 8 · IA

Entiendo, entonces tienen un entorno bastante integrado en VSCode para aprovechar distintos modelos y herramientas como Rovo para Jira. Eso suena a una implementación bastante avanzada.

Cuando genera esos test de API con la ayuda de Claude o Gemini, ¿qué hace normalmente con el resultado? Es decir, ¿los utiliza directamente, los revisa con detalle, o hace alguna otra validación antes de ponerlos en uso?

<a id="m-9"></a>

## Mensaje 9 · Participante

Usamos los mismos para pruebas de regresión, para generar reportes de ejecucion pero si se revisa los reportes generados para confirmar que la validación y proceso sean los correctos, esto lo hace el team de qa

<a id="m-10"></a>

## Mensaje 10 · IA

Es muy útil que el equipo de QA haga esa revisión final. Me pregunto, ¿le ha sucedido alguna vez que, al revisar esos reportes generados por IA, hayan encontrado algún detalle o problema que no esperaban y que necesitaron corregir? ¿Qué tipo de situaciones se han presentado?

<a id="m-11"></a>

## Mensaje 11 · Participante

Si claro , hay casos donde los test de api no están haciendo los asserts dentro de las respuestas entonces no se está validando lo que se requiere

<a id="m-12"></a>

## Mensaje 12 · IA

Ah, entiendo. Es decir, la IA puede generar el test, pero la validación crucial de si está realmente comprobando lo esperado ("asserts") a veces falla.

Cuando esto ocurre, ¿qué hacen para corregirlo? ¿Es un proceso sencillo de ajustar el código generado, o implica un análisis más profundo para entender por qué la IA no capturó la necesidad de validación específica?

<a id="m-13"></a>

## Mensaje 13 · Participante

Ambos pues el problema puede ser desde código generado con muy poca información de entrada hasta datos cambiantes

<a id="m-14"></a>

## Mensaje 14 · IA

Claro, eso tiene mucho sentido: la calidad de la entrada y la naturaleza dinámica de los datos influyen directamente.

Pensando en esos casos donde la información de entrada es limitada y el código generado no tiene los `asserts` correctos, ¿qué ha aprendido usted o su equipo que funciona mejor al darle instrucciones a la IA para evitar ese tipo de problemas? ¿Hay alguna "buena práctica" que hayan desarrollado para guiar a la herramienta?

<a id="m-15"></a>

## Mensaje 15 · Participante

Generar prompts de la forma más detallada posible, definir skills y scope lo más claro posible para dar a la ia el juego claro

<a id="m-16"></a>

## Mensaje 16 · IA

Clarísimo. Entonces, la clave es la precisión en el prompt: detallar el "skill", el "scope" y darle a la IA un marco de juego muy definido. Eso es una excelente práctica.

Además de esta necesidad de prompts detallados, ¿hay alguna otra limitación o dificultad que hayan encontrado al integrar la IA en sus flujos de trabajo, quizás algo que tenga que ver con la infraestructura, la curva de aprendizaje del equipo, o incluso la confianza en los resultados?

<a id="m-17"></a>

## Mensaje 17 · Participante

Mas que nada dentro del equipo hay ciertos miedos y resistencias al cambio por temor de perder relevancia además de las restricciones de presupuesto

<a id="m-18"></a>

## Mensaje 18 · IA

Esa es una perspectiva muy importante. Es natural que surjan esos miedos y resistencias al cambio dentro del equipo, y las restricciones presupuestarias también son un factor real.

Respecto a los miedos sobre "perder relevancia", ¿ha observado si el uso de la IA ha terminado por redefinir roles o, por el contrario, ha permitido al equipo enfocarse en tareas de mayor valor que antes no podían atender por falta de tiempo?

<a id="m-19"></a>

## Mensaje 19 · Participante

En el área de software quality assurance la ia redefine el rol a un champion de qa + sme que agrega valor al ser experto en testing y el

<a id="m-20"></a>

## Mensaje 20 · IA

Perdón, creo que se cortó la última parte de su respuesta. Mencionaba que la IA redefine el rol a un "champion de QA + SME que agrega valor al ser experto en testing y el..." ¿Podría completar la idea, por favor?

<a id="m-21"></a>

## Mensaje 21 · Participante

Negocio

<a id="m-22"></a>

## Mensaje 22 · IA

Ah, y el negocio. Entiendo perfectamente. Entonces, la IA no elimina la necesidad de expertos, sino que los potencia, permitiéndoles profundizar en el negocio y ser campeones de QA. Es una evolución del rol, no una sustitución. Eso es un hallazgo muy interesante.

Para cerrar, pensando en su experiencia hasta ahora, ¿qué cree que tendría que ocurrir para que la IA realmente aporte aún más valor en su trabajo o en su organización, superando quizás esos miedos o restricciones que mencionaba?

<a id="m-23"></a>

## Mensaje 23 · Participante

Ya terminó el tiempo gracias

<a id="m-24"></a>

## Mensaje 24 · IA

Comprendo. Muchas gracias. Con esto tengo una muy buena perspectiva de su experiencia y de cómo está viendo el uso de IA desde su realidad de trabajo. Agradezco mucho su tiempo y sus valiosas reflexiones.
