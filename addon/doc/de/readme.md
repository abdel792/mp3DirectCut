# Mp3DirectCut #

*	 Autoren: Abdel, Rémy, Abdellah zineddine, Jean-François Colas
*	 [Stabile Version herunterladen][1]
*	 Herunterladen der [Entwickler-Version][2]

# Presentation #

Diese Erweiterung verbessert die Zugänglichkeit von Mp3DirectCut mit NVDA.

Getestet wurde es mit den Versionen von 212 bis 222.

## Tastenkurzbefehle ##

Diese Erweiterung bietet die folgenden Befehle an, die Sie im NVDA-Menü bei
den Eingabe-Gesten für Mp3DirectCut selbstverständlich nach Belieben selbst
anpassen können:

*	B
	*	Used to confirm correct placement of the marker of the beginning of the selection B.
*	Strg+Umschalt+B
	*	Used to indicate the position of the marker of the beginning of selection B.
	*	Doppelt gedrückt gibt die Dauer des ausgewählten Bereichs aus.
*	Strg+Umschalt+D
	*	Gibt die Dauer vom Anfang der Datei bis zur aktuellen Cursor-Position aus.
	*	Doppelt gedrückt gibt die Gesamtdauer aus.
*	Strg+Umschalt+R
	*	Gibt die Dauer von der aktuellen Cursor-Position bis zum Ende der Datei aus.
*	Strg+Umschalt+N
	*	Used to indicate the position of the marker of the end of selection N.
	*	Double pressure gives recapitulatif positions B and N, and the duration of the selection.
*	Strg+Umschalt+P
	*	Nennt den tatsächlichen Bereich und die Gesamtanzahl aller Teilbereiche der aktuellen Datei.
*	Strg+Umschalt+Leertaste
	*	Used to determine the current level of the vu-meter, during recording.
	*	Doppelt gedrückt wird es wieder zurückgesetzt.
*	Pfeiltaste nach unten
	*	Gibt die aktuelle Position der Wiedergabe aus.
	*	This command also position the cursor at the location of the marker of the end of selection N, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the next value that can be reached generally with downArrow.
	*	Dieser Wert wird standardmäßig nicht angesagt.
*	Ende
	*	Moves the playback cursor at the end of the current file and give the total time.
*	Pos1
	*	Moves the playback cursor at the beginning of the current file.
*	Pfeiltaste nach links
	*	Lets make a brief return back of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	N
	*	Used to confirm correct placement of the marker of the end of the selection N.
*	Seite nach unten
	*	Lets make a leap forward of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Seite nach oben
	*	Lets make a return back of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	R
	*	Allows to prepare a record and whether you can press spacebar to start.
*	Pfeiltaste nach rechts
	*	Lets do a brief forward of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Strg+Pfeiltaste nach rechts
	*	Moves to the next splitting point, while giving the current duration.
*	Strg+Pfeiltaste nach links
	*	Moves to the previous splitting point, while giving the current duration.
*	Umschalt+Pfeiltaste nach rechts
	*	Lets do a brief forward of four hundredths of seconds during playback, while giving the current duration.
*	Umschalt+Pfeiltaste nach links
	*	Lets do a brief backwards of four hundredths of seconds during playback, while giving the current duration. 
*	S
	*	Used to stop the reading and give the current duration.
*	Leertaste
	*	If the recording is ready, start this recording.
	*	If a recording is in progress, stop it by positioning the cursor at the beginning.
	*	If a file is loaded, start the reading.
	*	If a read is in progress, allows to do a pause by giving current duration.
	*	If read is paused, allows to restart the reading from the current location.
*	Pfeiltaste nach oben
	*	Gibt die aktuelle Position der Wiedergabe aus.
	*	This command also position the cursor at the location of the marker of the beginning of selection B, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the previous value that can be reached generally with upArrow.
	*	Dieser Wert wird standardmäßig nicht angesagt.
*	NVDA+H
	*	Öffnet die Hilfe zu dieser Erweiterung.

## Change for version 2.2 ##

*     Correction of the scripts giving the selection markers' locations.

## Änderungen in Version 2.1.1 ##

*	 Removing the script giving the total time and adding this information to
   the script giving the elapsed time;
*	 Added the ability to enable or disable the announcements related to the
   space key in the module's configuration options, separately from other
   announcements;
*	 Added the ability to enable or disable the announcement of placement of
   the selection marqueures in the module's configuration options;
*	 Adding the announcement of the current part when moving through the
   cutting points;
*	 Correction of announcements related to vertical keys;
*	 Adding a script to open the help of the current add-on with 'NVDA+H';
*	 Displacement of the add-on's configuration menu from the Tools menu to
   the Preferences menu of NVDA.

## Änderungen in Version 2.1 ##

*	 Adding a script to vocalize moving to the next splitting point with
   Control+Right Arrow;
*	 Adding a script to vocalize moving to the previous splitting point with
   Control+Left Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second
   ahead, with Shift+Right Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second
   back, with Shift+Left Arrow;
*	 Correction of the addon's summary from 'for mp3DirectCut' to
   'mp3DirectCut'.

## Änderungen in Version 2.0 ##

*	 Adding a script to know the remaining time with 'Control Shift R';
*	 Fixed reading durations including hours;
*	 Added ability to differentiate thousandths or hundredths of seconds.

## Änderungen in Version 1.1 ##

*	Es werden nun in Mp3DirectCut die Kategorie-Informationen der Eingabe-Gesten mit einbezogen.
*	Diese sind nur sichtbar, solange Sie Mp3DirectCut verwenden.
*	In der Konfiguration von Mp3DirectCut können Sie nun die automatischen Benachrichtigungen im NVDA-Menü ein- oder ausschalten.

## Änderungen in Version 1.0 ##

*	 Erste Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
