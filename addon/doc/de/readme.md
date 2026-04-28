# Mp3DirectCut

- Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Presentation

Diese Erweiterung verbessert die Zugänglichkeit von Mp3DirectCut mit NVDA.

Die Erweiterung wurde mit den mp3Direktcut-Versionen von 212 bis 223
getestet.

## Tastenkombinationen

Diese Erweiterung bietet folgende Tastaturbefehle:

- B

  - Wird verwendet, um die korrekte Platzierung des Markers am Anfang der
    Auswahl B zu bestätigen.

- STRG+Umschalt+B

  - Wird verwendet, um die Position des Markers vom Anfang der Auswahl B
    anzusagen.
  - Zweimaliges Drücken meldet die Dauer der Auswahl.

- STRG+Umschalt+D

  - Meldet die Dauer vom Anfang der Datei bis zur aktuellen Position des
    Wiedergabecursors.
  - Zeimaliges Drücken meldet die Gesamtdauer.

- STRG+R

  - Beschtätigt das Abbrechen der Auswahl.

- STRG+Umschalt+R

  - Meldet die Restzeit von der aktuellen Wiedergabeposition bis zum Ende
    der Datei.

- STRG+Umschalt+E

  - Wird verwendet, um die Position des Markers vom Ende der Auswahl N zu
    melden.
  - Zweimaliges Drücken wiederholt die Positionen B und N und die Dauer
    der Auswahl.

- STRG+Umschalt+P

  - Meldet die Referenz des aktuellen Abschnitts und die Gesamtzahl der
    Abschnitte in der aktuellen Datei.

- STRG+Umschalt+Leertaste

  - Wird verwendet, um den aktuellen Pegel des Vu-Meters während der
    Aufzeichnung zu bestimmen.
  - Zweimaliges Drücken setzt ihn zurück.

- Pfeil abwärts

  - Meldet die aktuelle Position des Wiedergabekopfes.
  - Dieser Befehl positioniert den Cursor auch an der Position des Markers
    am Ende der Auswahl N, während die Position dieses Markers gemeldet
    wird, sofern eine Auswahl getroffen wurde.
  - Meldet im Lautstärke-Dialogfeld den nächsten Wert, der generell mit
    Pfeil abwärts erreicht werden kann.
  - Dieser Wert ist keine vokalisierte Voreinstellung.

- Ende

  - Bewegt den Wiedergabecursor am Ende der aktuellen Datei und meldet die
    Gesamtdauer.

- Home

  - Bewegt den Wiedergabecursor an den Anfang der aktuellen Datei.

- Pfeil links

  - Springt während der Wiedergabe eine Sekunde rückwärts, während die
    aktuelle Dauer gemeldet wird.
  - Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

- N

  - Wird verwendet, um die korrekte Platzierung des Markers am Ende der
    Auswahl N zu bestätigen.

- Seite ab

  - Springt während der Wiedergabe 10 Sekunden vorwärts, während die
    aktuelle Dauer gemeldet wird.
  - Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

- Seite auf

  - Springt während der Wiedergabe 10 Sekunden rückwärts, während die
    aktuelle Dauer gemeldet wird.
  - Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

- R

  - Ermöglicht die Vorbereitung einer Aufnahme. Drücken Sie die Leertaste
    zum Starten.

- Pfeil rechts

  - Springt während der Wiedergabe eine Sekunde vorwärts, während die
    aktuelle Dauer gemeldet wird.
  - Diese Dauer ist in den Optionen von mp3directcut konfigurierbar.

- STRG+Pfeil rechts

  - Springt zum nächsten Aufteilungspunkt, wobei die aktuelle Dauer
    gemeldet wird.

- Ctrl+Left Arrow

  - Springt zum vorherigen Aufteilungspunkt, wobei die aktuelle Dauer
    gemeldet wird.

- Umschalt+Pfeil rechts

  - Springt während der Wiedergabe vierhundertstel Sekunden vorwärts,
    während die aktuelle Dauer gemeldet wird.

- Umschalt+Pfeil links

  - Springt während der Wiedergabe vierhundertstel Sekunden rückwärts,
    während die aktuelle Dauer gemeldet wird.

- S

  - Wird verwendet, um den Lesevorgang zu stoppen und die aktuelle Dauer
    zu melden.

- Space

  - Startet die Aufnahme, sofern diese vorbereitet ist.
  - Wenn eine Aufnahme läuft, wird sie gestoppt und der Cursor wird am
    Anfang positioniert.
  - Startet das Lesen, wenn eine Datei geladen ist.
  - Meldet die aktuelle Dauer und pausiert währenddessen das Lesen.
  - Wenn das Lesen angehalten wird, kann es von der aktuellen Position
    weiter ausgeführt werden.

- Pfeil aufwärts

  - Meldet die aktuelle Position des Wiedergabekopfes.
  - Dieser Befehl positioniert den Cursor auch an der Position des Markers
    am Anfang von Auswahl B, während die Position dieses Markers gemeldet
    wird, sofern eine Auswahl getroffen wurde.
  - Meldet im Lautstärke-Dialogfeld den nächsten Wert, der generell mit
    Pfeil aufwärts erreicht werden kann.
  - Dieser Wert ist keine vokalisierte Voreinstellung.

- NVDA+A

  - Lets open the help of the current add-on.

## Kompatibilität

- Diese NVDA-Erweiterung ist kompatibel ab NVDA-Version 2019.3.

## Changes for 20240327.0.0

- Fixed a bug that caused a log error when reloading plugins, thanks to Rob,
  from nvda-addons mailing list;

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Änderungen in 20231007.0.0

- Nach dem Platzieren der Schnittpunkte und dem Öffnen des Fensters
  "Schnitteigenschaften" mit "Strg+N", fügen Sie dem Titel dieses Fensters
  eine Zugänglichkeit hinzu, indem Sie den Teile-Index angeben.
- Im Lesemodus, nach dem Verschieben der Start- oder Endmarkierungen der
  Auswahlen mit den Tasten 1 bis 6 des alphanumerischen Pads, Hinzufügen des
  automatischen Lesestarts von der neuen Position;
- Fixed a bug that occurred when consulting the remaining time with "control+shift+r" from the beginning of the track.

## Änderungen in 20230728.0.0

- Code angepasst für Flake8- und MyPy-Regeln;
- Die minimal unterstützte NVDA-Version wurde auf 2019.3 geändert, um die in
  Python 3 eingeführten Annotationen zu unterstützen.

## Änderungen in 20230508.0.0 und neuer

- Added the following workflows:
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Änderung für Version 20.12

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Änderungen in Version 19.02

- Anhalten der Sprachausgabe während der Aufnahme und des Vorlesens für die
  neuesten Versionen von mp3directcut;
- Die verbleibende Lesezeit für neue NVDA-Versionen mit Python 3 wurde
  behoben.

## Change for version 19.02

- Das Konfigurationsdialog der Erweiterung wurde in das seit nvda 2018.2
  verfügbare Einstellungsfenster von NVDA verschoben;
- Die Versionsnummerierung wurde in JJ.MM geändert (das Jahr in 2 Ziffern,
  gefolgt von einem Punkt, gefolgt von dem Monat in 2 Ziffern);
- Die Kompatibilität mit dem neuen Versionierungsformat der Erweiterung
  wurde gesichert, erschienen seit nvda 2019.1.

## Änderungen in Version 3.0

- Die Kompatibilität mit Python 2.7 und Python 3 wurde integriert;
- Ein Problem wurde behoben, welches bei Pfaden der Erweiterung mit
  Nicht-ASCII-Zeichen auftrat.

## Änderungen in Version 2.3

- Das Modul gui.guiHelper wurde anbewendet, um das Konfigurationsdialog der
  Erweiterung korrekt anzuzeigen;
- Statt %s wurde Format für formatierte Strings eingesetzt;
- Used compliance with guidelines for implementation.

## Änderungen in Version 2.2

- Die Erweiterung verfügt nun über eine GPL-Lizenz;
- Changed the shortcut of the script giving the end of selection from Ctrl + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work with the latest versions of mp3DirectCut;
- Ein Skript wurde eingefügt, welches das Abbrechen der Auswahl mit STRG+R
  bestätigt;
- Es wurden Einige Verbesserungen im Appmodul 'mp3directcut.py' vorgenommen.

## Änderungen in Version 2.1.1

- Es wurden die Skripte verbessert, die die Position der Auswahlmarker
  ausgeben.

## Änderungen in Version 2.1

- Das Skript, das die Gesamtzeit ausgibt, wurde entfernt. Die Information
  wird nun das Skript für die verstrichene Zeit mit ausgeben;
- Die Ansagen, die sich auf die Leertaste beziehen, können nun in den
  Einstellungen des Moduls unabhängig von anderen Ansagen aktiviert oder
  deaktiviert werden;
- Die Ankündigung der Platzierung von Auswahlmarkern können nun in den
  Einstellungen des Moduls aktiviert oder deaktiviert werden;
- Der aktuelle Abschnitt beim Durchlaufen der Schnittpunkte wird nun
  angesagt;
- Ansagen, die sich auf vertikale Schlüssel beziehen, wurden verbessert;
- Ein Skript wurde hinzugefügt, welches das Öffnen der Hilfe der aktuellen
  Erweiterung mit NVDA + H ermöglicht;
- Das Konfigurationsmenü der Erweiterung wurde aus dem Menü Extras in das
  Menü Einstellungen von NVDA verschoben.

## Änderungen in Version 2.0

- Ein Script wurde hinzugefügt, um die Bewegung zum nächsten
  Orientierungspunkt mit STRG+Rechtspfeil auszusprechen;
- Ein Script wurde hinzugefügt, um die Bewegung zum vorherigen
  Orientierungspunkt mit STRG+Linkspfeil auszusprechen;
- Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
  Sekunden vorwärts mit Umschalt+Rechtspfeil anzusagen;
- Ein Skript wurde hinzugefügt, um die Verschiebung um vierhundertstel
  Sekunden rückwärts mit Umschalt+Linkspfeil anzusagen;
- Correction of the addon's summary from 'for mp3DirectCut' to 'mp3DirectCut'.

## Änderungen in Version 1.1

- Ein Skript wurde hinzugefügt, um die verstrichene Zeit mit STRG+Umschalt+R
  anzusagen;
- Das Vorlesen der Dauer (inkl. Stunden) wurde verbessert;
- Added ability to differentiate thousandths or hundredths of seconds.

## Änderungen in Version 1.0

- Es wurde die Möglichkeit hinzugefügt, die Kategorie mp3DirectCut im Dialog
  "Eingaben" aufzunehmen;

  - Sie sind nur während der Verwendung der mp3DirectCut-Software
    sichtbar.

- Es wurde die Möglichkeit hinzugefügt, automatische Benachrichtigungen im
  Extras-Menü von NVDA unter dem Eintrag "mp3DirectCut-Konfiguration" zu
  aktivieren oder zu deaktivieren;

## Änderungen in Version 4.0

- Erste Version.
