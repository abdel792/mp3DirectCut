# mp3DirectCut #

*	 Autor(es: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descargar  [versión estable][1]
*	 Descargar [versión de desenvolvemento][2]

# Presentación #

Este complemento permite mellorar a accesibilidade do programa mp3DirectCut
co NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Atallos de teclado ##

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

## Cambio para la versión 2.2 ##

*	 Correción dos scripts que dan a localización dos marcadores de seleción.

## Cambios para a versión 2.1.1 ##

*	 Borrado do script dando a duración total e engadida esta información para
   o script que da o tempo transcorrido;
*	 Engadida a posibilidade de activar ou desactivar os anuncios relacionados
   coa tecla de espazo nas opcións de configuración do complemento, por
   separado dos outros anuncios;
*	 Engadida a posibilidade para activar ou desactivar o anuncio para a boa
   colocación de marcas de seleción nas opcións de configuración do
   complemento;
*	 Engadido o anuncio da parte actual cando se move entre os pontos de
   corte;
*	 Correción dos anuncios relacionados coas teclas verticais;
*	 Engadido un Script para abrir a axuda do actual complemento accesible
   grazas á orde de teclado "NVDA+H";
*	 Desprazamento do menú de configuración do complemento do menú Ferramentas
   ao menú Preferencias do NVDA.

## Cambios para a versión 2.1 ##

*	 Engadido un Script para falar o seguinte ponto de corte co Control+Frecha
   Dereita;
*	 Engadido un Script para falar o ponto de corte anterior co Control+Frecha
   Esquerda;
*	 Engadido un Script para falar o desprazamento de 4 centésimas de segundo
   cara adiante co Shift+Frecha Dereita;
*	 Engadido un Script para falar o desprazamento de 4 centésimas de segundo
   cara atrás co Shift+Frecha Esquerda;
*	 Corrección do summary do complemento "para mp3DirectCut" a
   "mp3DirectCut".

## Cambios para a versión 2.0 ##

*	 Engadido un Script para saber o tempo restante co "Control+Shift+R";
*	 Corrección da lectura das duracións incluindo as horas;
*	 Engadida a posibilidade de diferenciar milésimas ou centésimas de
   segundos.

## Cambios para a versión 1.1 ##

*	 Engadida a posibilidade para incluir as ordes do complemento entre os xestos de entrada, na categoría "mp3DirectCut";
*	 Serán visibles só durante unha utilización do programa mp3DirectCut.
*	 Engadiuse a posibilidade de activar ou desactivar as mensaxes automáticas, no menú Ferramentas NVDA, elemento de menú "Configuración do complemento mp3DirectCut";

## Cambios para a versión 1.0 ##

*	 versión inicial

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
