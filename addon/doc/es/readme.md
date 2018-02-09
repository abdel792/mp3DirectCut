# mp3DirectCut #

*	 Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descargar  [versión estable][1]
*	 Descargar [versión de desarrollo][2]

# Presentación #

Este complemento permite mejorar la accesibilidad del software mp3DirectCut
con NVDA.

Se ha probado con las versiones de mp3DirectCut que van desde la 212 hasta
la 223.

## Órdenes de teclado ##

Este complemento ofrece las siguientes órdenes:

*	B
	*	Permite confirmar la colocación correcta de la marca de inicio de la selección B.
*	Control+Shift+B
	*	Permite indicar la ubicación de la marca de inicio de selección B.
	*	Pulsando dos veces da la duración de la selección.
*	Control+Shift+D
	*	Da la duración transcurrida desde el inicio del archivo hasta la ubicación actual del cursor de reproducción.
	*	Pulsando dos veces da el tiempo total.
*	Control+R
	*	Confirma que la selección se ha cancelado.
*	Control+Shift+R
	*	Da el tiempo restante desde la posición actual del cursor de reproducción hasta el final del archivo.
*	Control+Shift+E
	*	Permite indicar la ubicación de la marca de final de selección N.
	*	Pulsando dos veces da un recapitulativo de la ubicación de los Tags B y N, así como la duración de la selección.
*	Control+Shift+P
	*	Da la referencia de la parte actual, así como el número total de partes.
*	Control+Shift+Espacio
	*	Permite indicar el valor actual del nivel del vúmetro.
	*	Pulsando dos veces permite reiniciar este nivel.
*	Flecha Abajo
	*	Permite dar la duración actual.
	*	Si se ha hecho una selección, coloca el cursor en la ubicación de la marca de final de selección N dando la ubicación de esta marca.
	*	En las opciones del control del volumen de mp3directcut, da el valor siguiente que generalmente se accede con la flecha abajo.
	*	Y que no es verbalizado por defecto.
*	Fin
	*	Permite mover el cursor de reproducción al final del archivo actual y da el tiempo total.
*	Inicio
	*	Permite mover el cursor de reproducción al inicio del archivo actual.
*	Flecha Izquierda
	*	Permite hacer un salto hacia atrás de un segundo durante una reproducción, dando la duración actual.
	*	La duración de este retroceso es configurable en las opciones de mp3directcut.
*	N
	*	Permite confirmar la colocación correcta de la marca de final de selección N.
*	Avance de página
	*	Permite hacer un salto hacia adelante de 10 segundos durante una reproducción, dando la duración actual.
	*	La duración de este salto hacia adelante es configurable en las opciones de mp3directcut.
*	Retroceso de página
	*	Permite hacer un salto hacia atrás de 10 segundos durante una reproducción, dando la duración actual.
	*	La duración de este salto hacia atrás es configurable en las opciones de mp3directcut.
*	R
	*	Permite preparar una grabación e indica si puedes pulsar sobre la barra espaciadora para iniciar.
*	Flecha Derecha
	*	Permite hacer un avance hacia adelante de un segundo durante una reproducción, dando la duración actual.
	*	La duración de este avance es configurable en las opciones de mp3directcut.
*	Control+Flecha Derecha
	*	Desplaza al siguiente punto de corte, dando la duración actual.
*	Control+Flecha Izquierda
	*	Desplaza al punto de corte anterior, dando la duración actual.
*	Shift+Flecha Derecha
	*	Permite hacer un avance hacia adelante de cuatro centésimas de segundo durante una reproducción, dando la duración actual.
*	Shift+Flecha Izquierda
	*	Permite hacer un retroceso de cuatro centésimas de segundo durante una reproducción, dando la duración actual.
*	S
	*	Permite detener la reproducción en curso, dando la duración actual.
*	Espacio
	*	Si la grabación está lista, permite iniciar ésta.
	*	Si una grabación está en curso, permite detenerla, colocando el cursor al inicio del archivo.
	*	Si un archivo está abierto, permite iniciar la reproducción.
	*	Si una reproducción está en curso, permite efectuar una pausa, dando la duración actual.
	*	Si una reproducción está en pausa, permite reiniciar la reproducción desde la ubicación actual.
*	Flecha Arriba
	*	Permite dar la duración actual.
	*	Si se ha hecho una selección, coloca el cursor en la ubicación de la marca de inicio de selección B, dando la ubicación de esta marca.
	*	En las opciones del control del volumen de mp3directcut, da el valor anterior al que generalmente se accede con la flecha arriba.
	*	Y que no es verbalizado por defecto.
*	NVDA+H
	*	Permite abrir la ayuda del actual complemento.

## Cambios para la versión 4.0 ##

*	 Añadido la compatibilidad del complemento con Python 2.7 y 3;
*	 Arreglado un error con rutas de complementos que no contienen caracteres
   ASCII.

## Cambios para la versión 3.0 ##

*	 Se utiliza el módulo gui.guiHelper para asegurarse de la correcta
   apariencia del diálogo de configuración del complemento;
*	 Se utiliza formato en lugar de %s para cadenas formateadas;
*	 Se cumplen las directrices de cumplimentación.

## Cambios para la versión 2.3 ##

*	 Se añade la licencia GPL al complemento;
*	 Se cambia el atajo de teclado del script que da fin a la selección de
   Ctrl + Shift + N a Ctrl + Shift + E porque Ctrl + Shift + N no funciona
   con  las últimas versiones de mp3DirectCut;
*	 Se añadió un script para confirmar que la selección se ha cancelado con
   'Control+r';
*	 Made some corrections in the code of the appModule 'mp3directcut.py'.

## Cambios para la versión 2.2 ##

*	 Corrección de los scripts que dan la localización de la selección de las
   marcas.

## Cambios para la versión 2.1.1 ##

*	 Supresión del script dando la duración total y añadida esta información
   para el script que da el tiempo transcurrido;
*	 Añadida la posibilidad de activar o desactivar los anuncios relacionados
   con la tecla de espacio en las opciones de configuración del complemento,
   por separado de los otros anuncios;
*	 Añadida la posibilidad para activar o desactivar el anuncio para la buena
   colocación de marcas de selección en las opciones de configuración del
   complemento;
*	 Añadido el anuncio de la parte actual cuando se mueve entre los puntos de
   corte;
*	 Corrección de los anuncios relacionados con las teclas verticales;
*	 Añadido un Script para abrir la ayuda del actual complemento accesible
   gracias a la orden de teclado "NVDA+H";
*	 Desplazamiento del menú de configuración del complemento del menú
   Herramientas al menú Preferencias de NVDA.

## Cambios para la versión 2.1 ##

*	 Añadido un Script para vocalizar el siguiente punto de corte con
   Control+Flecha Derecha;
*	 Añadido un Script para vocalizar el punto de corte anterior con
   Control+Flecha Izquierda;
*	 Añadido un Script para vocalizar el desplazamiento de 4 centésimas de
   segundo hacia adelante con Shift+Flecha Derecha;
*	 Añadido un Script para vocalizar el desplazamiento de 4 centésimas de
   segundo hacia atrás con Shift+Flecha Izquierda;
*	 Corrección del summary del complemento de "para mp3DirectCut" a
   "mp3DirectCut".

## Cambios para la versión 2.0 ##

*	 Añadido un Script para saber el tiempo restante con "Control+Shift+R";
*	 Corrección de la lectura de las duraciones incluyendo las horas;
*	 Añadida la posibilidad de diferenciar milésimas o centésimas de segundos.

## Cambios para la versión 1.1 ##

*	 Añadida la posibilidad para incluir las órdenes del complemento entre los Gestos de entrada, en la categoría "mp3DirectCut";
*	 Ellas serán visibles sólo durante una utilización del software mp3DirectCut.
*	 Se ha añadido la posibilidad de activar o desactivar los mensajes automáticos, en el menú Herramientas NVDA, elemento de menú "Configuración del complemento mp3DirectCut";

## Cambios para la versión 1.0 ##

*	 Primera versión

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
