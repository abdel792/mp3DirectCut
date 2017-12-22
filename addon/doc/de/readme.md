# Mp3DirectCut #

*	 Autoren: Abdel, Rémy, Abdellah zineddine, Jean-François Colas
*	 [Stabile Version herunterladen][1]
*	 Herunterladen der [Entwickler-Version][2]

# Beschreibung #

Diese Erweiterung verbessert die Zugänglichkeit von Mp3DirectCut mit NVDA.

Die Erweiterung wurde mit den mp3Direktcut-Versionen von 212 bis 223
getestet.

## Tastenkombinationen ##

Diese Erweiterung bietet folgende Tastaturbefehle:

*	B
	*	Bestätigt die korrekte Platzierung des Markers am Anfang der Auswahl B.
*	STRG+Umschalt+B
	*	Gibt die Position des Markers für den Beginn der Auswahl B an.
	*	Doppelter Druck gibt die Dauer der Auswahl an.
*	STRG+Umschalt+D
	*	Gibt die Dauer vom Anfang der Datei bis zur aktuellen Position des Wiedergabe-Cursors an.
	*	Doppelter Druck gibt die Gesamtdauer an.
*	STRG+R
	*	Bestätigt, dass die Auswahl abgebrochen wurde.
*	STRG+Umschalt+R
	*	Gibt die verbleibende Zeit von der aktuellen Position des Wiedergabe-Cursors bis zum Ende der Datei an.
*	STRG+Umschalt+E
	*	Gibt die Position des Markers für das Ende der Auswahl  N an.
	*	Doppelter Druck gibt zusammenfassende Positionen der Auswahl B und N an und spricht die Dauer der Auswahl aus.
*	STRG+Umschalt+P
	*	Gibt die Referenz des aktuellen Abschnitts und die Gesamtzahl der Abschnitte in der aktuellen Datei an.
*	STRG+Umschalt+Leerzeichen
	*	Regelt den aktuellen Pegel des Vu-Meters während der Aufnahme.
	*	Doppelter Druck setzt den Pegel zurück.
*	Abwärtspfeil
	*	Damit sehen Sie die aktuelle Position des Spielkopfes.
	*	Dieser Befehl positioniert den Cursor auch an der Position des Markers am Ende der Auswahl N, während die Position dieses Markers ausgesprochen wird.
	*	Im Lautstärke-Dialog spricht den nächsten Wert aus, der generell mit Abwärtspfeil erreicht werden kann.
	*	Dieser Wert wird standardmäßig nicht ausgesprochen.
*	Ende
	*	Bewegt den Wiedergabe-Cursor am Ende der aktuellen Datei und gibt die Gesamtzeit an.
*	Home
	*	Bewegt den Wiedergabe-Cursor an den Anfang der aktuellen Datei.
*	Linkspfeil
	*	Springt während der Wiedergabe um eine Sekunde zurück, wobei die aktuelle Dauer angegeben wird.
	*	Diese Vorspuhldauer ist in den Optionen von mp3Directcut konfigurierbar.
*	N
	*	Bestätigt die korrekte Platzierung des Markers am Ende der Auswahl N.
*	Seite ab
	*	Springt während der Wiedergabe um 10 Sekunden vorwärts, wobei die aktuelle Dauer angegeben wird.
	*	Diese Vorspuhldauer ist in den Optionen von mp3Directcut konfigurierbar.
*	Seite auf
	*	Springt während der Wiedergabe 10 Sekunden zurück, wobei die aktuelle Dauer angegeben wird.
	*	Diese RückwärtsDauer ist in den Optionen von mp3directcut konfigurierbar.
*	R
	*	Erlaubt es, eine Aufnahme vorzubereiten. Um zu beginnen, können Sie danach die Leertaste drücken.
*	Rechtspfeil
	*	Springt während der Wiedergabe um eine Sekunde vorwärts, während die aktuelle Dauer angegeben wird.
	*	Diese Vorspuhldauer ist in den Optionen von mp3directcut konfigurierbar.
*	STRG+Rechtspfeil
	*	Spring während der Wiedergabe vorwärts zum nächsten Orientierungspunkt und gibt gleichzeitig die aktuelle Dauer an.
*	STRG+Linkspfeil
	*	Springt während der Wiedergabe zum vorherigen Orientierungspunkt zurück und gibt gleichzeitig die aktuelle Dauer an.
*	Umschalt+Rechtspfeil
	*	Springt während der wiedergabe um vier Hundertstelsekunden vorwärts, wobei die aktuelle Dauer ausgesprochen wird.
*	Umschalt+Linkspfeil
	*	Springt während der Wiedergabe um vier Hundertstelsekunden zurück, wobei die aktuelle Dauer ausgesprochen wird.
*	S
	*	Stoppt das Vorlesen und gibt die aktuelle Dauer an.
*	Leertaste
	*	Beginnt mit der Aufnahme, wenn die Aufnahme nach dem Drücken  von r vorbereitet ist.
	*	Stoppt die Aufnahme und setzt den Cursor am Anfang, wenn eine Aufnahme läuft.
	*	Startet das Einlesen, nachdem eine Datei geladen ist.
	*	Pausiert das Einlesen und gibt die aktuelle Dauer an, wenn der Einlesevorgang läuft.
	*	Startet das Einlesen von der aktuellen Position, wenn der Vorgang vorher angehalten wurde.
*	Pfeil nach oben
	*	Damit sehen Sie die aktuelle Position des Spielkopfes.
	*	Dieser Befehl positioniert den Cursor auch auf die Position des Markers am Anfang der Auswahl B, während die Position dieses Markers ausgesprochen wird.
	*	Im Lautstärke-Dialog können Sie den vorherigen Wert hören, der im Allgemeinen mit Pfeil nach oben erreicht werden kann.
	*	Dieser Wert wird standardmäßig nicht ausgesprochen.
*	NVDA+H
	*	Öffnet die Hilfe der aktuellen Erweiterung.

## Änderungen in Version 3.0 ##

*	 Das Modul gui.guiHelper wurde anbewendet, um das Konfigurationsdialog der
   Erweiterung korrekt anzuzeigen.
*	 Statt %s wurde Format für formatierte Strings eingesetzt;
*	 Die Übereinstimmung mit Implementierungsvorgaben wurde finalisiert.

## Änderungen in Version 2.3 ##

*	 Die Erweiterung verfügt nun über eine GPL-Lizenz;
*	 Wegen Inkompatibilität mit den letzten Versionen dieser Erweiterung wurde
   die Tastenkombination für das Skript, welches das Ende der Auswahl
   ansagt, von STRG+Umschalt+N zu STRG+Umschalt+E geändert;
*	 Ein Skript wurde eingefügt, welches das Abbrechen der Auswahl mit STRG+R
   bestätigt;
*	 Es wurden Einige Verbesserungen im Appmodul 'mp3directcut.py'
   vorgenommen.

## Änderungen in Version 2.2 ##

*	 Es wurden die Skripte verbessert, die die Position der Auswahlmarker
   ausgeben.

## Änderungen in Version 2.1.1 ##

*	 Das Skript, das die Gesamtzeit ausgibt, wurde entfernt. Die Information
   wird nun das Skript für die verstrichene Zeit mit ausgeben.
*	 Die Ansagen, die sich auf die Leertaste beziehen, können nun in den
   Einstellungen des Moduls unabhängig von anderen Ansagen aktiviert oder
   deaktiviert werden;
*	 Die Ankündigung der Platzierung von Auswahlmarkern können nun in den
   Einstellungen des Moduls aktiviert oder deaktiviert werden;
*	 Der aktuelle Abschnitt beim Durchlaufen der Schnittpunkte wird nun
   angesagt;
*	 Ansagen, die sich auf vertikale Schlüssel beziehen, wurden verbessert;
*	 Ein Skript wurde hinzugefügt, welches das Öffnen der Hilfe der aktuellen
   Erweiterung mit NVDA + H ermöglicht;
*	 Das Konfigurationsmenü der Erweiterung wurde aus dem Menü Extras in das
   Menü Einstellungen von NVDA verschoben.

## Änderungen in Version 2.1 ##

*	 Ein Script wurde hinzugefügt, um die Bewegung zum nächsten
   Orientierungspunkt mit STRG+Rechtspfeil auszusprechen;
*	 Ein Script wurde hinzugefügt, um die Bewegung zum vorherigen
   Orientierungspunkt mit STRG+Linkspfeil auszusprechen;
*	 Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
   Sekunden vorwärts mit Umschalt+Rechtspfeil anzusagen;
*	 Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
   Sekunden rückwärts mit Umschalt+Linkspfeil anzusagen;
*	 Kleine Verbesserungen des Titels.

## Änderungen in Version 2.0 ##

*	 Ein Skript wurde hinzugefügt, um die verstrichene Zeit mit
   STRG+Umschalt+R anzusagen;
*	 Das Vorlesen der Dauer (inkl. Stunden) wurde verbessert;
*	 Es besteht nun die Möglichkeit zwischen hundertstel und tausendstel
   Sekunden zu unterscheiden;

## Änderungen in Version 1.1 ##

*	Es werden nun in Mp3DirectCut die Kategorie-Informationen der Eingabe-Gesten mit einbezogen.
*	Diese sind nur sichtbar, solange Sie Mp3DirectCut verwenden.
*	In der Konfiguration von Mp3DirectCut können Sie nun die automatischen Benachrichtigungen im NVDA-Menü ein- oder ausschalten.

## Änderungen in Version 1.0 ##

*	 Erste Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
