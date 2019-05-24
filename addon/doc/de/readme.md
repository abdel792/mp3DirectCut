# Mp3DirectCut #

* Autoren: Abdel, Rémy, Abdellah zineddine, Jean-François Colas
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

# Beschreibung #

Diese Erweiterung verbessert die Zugänglichkeit von Mp3DirectCut mit NVDA.

Die Erweiterung wurde mit den mp3Direktcut-Versionen von 212 bis 223
getestet.

## Tastenkombinationen ##

Diese Erweiterung bietet folgende Tastaturbefehle:

* B

    * Wird verwendet, um die korrekte Platzierung des Markers am Anfang der
      Auswahl B zu bestätigen.

* STRG+Umschalt+B

    * Wird verwendet, um die Position des Markers vom Anfang der Auswahl B
      anzusagen.
    * Zweimaliges Drücken meldet die Dauer der Auswahl.

* STRG+Umschalt+D

    * Meldet die Dauer vom Anfang der Datei bis zur aktuellen Position des
      Wiedergabecursors.
    * Zeimaliges Drücken meldet die Gesamtdauer.

* STRG+R

    * Beschtätigt das Abbrechen der Auswahl.

* STRG+Umschalt+R

    * Meldet die Restzeit von der aktuellen Wiedergabeposition bis zum Ende
      der Datei.

* STRG+Umschalt+E

    * Wird verwendet, um die Position des Markers vom Ende der Auswahl N zu
      melden.
    * Zweimaliges Drücken wiederholt die Positionen B und N und die Dauer
      der Auswahl.

* STRG+Umschalt+P

    * Meldet die Referenz des aktuellen Abschnitts und die Gesamtzahl der
      Abschnitte in der aktuellen Datei.

* STRG+Umschalt+Leertaste

    * Wird verwendet, um den aktuellen Pegel des Vu-Meters während der
      Aufzeichnung zu bestimmen.
    * Zweimaliges Drücken setzt ihn zurück.

* Pfeil abwärts

    * Meldet die aktuelle Position des Wiedergabekopfes.
    * Dieser Befehl positioniert den Cursor auch an der Position des Markers
      am Ende der Auswahl N, während die Position dieses Markers gemeldet
      wird, sofern eine Auswahl getroffen wurde.
    * Meldet im Lautstärke-Dialogfeld den nächsten Wert, der generell mit
      Pfeil abwärts erreicht werden kann.
    * Dieser Wert ist keine vokalisierte Voreinstellung.

* Ende

    * Bewegt den Wiedergabecursor am Ende der aktuellen Datei und meldet die
      Gesamtdauer.

* Pos1

    * Bewegt den Wiedergabecursor an den Anfang der aktuellen Datei.

* Pfeil links

    * Springt während der Wiedergabe eine Sekunde rückwärts, während die
      aktuelle Dauer gemeldet wird.
    * Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

* N

    * Wird verwendet, um die korrekte Platzierung des Markers am Ende der
      Auswahl N zu bestätigen.

* Seite ab

    * Springt während der Wiedergabe 10 Sekunden vorwärts, während die
      aktuelle Dauer gemeldet wird.
    * Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

* Seite auf

    * Springt während der Wiedergabe 10 Sekunden rückwärts, während die
      aktuelle Dauer gemeldet wird.
    * Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

* R

    * Ermöglicht die Vorbereitung einer Aufnahme. Drücken Sie die Leertaste
      zum Starten.

* Pfeil rechts

    * Springt während der Wiedergabe eine Sekunde vorwärts, während die
      aktuelle Dauer gemeldet wird.
    * Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

* STRG+Pfeil rechts

    * Springt zum nächsten Aufteilungspunkt, wobei die aktuelle Dauer
      gemeldet wird.

* STRG+Pfeil links

    * Springt zum vorherigen Aufteilungspunkt, wobei die aktuelle Dauer
      gemeldet wird.

* Umschalt+Pfeil rechts

    * Springt während der Wiedergabe vierhundertstel Sekunden vorwärts,
      während die aktuelle Dauer gemeldet wird.

* Umschalt+Pfeil links

    * Springt während der Wiedergabe vierhundertstel Sekunden rückwärts,
      während die aktuelle Dauer gemeldet wird.

* S

    * Wird verwendet, um den Lesevorgang zu stoppen und die aktuelle Dauer
      zu melden.

* Leertaste

    * Startet die Aufnahme, sofern diese vorbereitet ist.
    * Wenn eine Aufnahme läuft, wird sie gestoppt und der Cursor wird am
      Anfang positioniert.
    * Startet das Lesen, wenn eine Datei geladen ist.
    * Meldet die aktuelle Dauer und pausiert währenddessen das Lesen.
    * Wenn das Lesen angehalten wird, kann es von der aktuellen Position
      weiter ausgeführt werden.

* Pfeil aufwärts

    * Meldet die aktuelle Position des Wiedergabekopfes.
    * Dieser Befehl positioniert den Cursor auch an der Position des Markers
      am Anfang von Auswahl B, während die Position dieses Markers gemeldet
      wird, sofern eine Auswahl getroffen wurde.
    * Meldet im Lautstärke-Dialogfeld den nächsten Wert, der generell mit
      Pfeil aufwärts erreicht werden kann.
    * Dieser Wert ist keine vokalisierte Voreinstellung.

* NVDA+A

    * Öffnet die Hilfe-Datei der Erweiterung.

## Kompatibilität ##

* Diese Erweiterung ist kompatibel mit den NVDA-Versionen von 2016.4 bis
  2019.1.

## Änderungen in Version 19.02 ##

* Das Konfigurationsdialog der Erweiterung wurde in das seit nvda 2018.2
  verfügbare Einstellungsfenster von NVDA verschoben;
* Die Versionsnummerierung wurde in JJ.MM geändert (das Jahr in 2 Ziffern,
  gefolgt von einem Punkt, gefolgt von dem Monat in 2 Ziffern);
* Die Kompatibilität mit dem neuen Versionierungsformat der Erweiterung
  wurde gesichert, erschienen seit nvda 2019.1.

## Änderungen in Version 4.0 ##

* Die Kompatibilität mit Python 2.7 und Python 3 wurde integriert;
* Ein Problem wurde behoben, welches bei Pfaden der Erweiterung mit
  Nicht-ASCII-Zeichen auftrat.

## Änderungen in Version 3.0 ##

* Das Modul gui.guiHelper wurde anbewendet, um das Konfigurationsdialog der
  Erweiterung korrekt anzuzeigen;
* Statt %s wurde Format für formatierte Strings eingesetzt;
* Die Übereinstimmung mit Implementierungsvorgaben wurde finalisiert.

## Änderungen in Version 2.3 ##

* Die Erweiterung verfügt nun über eine GPL-Lizenz;
* Wegen Inkompatibilität mit den letzten Versionen dieser Erweiterung wurde
  die Tastenkombination für das Skript, welches das Ende der Auswahl ansagt,
  von STRG+Umschalt+N zu STRG+Umschalt+E geändert;
* Ein Skript wurde eingefügt, welches das Abbrechen der Auswahl mit STRG+R
  bestätigt;
* Es wurden Einige Verbesserungen im Appmodul 'mp3directcut.py' vorgenommen.

## Änderungen in Version 2.2 ##

* Es wurden die Skripte verbessert, die die Position der Auswahlmarker
  ausgeben.

## Änderungen in Version 2.1.1 ##

* Das Skript, das die Gesamtzeit ausgibt, wurde entfernt. Die Information
  wird nun das Skript für die verstrichene Zeit mit ausgeben;
* Die Ansagen, die sich auf die Leertaste beziehen, können nun in den
  Einstellungen des Moduls unabhängig von anderen Ansagen aktiviert oder
  deaktiviert werden;
* Die Ankündigung der Platzierung von Auswahlmarkern können nun in den
  Einstellungen des Moduls aktiviert oder deaktiviert werden;
* Der aktuelle Abschnitt beim Durchlaufen der Schnittpunkte wird nun
  angesagt;
* Ansagen, die sich auf vertikale Schlüssel beziehen, wurden verbessert;
* Ein Skript wurde hinzugefügt, welches das Öffnen der Hilfe der aktuellen
  Erweiterung mit NVDA + H ermöglicht;
* Das Konfigurationsmenü der Erweiterung wurde aus dem Menü Extras in das
  Menü Einstellungen von NVDA verschoben.

## Änderungen in Version 2.1 ##

* Ein Script wurde hinzugefügt, um die Bewegung zum nächsten
  Orientierungspunkt mit STRG+Rechtspfeil auszusprechen;
* Ein Script wurde hinzugefügt, um die Bewegung zum vorherigen
  Orientierungspunkt mit STRG+Linkspfeil auszusprechen;
* Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
  Sekunden vorwärts mit Umschalt+Rechtspfeil anzusagen;
* Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
  Sekunden rückwärts mit Umschalt+Linkspfeil anzusagen;
* Kleine Verbesserungen des Titels.

## Änderungen in Version 2.0 ##

* Ein Skript wurde hinzugefügt, um die verstrichene Zeit mit STRG+Umschalt+R
  anzusagen;
* Das Vorlesen der Dauer (inkl. Stunden) wurde verbessert;
* Es besteht nun die Möglichkeit zwischen hundertstel und tausendstel
  Sekunden zu unterscheiden.

## Änderungen in Version 1.1 ##

* Es wurde die Möglichkeit hinzugefügt, die Kategorie mp3DirectCut im Dialog
  "Eingaben" aufzunehmen;

    * Sie sind nur während der Verwendung der mp3DirectCut-Software
      sichtbar.

* Es wurde die Möglichkeit hinzugefügt, automatische Benachrichtigungen im
  Extras-Menü von NVDA unter dem Eintrag "mp3DirectCut-Konfiguration" zu
  aktivieren oder zu deaktivieren;

## Änderungen in Version 1.0 ##

* Erste Version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
