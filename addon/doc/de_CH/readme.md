# mp3DirectCut

* Autor(en): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Präsentation #

Dieses Add-on verbessert die Barrierefreiheit der Software mp3DirectCut mit NVDA.

Es wurde mit den Versionen von mp3DirectCut von 212 bis 233 getestet.

## Tastenkombinationen ##

Dieses Add-on bietet die folgenden Befehle:

* B

    * Bestätigt die korrekte Platzierung der Markierung für den Anfang der Auswahl B.

* Ctrl+Shift+B

    * Zeigt die Position der Markierung für den Anfang der Auswahl B an.
    * Zweimaliges Drücken gibt die Dauer der Auswahl aus.

* Ctrl+Shift+D

    * Gibt die Dauer vom Anfang der Datei bis zur aktuellen Position des Wiedergabecursors an.
    * Zweimaliges Drücken gibt die Gesamtdauer aus.

* Ctrl+R

    * Bestätigt, dass die Auswahl aufgehoben wurde.

* Ctrl+Shift+R

    * Gibt die verbleibende Zeit von der aktuellen Position des Wiedergabecursors bis zum Ende der Datei an.

* Ctrl+Shift+E

    * Zeigt die Position der Markierung für das Ende der Auswahl N an.
    * Zweimaliges Drücken gibt eine Zusammenfassung der Positionen B und N sowie die Dauer der Auswahl aus.

* Ctrl+Shift+P

    * Gibt die Nummer des aktuellen Teils und die Gesamtzahl der Teile in der aktuellen Datei an.

* Ctrl+Shift+Space

    * Bestimmt den aktuellen Pegel der Aussteuerungsanzeige während der Aufnahme.
    * Zweimaliges Drücken setzt diese zurück.

* Pfeiltaste unten

    * Zeigt die aktuelle Position des Wiedergabecursors an.
    * Dieser Befehl positioniert den Cursor auch an der Stelle der Markierung für das Ende der Auswahl N und gibt die Position dieser Markierung an, falls eine Auswahl getroffen wurde.
    * Spricht im Lautstärkedialog den nächsten Wert aus, der im Allgemeinen mit der Pfeiltaste unten erreicht werden kann.
    * Dieser Wert wird standardmässig nicht gesprochen.

* End

    * Bewegt den Wiedergabecursor an das Ende der aktuellen Datei und gibt die Gesamtzeit an.

* Home

    * Bewegt den Wiedergabecursor an den Anfang der aktuellen Datei.

* Pfeiltaste links

    * Springt während der Wiedergabe eine Sekunde zurück und gibt die aktuelle Dauer an.
    * Diese Dauer ist in den Optionen von mp3DirectCut konfigurierbar.

* N

    * Bestätigt die korrekte Platzierung der Markierung für das Ende der Auswahl N.

* Page Down

    * Springt während der Wiedergabe 10 Sekunden vorwärts und gibt die aktuelle Dauer an.
    * Diese Dauer ist in den Optionen von mp3DirectCut konfigurierbar.

* Page Up

    * Springt während der Wiedergabe 10 Sekunden zurück und gibt die aktuelle Dauer an.
    * Diese Dauer ist in den Optionen von mp3DirectCut konfigurierbar.

* R

    * Bereitet eine Aufnahme vor und teilt mit, ob die Leertaste zum Starten gedrückt werden kann.

* Pfeiltaste rechts

    * Springt während der Wiedergabe eine Sekunde vorwärts und gibt die aktuelle Dauer an.
    * Diese Dauer ist in den Optionen von mp3DirectCut konfigurierbar.

* Ctrl+Pfeiltaste rechts

    * Bewegt den Cursor zum nächsten Trennpunkt und gibt die aktuelle Dauer an.

* Ctrl+Pfeiltaste links

    * Bewegt den Cursor zum vorherigen Trennpunkt und gibt die aktuelle Dauer an.

* Shift+Pfeiltaste rechts

    * Springt während der Wiedergabe vier Hundertstelsekunden vorwärts und gibt die aktuelle Dauer an.

* Shift+Pfeiltaste links

    * Springt während der Wiedergabe vier Hundertstelsekunden zurück und gibt die aktuelle Dauer an.

* S

    * Stoppt die Wiedergabe und gibt die aktuelle Dauer an.

* Space

    * Wenn die Aufnahme bereit ist, startet sie diese Aufnahme.
    * Wenn eine Aufnahme läuft, stoppt sie diese und positioniert den Cursor am Anfang.
    * Wenn eine Datei geladen ist, startet sie die Wiedergabe.
    * Wenn eine Wiedergabe läuft, pausiert sie diese und gibt die aktuelle Dauer an.
    * Wenn die Wiedergabe pausiert ist, startet sie die Wiedergabe an der aktuellen Position neu.

* Pfeiltaste oben

    * Zeigt die aktuelle Position des Wiedergabecursors an.
    * Dieser Befehl positioniert den Cursor auch an der Stelle der Markierung für den Anfang der Auswahl B und gibt die Position dieser Markierung an, falls eine Auswahl getroffen wurde.
    * Spricht im Lautstärkedialog den vorherigen Wert aus, der im Allgemeinen mit der Pfeiltaste oben erreicht werden kann.
    * Dieser Wert wird standardmässig nicht gesprochen.

* NVDA+H

    * Öffnet die Hilfe des aktuellen Add-ons.

## Kompatibilität ##

* Dieses Add-on ist mit den Versionen von NVDA ab 2019.3 und höher kompatibel.

## Änderungen für 20240327.0.0

* Fehler behoben, der beim Neuladen von Plugins einen Protokollfehler verursachte, dank Rob aus der nvda-addons-Mailingliste;

## Änderungen für 20240326.0.0

* Kompatibilität für nvda-2024.1 aktualisiert;
* Download-Link aus der Readme entfernt, der Download-Link für zukünftige Updates wird nun nur noch über den Add-on-Store verfügbar sein.

## Änderungen für 20231229.0.0 ##

* Abwärtskompatible Implementierung zur Unterstützung des Modus "Sprechen auf Anforderung" hinzugefügt, der bald mit nvda-2024.1 verfügbar sein wird.

## Änderungen für 20231007.0.0 ##

* Nach dem Platzieren der Trennpunkte und dem Öffnen des Fensters für die Schneideigenschaften mit "Ctrl+N" wurde die Barrierefreiheit für den Titel dieses Fensters durch Angabe des Teilindexes hinzugefügt.
* Im Lesemodus wird nach dem Verschieben der Start- oder Endmarkierungen von Auswahlen mit den Tasten 1 bis 6 des alphanumerischen Blocks der automatische Start der Wiedergabe an der neuen Position hinzugefügt;
* Fehler behoben, der beim Abfragen der verbleibenden Zeit mit "Control+Shift+R" vom Anfang des Titels an auftrat.

## Änderungen für 20230728.0.0 ##

* Die flake8- und mypy-Regeln wurden auf den Code angewendet;
* Die minimal unterstützte NVDA-Version wurde auf 2019.3 geändert, um die in Python 3 eingeführten Annotationen zu unterstützen.

## Änderungen für 20230607.0.0 ##

* Die folgenden Workflows wurden hinzugefügt:
 * auto-update-translations - zur automatischen Aktualisierung von Übersetzungen aus dem Übersetzungssystem von NVDA.
 * release-on-tag..yaml: zum Erstellen und Veröffentlichen des Add-ons, sobald ein neuer Tag gepusht wird;
 * manual-release.yaml: zum manuellen Erstellen und Veröffentlichen neuer Versionen des Add-ons.
* Übersetzungen aktualisiert.

## Änderungen für Version 20230508.0.0 und höher ##

* Versionsnummer, minimale NVDA-Version und Download-Link gemäss den Konventionen/Anforderungen des Stores geändert.

## Änderungen für Version 20.12 ##

* Sprache während der Aufnahme und Wiedergabe für die neuesten Versionen von mp3DirectCut gestoppt;
* Das Lesen der verbleibenden Zeit für neue Versionen von NVDA unter Verwendung von Python 3 wurde korrigiert.

## Änderungen für Version 19.02 ##

* Die Konfiguration des Add-ons wurde im Einstellungsfenster hinzugefügt, das seit nvda 2018.2 verfügbar ist;
* Die Versionsnummerierung wurde auf JJ.MM geändert (das Jahr zweistellig, gefolgt von einem Punkt, gefolgt vom Monat zweistellig);
* Kompatibilität mit dem neuen Versionierungsformat für Add-ons hinzugefügt, das seit nvda 2019.1 existiert.

## Änderungen für Version 4.0 ##

* Kompatibilität des Add-ons sowohl mit Python 2.7 als auch mit 3 hinzugefügt;
* Fehler bei Add-on-Pfaden behoben, die Nicht-ASCII-Zeichen enthalten.

## Änderungen für Version 3.0 ##

* Das Modul gui.guiHelper wurde verwendet, um das korrekte Erscheinungsbild des Konfigurationsdialogs des Add-ons zu gewährleisten;
* format anstelle von %s für formatierte Zeichenketten verwendet;
* Einhaltung der Richtlinien für die Implementierung angewendet.

## Änderungen für Version 2.3 ##

* Die GPL-Lizenz wurde zum Add-on hinzugefügt;
* Die Tastenkombination des Skripts, das das Ende der Auswahl angibt, wurde von Ctrl + Shift + N auf Ctrl + Shift + E geändert, da Ctrl + Shift + N mit den neuesten Versionen von mp3DirectCut nicht funktioniert;
* Ein Skript wurde hinzugefügt, um zu bestätigen, dass die Auswahl mit 'Ctrl+r' aufgehoben wurde;
* Einige Korrekturen im Code des appModule 'mp3directcut.py' vorgenommen.

## Änderungen für Version 2.2 ##

* Korrektur der Skripte, die die Positionen der Auswahlmarkierungen angeben.

## Änderungen für Version 2.1.1 ##

* Das Skript für die Gesamtzeit wurde entfernt und diese Information zum Skript für die abgelaufene Zeit hinzugefügt;
* Die Möglichkeit hinzugefügt, die Ansagen bezüglich der Leertaste in den Konfigurationsoptionen des Moduls separat von anderen Ansagen zu aktivieren oder zu deaktivieren;
* Die Möglichkeit hinzugefügt, die Ansage der Platzierung der Auswahlmarkierungen in den Konfigurationsoptionen des Moduls zu aktivieren oder zu deaktivieren;
* Die Ansage des aktuellen Teils beim Bewegen durch die Trennpunkte wurde hinzugefügt;
* Korrektur der Ansagen bezüglich der vertikalen Tasten;
* Ein Skript zum Öffnen der Hilfe des aktuellen Add-ons mit 'NVDA+H' wurde hinzugefügt;
* Verschiebung des Konfigurationsmenüs des Add-ons vom Menü Werkzeuge in das Menü Einstellungen von NVDA.

## Änderungen für Version 2.1 ##

* Ein Skript zur Sprachausgabe beim Bewegen zum nächsten Trennpunkt mit Control+Pfeiltaste rechts wurde hinzugefügt;
* Ein Skript zur Sprachausgabe beim Bewegen zum vorherigen Trennpunkt mit Control+Pfeiltaste links wurde hinzugefügt;
* Ein Skript zur Sprachausgabe bei der Verschiebung von 4 Hundertstelsekunden vorwärts mit Shift+Pfeiltaste rechts wurde hinzugefügt;
* Ein Skript zur Sprachausgabe bei der Verschiebung von 4 Hundertstelsekunden zurück mit Shift+Pfeiltaste links wurde hinzugefügt;
* Korrektur der Zusammenfassung des Add-ons von 'for mp3DirectCut' zu 'mp3DirectCut'.

## Änderungen für Version 2.0 ##

* Ein Skript wurde hinzugefügt, um die verbleibende Zeit mit 'Control Shift R' abzufragen;
* Das Lesen von Zeitdauern einschliesslich Stunden wurde korrigiert;
* Die Möglichkeit hinzugefügt, zwischen Tausendsteln und Hundertsteln einer Sekunde zu unterscheiden.

## Änderungen für Version 1.1 ##

* Die Möglichkeit hinzugefügt, die Kategorie mp3DirectCut in die Eingabegesten aufzunehmen;

    * Sie sind nur während der Nutzung der mp3DirectCut-Software sichtbar.

* Die Möglichkeit hinzugefügt, automatische Meldungen im Werkzeuge-Menü von NVDA, Eintrag 'mp3DirectCut Konfiguration', zu aktivieren oder zu deaktivieren;

## Änderungen für Version 1.0 ##

* Initialversion.
