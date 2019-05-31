# mp3DirectCut #

* Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Descargar  [versión estable][1]
* Descargar [versión de desarrollo][2]

# Presentación #

Este complemento permite mejorar la accesibilidad del software mp3DirectCut
con NVDA.

Se ha probado con las versiones de mp3DirectCut que van desde la 212 hasta
la 223.

## Órdenes de teclado ##

Este complemento ofrece las siguientes órdenes:

* B

    * Se usa para confirmar la situación correcta del marcador de inicio de
      la selección B.

* Ctrl+Shift+B

    * Se usa para indicar la posición del marcador de inicio de la selección
      B.
    * Con una doble pulsación devuelve la duración de la selección.

* Ctrl+Shift+D

    * Da la posición desde el comienzo del archivo hasta la posición actual
      del cursor de reproducción.
    * Con una doble pulsación indica la duración total.

* Ctrl+R

    * Confirma que se ha cancelado la selección.

* Ctrl+Shift+R

    * Devuelve el tiempo restante desde la posición actual del cursor de
      reproducción hasta el final del archivo.

* Ctrl+Shift+E

    * Se usa para indicar la posición del marcador del fin de la selección
      N.
    * Si se pulsa dos veces devuelve las posiciones B y N, y la duración de
      la selección.

* Ctrl+Shift+P

    * Da la referencia de la parte actual y la cantidad total de partes del
      archivo.

* Ctrl+Shift+Espacio

    * Se usa para determinar el nivel actual del volumen del micrófono
      durante la grabación.
    * Una doble pulsación lo restablece.

* Flecha abajo

    * Te permite saber la posición actual del cursor de reproducción.
    * Esta orden también sitúa el cursor en la posición del marcador del
      final de la selección N, mientras da la ubicación de este marcador si
      se ha hecho una selección.
    * En el cuadro de diálogo de volumen, verbaliza el siguiente valor que
      generalmente puede alcanzarse pulsando flecha abajo.
    * Este valor no se verbaliza por defecto.

* Fin

    * Mueve el cursor de reproducción al final del archivo actual e indica
      la duración total.

* Inicio

    * Mueve el cursor de reproducción al comienzo del archivo actual.

* Flecha izquierda

    * Retrocede un segundo durante la reproducción e indica la duración
      actual.
    * Esta duración es configurable en las opciones de MP3DirectCut.

* N

    * Se usa para confirmar la situación correcta del marcador de fin de
      selección N.

* Avance página

    * Adelanta 10 segundos la reproducción e indica la duración actual.
    * Esta duración es configurable en las opciones de MP3DirectCut.

* Retroceso página

    * Retrocede 10 segundos en la reproducción e indica la duración actual.
    * Esta duración es configurable en las opciones de MP3DirectCut.

* R

    * Prepara una grabación, que se puede iniciar pulsando Espacio.

* Flecha derecha

    * Adelanta un segundo la reproducción e indica la duración actual.
    * Esta duración es configurable en las opciones de MP3DirectCut.

* CTRL+Flecha derecha

    * Se mueve al siguiente punto de división e indica la duración actual.

* CTRL+flecha izquierda

    * Se mueve al punto de división anterior e indica la duración actual.

* Shift+flecha derecha

    * Adelanta cuatro centésimas de segundo en la reproducción e indica la
      duración actual.

* Shift+flecha izquierda

    * Retrocede cuatro centésimas de segundo en la reproducción e indica la
      duración actual.

* S

    * Detiene la reproducción e indica la duración actual.

* Espacio

    * Si la grabación está preparada, la inicia.
    * Si hay una grabación en progreso, la detiene y sitúa el cursor al
      principio.
    * Si hay un archivo cargado, comienza la reproducción.
    * Si hay una reproducción en curso, la pausa e indica la duración
      actual.
    * Si la reproducción está en pausa, la reanuda desde la posición actual.

* Flecha arriba

    * Te permite saber la posición actual del cursor de reproducción.
    * Esta orden también sitúa el cursor en la ubicación del marcador del
      principio de la selección B, e indica la posición de este marcador si
      se ha hecho una selección.
    * En el cuadro de diálogo de volumen, verbaliza el valor anterior que se
      puede alcanzar pulsando flecha arriba.
    * Este valor no se verbaliza por defecto.

* NVDA+H

    * Te permite abrir la ayuda del complemento actual.

## Compatibilidad ##

* Este complemento es compatible con las versiones de NVDA que van desde la
  2016.4 hasta la 2019.3.

## Cambios para la versión 19.02 ##

* Se ha añadido la configuración del complemento al diálogo de opciones
  disponible desde NVDA 2018.2;
* Se ha cambiado el número de versión siguiendo el esquema AA.MM (dos
  dígitos para el año, seguidos de un punto y dos dígitos para el mes);
* Se ha añadido compatibilidad con el nuevo formato de versiones de
  complementos, disponible en NVDA 2019.1.

## Cambios para la versión 4.0 ##

* Añadido la compatibilidad del complemento con Python 2.7 y 3;
* Arreglado un error con rutas de complementos que no contienen caracteres
  ASCII.

## Cambios para la versión 3.0 ##

* Se utiliza el módulo gui.guiHelper para asegurarse de la correcta
  apariencia del diálogo de configuración del complemento;
* Se utiliza formato en lugar de %s para cadenas formateadas;
* Se cumplen las directrices de cumplimentación.

## Cambios para la versión 2.3 ##

* Se añade la licencia GPL al complemento;
* Se cambia el atajo de teclado del script que da fin a la selección de Ctrl
  + Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N no funciona con
  las últimas versiones de mp3DirectCut;
* Se añadió un script para confirmar que la selección se ha cancelado con
  'Control+r';
* Se hicieron algunas correcciones en el código del appModule
  'mp3directcut.py'.

## Cambios para la versión 2.2 ##

* Corrección de los scripts que dan la localización de la selección de las
  marcas.

## Cambios para la versión 2.1.1 ##

* Supresión del script dando la duración total y añadida esta información
  para el script que da el tiempo transcurrido;
* Añadida la posibilidad de activar o desactivar los anuncios relacionados
  con la tecla de espacio en las opciones de configuración del complemento,
  por separado de los otros anuncios;
* Añadida la posibilidad para activar o desactivar el anuncio para la buena
  colocación de marcas de selección en las opciones de configuración del
  complemento;
* Añadido el anuncio de la parte actual cuando se mueve entre los puntos de
  corte;
* Corrección de los anuncios relacionados con las teclas verticales;
* Añadido un Script para abrir la ayuda del actual complemento accesible
  gracias a la orden de teclado "NVDA+H";
* Desplazamiento del menú de configuración del complemento del menú
  Herramientas al menú Preferencias de NVDA.

## Cambios para la versión 2.1 ##

* Añadido un Script para vocalizar el siguiente punto de corte con
  Control+Flecha Derecha;
* Añadido un Script para vocalizar el punto de corte anterior con
  Control+Flecha Izquierda;
* Añadido un Script para vocalizar el desplazamiento de 4 centésimas de
  segundo hacia adelante con Shift+Flecha Derecha;
* Añadido un Script para vocalizar el desplazamiento de 4 centésimas de
  segundo hacia atrás con Shift+Flecha Izquierda;
* Corrección del summary del complemento de "para mp3DirectCut" a
  "mp3DirectCut".

## Cambios para la versión 2.0 ##

* Añadido un Script para saber el tiempo restante con "Control+Shift+R";
* Corrección de la lectura de las duraciones incluyendo las horas;
* Añadida la posibilidad de diferenciar milésimas o centésimas de segundos.

## Cambios para la versión 1.1 ##

* Se ha añadido la capacidad de incluir la categoría MP3DirectCut en el
  diálogo Gestos de entrada;

    * Sólo serán visibles durante el uso del software MP3DirectCut.

* Añadida la posibilidad de activar o desactivar los mensajes automáticos
  desde el menú Herramientas de NVDA, elemento 'Configuración de
  MP3DirectCut';

## Cambios para la versión 1.0 ##

* Primera versión.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
