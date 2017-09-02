# mp3DirectCut #

*	 Tekijät: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Lataa [vakaa versio][1]
*	 Lataa [kehitysversio][2]

# Esittely #

Tämä lisäosa parantaa mp3DirectCut-ohjelman esteettömyyttä NVDA:n kanssa.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Pikanäppäimet ##

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

## Muutokset versiossa 2.2 ##

*	 Valitun alueen  merkkien sijainnit ilmoittavat skriptit korjattu.

## Muutokset versiossa 2.1.1 ##

*	 Kokonaisajan ilmoittava skripti poistettu ja lisätty sen antamat tiedot
   jäljellä olevan ajan ilmoitukseen;
*	 Lisäosan asetuksiin lisätty mahdollisuus muista ilmoituksista erillisten
   välilyöntinäppäimeen liittyvien ilmoitusten käyttöön ottamiseen tai
   käytöstä poistamiseen;
*	 Lisäosan asetuksiin lisätty mahdollisuus valintamerkkien
   sijainti-ilmoituksen käyttöön ottamiseen tai käytöstä poistamiseen;
*	 Lisätty mahdollisuus nykyisen sijainnin ilmoittamiseen leikkauskohtien
   välillä liikuttaessa;
*	 Korjattu nuoli ylös- ja nuoli alas -näppäimiin liittyvät ilmoitukset;
*	 Lisätty skripti lisäosaohjeen avaamiseen näppäinkomennolla NVDA+H;
*	 Siirretty lisäosan asetusvalintaikkuna Työkalut-valikosta
   Asetukset-valikkoon.

## Muutokset versiossa 2.1 ##

*	 Lisätty skripti, joka puhuu seuraavan leikkauskohdan siirryttäessä siihen
   näppäinkomennolla Control+Nuoli oikealle;
*	 Lisätty skripti, joka puhuu edellisen leikkauskohdan siirryttäessä siihen
   näppäinkomennolla Control+Nuoli vasemmalle;
*	 Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
   eteenpäin näppäinkomennolla Shift+Nuoli oikealle;
*	 Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
   taaksepäin näppäinkomennolla Shift+Nuoli vasemmalle;
*	 Korjattu lisäosan yhteenvedoksi "mp3DirectCut".

## Muutokset versiossa 2.0 ##

*	 Lisätty jäljellä olevan ajan ilmoittava komento Control+Shift+R;
*	 Korjattu keston, tunnit mukaan lukien, lukeminen;
*	 Lisätty mahdollisuus sekunnin tuhannes- ja sadasosien erottamiseen
   toisistaan.

## Muutokset versiossa 1.1 ##

*	 Syöte-eleet-valintaikkunaan lisätty mp3DirectCut-kategoria;
	*	 sen sisältämät komennot ovat näkyvissä vain ohjelman ollessa käynnissä.
*	 Lisätty mahdollisuus automaattisten ilmoitusten käyttöön ottamiseen tai käytöstä poistamiseen NVDA:n Työkalut-valikon mp3DirectCut-kohteeseen;

## Muutokset versiossa 1.0 ##

*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
