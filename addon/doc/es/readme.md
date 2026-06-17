# mp3DirectCut

* Autor(es) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Presentación

Este complemento mejora la accesibilidad del software mp3DirectCut con NVDA.

Ha sido probado con versiones de mp3DirectCut comprendidas entre la 212 y la 233.

## Atajos de teclado

Este complemento ofrece los siguientes comandos:

* B

    * Se utiliza para confirmar la colocación correcta del marcador del inicio de la selección B.

* Ctrl+Shift+B

    * Se utiliza para indicar la posición del marcador del inicio de la selección B.
    * Una doble pulsación permite obtener la duración de la selección.

* Ctrl+Shift+D

    * Proporciona la duración desde el inicio del archivo hasta la posición actual del cursor de reproducción.
    * Una doble pulsación permite obtener la duración total.

* Ctrl+R

    * Confirma que la selección ha sido cancelada.

* Ctrl+Shift+R

    * Proporciona el tiempo restante desde la posición actual del cursor de reproducción hasta el final del archivo.

* Ctrl+Shift+E

    * Se utiliza para indicar la posición del marcador del final de la selección N.
    * Una doble pulsación proporciona un resumen de las posiciones B y N, y la duración de la selección.

* Ctrl+Shift+P

    * Proporciona la referencia de la parte actual y el número total de partes en el archivo actual.

* Ctrl+Shift+Space

    * Se utiliza para determinar el nivel actual del vúmetro durante la grabación.
    * Una doble pulsación lo restablece.

* Flecha abajo

    * Permite conocer la posición actual del cabezal de reproducción.
    * Este comando también posiciona el cursor en la ubicación del marcador del final de la selección N, indicando la ubicación de este marcador si se ha realizado una selección.
    * En el cuadro de diálogo de volumen, vocaliza el siguiente valor que normalmente puede alcanzarse con Flecha abajo.
    * Este valor no se vocaliza de forma predeterminada.

* Fin

    * Mueve el cursor de reproducción al final del archivo actual y proporciona el tiempo total.

* Inicio

    * Mueve el cursor de reproducción al inicio del archivo actual.

* Flecha izquierda

    * Permite retroceder brevemente un segundo durante la reproducción, indicando la duración actual.
    * Esta duración es configurable en las opciones de mp3directcut.

* N

    * Se utiliza para confirmar la colocación correcta del marcador del final de la selección N.

* Av Pág

    * Permite avanzar 10 segundos durante la reproducción, indicando la duración actual.
    * Esta duración es configurable en las opciones de mp3directcut.

* Re Pág

    * Permite retroceder 10 segundos durante la reproducción, indicando la duración actual.
    * Esta duración es configurable en las opciones de mp3directcut.

* R

    * Permite preparar una grabación e indica que puede pulsar la barra espaciadora para comenzar.

* Flecha derecha

    * Permite avanzar brevemente un segundo durante la reproducción, indicando la duración actual.
    * Esta duración es configurable en las opciones de mp3directcut.

* Ctrl+Flecha derecha

    * Se desplaza al siguiente punto de división, indicando la duración actual.

* Ctrl+Flecha izquierda

    * Se desplaza al punto de división anterior, indicando la duración actual.

* Shift+Flecha derecha

    * Permite avanzar brevemente cuatro centésimas de segundo durante la reproducción, indicando la duración actual.

* Shift+Flecha izquierda

    * Permite retroceder brevemente cuatro centésimas de segundo durante la reproducción, indicando la duración actual.

* S

    * Se utiliza para detener la reproducción e indicar la duración actual.

* Espacio

    * Si la grabación está preparada, inicia dicha grabación.
    * Si hay una grabación en curso, la detiene posicionando el cursor al inicio.
    * Si hay un archivo cargado, inicia la reproducción.
    * Si una reproducción está en curso, permite hacer una pausa indicando la duración actual.
    * Si la reproducción está en pausa, permite reanudarla desde la posición actual.

* Flecha arriba

    * Permite conocer la posición actual del cabezal de reproducción.
    * Este comando también posiciona el cursor en la ubicación del marcador del inicio de la selección B, indicando la ubicación de este marcador si se ha realizado una selección.
    * En el cuadro de diálogo de volumen, vocaliza el valor anterior que normalmente puede alcanzarse con Flecha arriba.
    * Este valor no se vocaliza de forma predeterminada.

* NVDA+H

    * Permite abrir la ayuda del complemento actual.

## Compatibilidad

* Este complemento es compatible con las versiones de NVDA desde la 2019.3 en adelante.

## Cambios para 20240327.0.0

* Corregido un error que provocaba un mensaje de error en el registro al recargar los complementos, gracias a Rob, de la lista de correo nvda-addons;

## Cambios para 20240326.0.0

* Actualizada la compatibilidad para nvda-2024.1.;
* Eliminado el enlace de descarga del readme; el enlace de descarga para futuras actualizaciones estará disponible únicamente desde la tienda de complementos.

## Cambios para 20231229.0.0

* Añadida una implementación retrocompatible para soportar el modo de habla bajo demanda, que pronto estará disponible con nvda-2024.1.

## Cambios para 20231007.0.0

* Después de colocar los puntos de corte y tras abrir la ventana de propiedades de corte con "Ctrl+N", se añadió accesibilidad al título de esta ventana indicando el índice de la parte.
* En modo de lectura, después de mover los marcadores de inicio o fin de selección con las teclas 1 a 6 del teclado numérico, se añadió el inicio automático de la lectura desde la nueva posición;
* Corregido un error que ocurría al consultar el tiempo restante con "control+shift+r" desde el inicio de la pista.

## Cambios para 20230728.0.0

* Aplicadas las reglas flake8 y mypy al código;
* Cambiada la versión mínima compatible de NVDA a 2019.3 para admitir las anotaciones introducidas en Python 3.

## Cambios para 20230607.0.0

* Añadidos los siguientes flujos de trabajo:
 * auto-update-translations - para actualizar automáticamente las traducciones desde el sistema de traducción de NVDA.
 * release-on-tag..yaml: para compilar y publicar el complemento tan pronto como se envíe una nueva etiqueta;
 * manual-release.yaml: para compilar y publicar manualmente nuevas versiones del complemento.
* Traducciones actualizadas.

## Cambios para la versión 20230508.0.0 y posteriores

* • Cambiado el número de versión, la versión mínima de NVDA y el enlace de descarga de acuerdo con las convenciones y requisitos de la tienda.

## Cambio para la versión 20.12

* Detención de la voz durante la grabación y la lectura para las versiones más recientes de mp3directcut;
* Corregida la lectura del tiempo restante para las nuevas versiones de NVDA que utilizan Python 3.

## Cambio para la versión 19.02

* Añadida la configuración del complemento en el panel de ajustes disponible desde nvda 2018.2;
* Modificada la numeración de versiones utilizando YY.MM (el año en 2 dígitos, seguido de un punto y del mes en 2 dígitos);
* Añadida compatibilidad con el nuevo formato de versionado de complementos aparecido desde nvda 2019.1.

## Cambio para la versión 4.0

* Añadida la compatibilidad del complemento con Python 2.7 y 3;
* Corregido un error con las rutas del complemento que contenían caracteres no ASCII.

## Cambio para la versión 3.0

* Utilizado el módulo gui.guiHelper para garantizar la correcta apariencia del cuadro de diálogo de configuración del complemento;
* Utilizado format en lugar de %s para las cadenas formateadas;
* Aplicadas las directrices de conformidad para la implementación.

## Cambio para la versión 2.3

* Añadida la licencia GPL al complemento;
* Modificado el atajo del script que proporciona el final de la selección de Ctrl + Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N no funciona con las versiones más recientes de mp3DirectCut;
* Añadido un script para confirmar que la selección ha sido cancelada con 'Ctrl+r';
* Realizadas algunas correcciones en el código del appModule 'mp3directcut.py'.

## Cambio para la versión 2.2

* Corrección de los scripts que proporcionan la ubicación de los marcadores de selección.

## Cambio para la versión 2.1.1

* Eliminado el script que proporciona el tiempo total y añadida esta información al script que proporciona el tiempo transcurrido;
* Añadida la posibilidad de activar o desactivar los anuncios relacionados con la tecla espacio en las opciones de configuración del módulo, de forma independiente a otros anuncios;
* Añadida la posibilidad de activar o desactivar el anuncio de colocación de los marcadores de selección en las opciones de configuración del módulo;
* Añadido el anuncio de la parte actual al desplazarse entre los puntos de corte;
* Corrección de los anuncios relacionados con las teclas verticales;
* Añadido un script para abrir la ayuda del complemento actual con 'NVDA+H';
* Trasladado el menú de configuración del complemento desde el menú Herramientas al menú Preferencias de NVDA.

## Cambio para la versión 2.1

* Añadido un script para vocalizar el desplazamiento al siguiente punto de división con Control+Flecha derecha;
* Añadido un script para vocalizar el desplazamiento al punto de división anterior con Control+Flecha izquierda;
* Añadido un script para vocalizar el desplazamiento de 4 centésimas de segundo hacia adelante con Shift+Flecha derecha;
* Añadido un script para vocalizar el desplazamiento de 4 centésimas de segundo hacia atrás con Shift+Flecha izquierda;
* Corregido el resumen del complemento de 'for mp3DirectCut' a 'mp3DirectCut'.

## Cambio para la versión 2.0

* Añadido un script para conocer el tiempo restante con 'Control Shift R';
* Corregida la lectura de duraciones que incluyen horas;
* Añadida la capacidad de diferenciar milésimas o centésimas de segundo.

## Cambio para la versión 1.1

* Añadida la posibilidad de incluir la categoría mp3DirectCut en Gestos de entrada;

    * Solo será visible durante el uso del software mp3DirectCut.

* Añadida la posibilidad de activar o desactivar los mensajes automáticos en el menú Herramientas de NVDA, elemento 'Configuración de mp3DirectCut';

## Cambio para la versión 1.0

* Versión inicial.
