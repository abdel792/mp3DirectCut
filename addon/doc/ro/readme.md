# mp3DirectCut #

*	 Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descărcați [versiunea stabilă][1]
*	 Descărcați [versiunea în dezvoltare][2]

# Prezentare #

Acest supliment îmbunătățește accesibilitatea programului mp3DirectCut cu
NVDA.

A fost testat cu versiuni ale mp3DirectCut de la 212 până la 222.

## Scurtături ##

Acest supliment oferă următoarele comenzi pe care le puteți modifica mergând
în meniul preferințe / Gesturi de intrare' în categoria 'mp3DirectCut':

*	B
	*	Used to confirm correct placement of the marker of the beginning of the selection B.
*	Ctrl+Shift+B
	*	Used to indicate the position of the marker of the beginning of selection B.
	*	Double pressure lets give you the duration of the selection.
*	Ctrl+Shift+D
	*	Gives the duration from the beginning of the file to the current position of the playback cursor.
	*	Double pressure lets give you the total duration.
*	Ctrl+Shift+R
	*	Gives the time remaining from the current position of the playback cursor to the end of the file.
*	Ctrl+Shift+N
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

## Modificări aduse în versiunea 2.2 ##

*     Corecția scripturilor care dau locația selectată a marcajelor.

## Modificări aduse în versiunea 2.1.1 ##

*	 Eliminarea scriptului care dă timpul total și adaugă această informație
   la scriptul care dă timpul scurs.
*	 A fost adăugată abilitatea de a activa sau dezactiva anunțurile relatate
   la tasta spațiu în opțiunile de configurare ale modulelor separat din
   alte anunțuri;
*	 A fost adăugată abilitatea de a activa sau dezactiva anunțul plasat
   selecției marque în opțiunile de configurare ale modulelor;
*	 Adăugarea anunțării părții curente atunci când se deplasează prin
   punctele de tăiere;
*	 Corectarea anunțurilor relatate la tastele verticale;
*	 Adăugarea unui script pentru a deschide ajutorul add-onului curent cu
   'NVDA+H';
*	 Deplasare din meniul de configurare ale add-onurilor la meniul
   instrumente către meniul preferințe nvda.

## Modificări aduse în versiunea 2.1 ##

*	 Adăugarea unui script pentru a cânta se deplasează la următorul punct
   divizat cu control+săgeată dreapta;
*	 Adăugarea unui script pentru a cânta se deplasează la punctul anterior
   divizat cu control+săgeată stânga;
*	 Adăugarea unui script pentru a cânta se deplasează cu 400 de secunde
   înainte, cu shift+săgeată dreapta;
*	 Adăugarea unui script pentru a cânta se deplasează cu 400 de secunde în
   urmă, cu shift+săgeată stânga;
*	 Corectarea cuprinsului add-on-ului de la 'for mp3DirectCut' la
   'mp3DirectCut'.

## Modificări în versiunea 1.0 ##

*	 A fost adăugat un script pentru cunoașterea timpului rămas cu 'Control
   Shift R';
*	 A fost reparată durata orelor;
*	 A fost adăugată abilitatea de diferențiere între mi și sute de secunde;

## Modificări aduse în versiunea 1.1 ##

*	 Added the ability to include the mp3DirectCut category into the Input Gestures;
	*	 They will be visible only during use of the mp3DirectCut software.
*	 Added the ability to enable or disable automatic messages, in the tools menu of NVDA, item 'mp3DirectCut configuration';

## Modificări adyse în 1.0 ##

*	 Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
