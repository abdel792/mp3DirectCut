# mp3DirectCut

* Autor(en): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Vorstellung #

Dieses Add-on verbessert die Zugänglichkeit der Software mp3DirectCut mit NVDA.

Es wurde mit den Versionen 212 bis 233 von mp3DirectCut getestet.

## Tastenkombinationen ##

Dieses Add-on bietet die folgenden Befehle:

* B

    * Dient zum Bestätigen der korrekten Positionierung der Markierung für den Anfang der Auswahl B.

* Ctrl+Shift+B

    * Gibt die Position der Markierung für den Anfang der Auswahl B aus.
    * Zweimaliges Drücken gibt die Dauer der Auswahl aus.

* Ctrl+Shift+D

    * Gibt die Dauer vom Beginn der Datei bis zur aktuellen Position des Wiedergabecursors aus.
    * Zweimaliges Drücken gibt die Gesamtdauer aus.

* Ctrl+R

    * Bestätigt, dass die Auswahl aufgehoben wurde.

* Ctrl+Shift+R

    * Gibt die verbleibende Zeit von der aktuellen Position des Wiedergabecursors bis zum Ende der Datei aus.

* Ctrl+Shift+E

    * Gibt die Position der Markierung für das Ende der Auswahl N aus.
    * Zweimaliges Drücken gibt die Positionen der Markierungen B und N sowie die Dauer der Auswahl aus.

* Ctrl+Shift+P

    * Gibt die Nummer des aktuellen Abschnitts sowie die Gesamtzahl der Abschnitte in der aktuellen Datei aus.

* Ctrl+Shift+Space

    * Dient zum Ermitteln des aktuellen Pegels des VU-Meters während der Aufnahme.
    * Zweimaliges Drücken setzt den Wert zurück.

* Down Arrow

    * Gibt die aktuelle Position des Wiedergabecursors aus.
    * Dieser Befehl setzt den Cursor außerdem auf die Position der Endmarkierung N und gibt deren Position aus, sofern eine Auswahl vorhanden ist.
    * Im Lautstärke-Dialog wird der nächste Wert ausgegeben, der normalerweise mit der Pfeiltaste nach unten erreicht werden kann.
    * Dieser Wert wird standardmäßig nicht ausgegeben.

* End

    * Bewegt den Wiedergabecursor an das Ende der aktuellen Datei und gibt die Gesamtdauer aus.

* Home

    * Bewegt den Wiedergabecursor an den Anfang der aktuellen Datei.

* Left Arrow

    * Springt während der Wiedergabe eine Sekunde zurück und gibt die aktuelle Zeit aus.
    * Diese Dauer kann in den Optionen von mp3DirectCut konfiguriert werden.

* N

    * Dient zum Bestätigen der korrekten Positionierung der Markierung für das Ende der Auswahl N.

* Page Down

    * Springt während der Wiedergabe 10 Sekunden vor und gibt die aktuelle Zeit aus.
    * Diese Dauer kann in den Optionen von mp3DirectCut konfiguriert werden.

* Page Up

    * Springt während der Wiedergabe 10 Sekunden zurück und gibt die aktuelle Zeit aus.
    * Diese Dauer kann in den Optionen von mp3DirectCut konfiguriert werden.

* R

    * Bereitet eine Aufnahme vor und teilt mit, dass die Leertaste zum Starten gedrückt werden kann.

* Right Arrow

    * Springt während der Wiedergabe eine Sekunde vor und gibt die aktuelle Zeit aus.
    * Diese Dauer kann in den Optionen von mp3DirectCut konfiguriert werden.

* Ctrl+Right Arrow

    * Springt zum nächsten Trennpunkt und gibt die aktuelle Zeit aus.

* Ctrl+Left Arrow

    * Springt zum vorherigen Trennpunkt und gibt die aktuelle Zeit aus.

* Shift+Right Arrow

    * Springt während der Wiedergabe vier Hundertstelsekunden vor und gibt die aktuelle Zeit aus.

* Shift+Left Arrow

    * Springt während der Wiedergabe vier Hundertstelsekunden zurück und gibt die aktuelle Zeit aus.

* S

    * Stoppt die Wiedergabe und gibt die aktuelle Zeit aus.

* Space

    * Startet die Aufnahme, wenn diese vorbereitet wurde.
    * Stoppt eine laufende Aufnahme und setzt den Cursor an den Anfang zurück.
    * Startet die Wiedergabe, wenn eine Datei geladen ist.
    * Pausiert die Wiedergabe und gibt die aktuelle Zeit aus, wenn die Wiedergabe läuft.
    * Setzt die Wiedergabe an der aktuellen Position fort, wenn sie pausiert wurde.

* Up Arrow

    * Gibt die aktuelle Position des Wiedergabecursors aus.
    * Dieser Befehl setzt den Cursor außerdem auf die Position der Anfangsmarkierung B und gibt deren Position aus, sofern eine Auswahl vorhanden ist.
    * Im Lautstärke-Dialog wird der vorherige Wert ausgegeben, der normalerweise mit der Pfeiltaste nach oben erreicht werden kann.
    * Dieser Wert wird standardmäßig nicht ausgegeben.

* NVDA+H

    * Öffnet die Hilfe für das aktuelle Add-on.

## Kompatibilität ##

* Dieses Add-on ist mit NVDA-Versionen ab 2019.3 kompatibel.

## Änderungen für 20240327.0.0

* Ein Fehler wurde behoben, der beim Neuladen von Plugins einen Protokollfehler verursachte; danke an Rob von der Mailingliste nvda-addons.

## Änderungen für 20240326.0.0

* Die Kompatibilität mit nvda-2024.1 wurde aktualisiert.;
* Der Download-Link wurde aus der Readme-Datei entfernt. Der Download-Link für zukünftige Aktualisierungen ist künftig nur noch über den Add-on-Store verfügbar.

## Änderungen für 20231229.0.0 ##

* Eine abwärtskompatible Implementierung zur Unterstützung des Modus „Sprechen auf Anforderung“ (Speak on Demand) wurde hinzugefügt, der in nvda-2024.1 verfügbar sein wird.

## Änderungen für 20231007.0.0 ##

* Nach dem Setzen der Schnittmarken und dem Öffnen des Fensters mit den Schnitteigenschaften über "Ctrl+N" wurde die Zugänglichkeit des Fenstertitels verbessert, indem die Nummer des Abschnitts ausgegeben wird.
* Im Wiedergabemodus wird nach dem Verschieben der Start- oder Endmarkierung einer Auswahl mit den Tasten 1 bis 6 des Nummernblocks die Wiedergabe automatisch an der neuen Position gestartet.
* Ein Fehler wurde behoben, der beim Abfragen der verbleibenden Zeit mit "Control+Shift+R" vom Anfang des Titels auftrat.

## Änderungen für 20230728.0.0 ##

* Die Regeln von flake8 und mypy wurden auf den Quellcode angewendet;
* Die mindestens unterstützte NVDA-Version wurde auf 2019.3 angehoben, um die mit Python 3 eingeführten Annotationen zu unterstützen.

## Änderungen für 20230607.0.0 ##

* Die folgenden Workflows wurden hinzugefügt:
 * auto-update-translations – zum automatischen Aktualisieren der Übersetzungen aus dem Übersetzungssystem von NVDA.
 * release-on-tag..yaml: zum Erstellen und Veröffentlichen des Add-ons, sobald ein neues Tag erstellt wird;
 * manual-release.yaml: zum manuellen Erstellen und Veröffentlichen neuer Versionen des Add-ons.
* Die Übersetzungen wurden aktualisiert.

## Änderungen für Version 20230508.0.0 und neuer ##

* • Versionsnummer, Mindestversion von NVDA und Download-Link wurden entsprechend den Vorgaben des Add-on-Stores geändert.

## Änderungen für Version 20.12 ##

* Sprachausgabe während der Aufnahme und Wiedergabe für die neuesten Versionen von mp3DirectCut deaktiviert;
* Die Ausgabe der verbleibenden Zeit für neue NVDA-Versionen mit Python 3 wurde korrigiert.

## Änderungen für Version 19.02 ##

* Die Konfiguration des Add-ons wurde zum Einstellungsdialog hinzugefügt, der seit NVDA 2018.2 verfügbar ist;
* Das Versionsschema wurde auf YY.MM geändert (zweistellige Jahreszahl, gefolgt von einem Punkt und einer zweistelligen Monatszahl);
* Kompatibilität mit dem neuen Versionsformat für Add-ons, das seit NVDA 2019.1 verwendet wird, wurde hinzugefügt.

## Änderungen für Version 4.0 ##

* Kompatibilität des Add-ons mit Python 2.7 und Python 3 wurde hinzugefügt;
* Ein Fehler bei Add-on-Pfaden mit Nicht-ASCII-Zeichen wurde behoben.

## Änderungen für Version 3.0 ##

* Das Modul gui.guiHelper wird verwendet, um die korrekte Darstellung des Konfigurationsdialogs des Add-ons sicherzustellen;
* Für formatierte Zeichenketten wird nun format anstelle von %s verwendet;
* Die Implementierung wurde an die Entwicklungsrichtlinien angepasst.

## Änderungen in Version 2.3 ##

* Die GPL-Lizenz wurde zum Add-on hinzugefügt;
* Die Tastenkombination des Skripts zur Ausgabe des Endes der Auswahl wurde von Ctrl + Shift + N auf Ctrl + Shift + E geändert, da Ctrl + Shift + N mit den neuesten Versionen von mp3DirectCut nicht funktioniert;
* Ein Skript wurde hinzugefügt, das mit 'Ctrl+R' bestätigt, dass die Auswahl aufgehoben wurde;
* Einige Korrekturen am Code des App-Moduls 'mp3directcut.py' wurden vorgenommen.

## Änderungen in Version 2.2 ##

* Korrektur der Skripte, welche die Positionen der Auswahlmarkierungen ausgeben.

## Änderungen in Version 2.1.1 ##

* Das Skript zur Ausgabe der Gesamtdauer wurde entfernt und diese Information stattdessen in das Skript zur Ausgabe der verstrichenen Zeit integriert;
* Es wurde eine Möglichkeit hinzugefügt, die Ansagen im Zusammenhang mit der Leertaste unabhängig von den übrigen Ansagen in den Einstellungen des Moduls zu aktivieren oder zu deaktivieren;
* Es wurde eine Möglichkeit hinzugefügt, die Ansagen über die Platzierung der Auswahlmarkierungen in den Einstellungen des Moduls zu aktivieren oder zu deaktivieren;
* Die Ansage des aktuellen Abschnitts beim Wechsel zwischen den Trennpunkten wurde hinzugefügt;
* Korrektur der Ansagen für die Pfeiltasten;
* Ein Skript zum Öffnen der Hilfe des aktuellen Add-ons mit 'NVDA+H' wurde hinzugefügt;
* Das Konfigurationsmenü des Add-ons wurde vom Menü „Extras“ in das Menü „Einstellungen“ von NVDA verschoben.

## Änderungen in Version 2.1 ##

* Ein Skript zur Ausgabe des Wechsels zum nächsten Trennpunkt mit Control+Right Arrow wurde hinzugefügt;
* Ein Skript zur Ausgabe des Wechsels zum vorherigen Trennpunkt mit Control+Left Arrow wurde hinzugefügt;
* Ein Skript zur Ausgabe eines Sprungs um vier Hundertstelsekunden vorwärts mit Shift+Right Arrow wurde hinzugefügt;
* Ein Skript zur Ausgabe eines Sprungs um vier Hundertstelsekunden rückwärts mit Shift+Left Arrow wurde hinzugefügt;
* Die Kurzbeschreibung des Add-ons wurde von 'for mp3DirectCut' in 'mp3DirectCut' geändert.

## Änderungen in Version 2.0 ##

* Ein Skript zur Ausgabe der verbleibenden Zeit mit 'Control Shift R' wurde hinzugefügt;
* Die Ausgabe von Zeitangaben mit Stunden wurde korrigiert;
* Es wurde die Möglichkeit hinzugefügt, Tausendstel- und Hundertstelsekunden zu unterscheiden.

## Änderungen in Version 1.1 ##

* Es wurde die Möglichkeit hinzugefügt, die Kategorie „mp3DirectCut“ in die „Eingabegesten“ aufzunehmen;

    * Sie ist nur sichtbar, wenn die Software mp3DirectCut verwendet wird.

* Es wurde die Möglichkeit hinzugefügt, automatische Ansagen über den Menüpunkt „mp3DirectCut-Konfiguration“ im Menü „Extras“ von NVDA zu aktivieren oder zu deaktivieren;

## Änderungen in Version 1.0 ##

* Erste Version.
