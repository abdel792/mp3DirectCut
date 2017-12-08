# mp3DirectCut #

*	 Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Preuzmi[stabilnu verziju][1]
*	 Preuzmi[razvojnu verziju][2]

# Predstavljanje #

Ovaj dodatak poboljšava pristupačnost programa mp3DirectCut sa programom
NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Prečice ##

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
*	 Made some corrections in the code of the appModule 'mp3directcut.py'.

## Promene u verziji 2.2 ##

*	 Popravljene prečice za lokaciju izbora

## Promene u verziji 2.1.1 ##

*	 Uklonjena prečica za ukupno vreme i prebačena na prečicu za preostalo
   vreme
*	 Dodata mogućnost da onemogućite izgovor razmaka, odvojeno od drugih
   objava
*	 Dodata mogućnost podešavanja izgovora izbora
*	 Dodat  izgovor isečenih delova kada se krećete kroz zapis
*	 Popravljen izgovor uspravnih tastera
*	 Dodata prečica za otvaranje pomoći dodatka komandom NVDA+h
*	 Pomeranje stavke za podešavanje dodatka iz menija alati u meni
   podešavanja

## Promene u verziji 2.1 ##

*	 Dodata prečica za izgovor pomeranja na sledeću stavku komandom
   Kontrol+strelica desno
*	 Dodata prečica za izgovor pomeranja na prethodnu stavku komandom
   Kontrol+strelica levo
*	 Dodata prečica za izgovor pomeranja komandom šift+ strelica desno
*	 Dodata prečica za izgovor pomeranja komandom šift+ strelica levo
*	 Popravljeno ime dodatka iz 'for mp3DirectCut' u 'mp3DirectCut'.

## Promene u verziji 2.0 ##

*	 Dodata prečica za izgovor preostalog vremena 'Control Shift R';
*	 Popravljeno čitanje trajanja uključujući sate
*	 Dodata sposobnost razlikovanja desetinki i stotinki

## Promene u verziji 1.1 ##

*	 Dodata sposobnost prepoznavanja MP3 DirectCut u ulaznim komandama;
	*	 Biće dostupne samo kada koristite MP3 DirectCut program.
*	 Dodata sposobnost da omogućite ili onemogućite automatske poruke, u meniju alati NVDA menija, stavka 'mp3DirectCut podešavanja';

## Promene u verziji 1.0 ##

*	 Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
