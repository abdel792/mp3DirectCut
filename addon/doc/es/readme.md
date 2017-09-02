# mp3DirectCut #

*	 Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descargar  [versión estable][1]
*	 Descargar [versión de desarrollo][2]

# Presentación #

Este complemento permite mejorar la accesibilidad del software mp3DirectCut
con NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Órdenes de teclado ##

This addon offers the following commands:

*	B
	*	Used to confirm correct placement of the marker of the beginning of the selection B.
*	Ctrl+Shift+B
	*	Used to indicate the position of the marker of the beginning of selection B.
	*	Double pressure lets give you the duration of the selection.
*	Ctrl+Shift+D
	*	Gives the duration from the beginning of the file to the current position of the playback cursor.
	*	Double pressure lets give you the total duration.
*	Ctrl+R
	*	Confirms that the selection has been canceled.
*	Ctrl+Shift+R
	*	Gives the time remaining from the current position of the playback cursor to the end of the file.
*	Ctrl+Shift+E
	*	Used to indicate the position of the marker of the end of selection N.
	*	Double pressure gives recapitulatif positions B and N, and the duration of the selection.
*	Ctrl+Shift+P
	*	Give the reference of the actual part and the total number of parts in the current file.
*	Ctrl+Shift+Space
	*	Used to determine the current level of the vu-meter, during recording.
	*	Double pressure reset it.
*	Down Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the end of selection N, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the next value that can be reached generally with downArrow.
	*	This value is not vocalized default.
*	End
	*	Moves the playback cursor at the end of the current file and give the total time.
*	Home
	*	Moves the playback cursor at the beginning of the current file.
*	Left Arrow
	*	Lets make a brief return back of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	N
	*	Used to confirm correct placement of the marker of the end of the selection N.
*	Page Down
	*	Lets make a leap forward of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Page Up
	*	Lets make a return back of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	R
	*	Allows to prepare a record and whether you can press spacebar to start.
*	Right Arrow
	*	Lets do a brief forward of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Ctrl+Right Arrow
	*	Moves to the next splitting point, while giving the current duration.
*	Ctrl+Left Arrow
	*	Moves to the previous splitting point, while giving the current duration.
*	Shift+Right Arrow
	*	Lets do a brief forward of four hundredths of seconds during playback, while giving the current duration.
*	Shift+Left Arrow
	*	Lets do a brief backwards of four hundredths of seconds during playback, while giving the current duration. 
*	S
	*	Used to stop the reading and give the current duration.
*	Space
	*	If the recording is ready, start this recording.
	*	If a recording is in progress, stop it by positioning the cursor at the beginning.
	*	If a file is loaded, start the reading.
	*	If a read is in progress, allows to do a pause by giving current duration.
	*	If read is paused, allows to restart the reading from the current location.
*	Up Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the beginning of selection B, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the previous value that can be reached generally with upArrow.
	*	This value is not vocalized default.
*	NVDA+H
	*	Lets open the help of the current add-on.

## Change for version 3.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   addon's configuration dialog;
*	 Used format instead of %s for formatted strings;
*	 Used compliance with guidelines for implementation.

## Change for version 2.3 ##

*	 Added the GPL license to the addon;
*	 Changed the shortcut of the script giving the end of selection from Ctrl
   + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work
   with the latest versions of mp3DirectCut;
*	 Added a script to confirm that the selection has been canceled with
   'Ctrl+r';
*	 Maked some correction in the code of the appModule 'mp3directcut.py'.

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
