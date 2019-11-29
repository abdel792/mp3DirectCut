# mp3DirectCut #

* Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Preuzmi [stabilnu verziju][1]
* Preuzmite [razvojnu verziju][2]

# Objašnjenje #

Ovaj dodatak poboljšava pristupačnost programa mp3DirectCut s NVDA čitačem.

Testiran je s mp3DirectCut inačicama 212 do 223.

## Tipkovni prečaci ##

Ovaj dodatak nudi sljedeće naredbe:

* B

    * Koristi se za potvrđivanje ispravnosti pozicije oznake za početak B
      odabira.

* Ctrl+Shift+B

    * Used to indicate the position of the marker of the beginning of
      selection B.
    * Double pressure lets give you the duration of the selection.

* Ctrl+Shift+D

    * Gives the duration from the beginning of the file to the current
      position of the playback cursor.
    * Double pressure lets give you the total duration.

* Ctrl+R

    * Potvrđuje da je odabir otkazan.

* Ctrl+Shift+R

    * Gives the time remaining from the current position of the playback
      cursor to the end of the file.

* Ctrl+Shift+E

    * Used to indicate the position of the marker of the end of selection N.
    * Double pressure gives recapitulatif positions B and N, and the
      duration of the selection.

* Ctrl+Shift+P

    * Give the reference of the actual part and the total number of parts in
      the current file.

* Ctrl+Shift+Space

    * Used to determine the current level of the vu-meter, during recording.
    * Double pressure reset it.

* Down Arrow

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of
      the end of selection N, while giving the location of this marker if a
      selection has been made.
    * In the volume dialog box, vocalise the next value that can be reached
      generally with downArrow.
    * This value is not vocalized default.

* End

    * Moves the playback cursor at the end of the current file and give the
      total time.

* Home

    * Moves the playback cursor at the beginning of the current file.

* Left Arrow

    * Lets make a brief return back of one second during playback, while
      giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* N

    * Koristi se za potvrđivanje ispravnosti pozicije oznake za kraj N
      odabira.

* Page Down

    * Lets make a leap forward of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Page Up

    * Lets make a return back of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* R

    * Allows to prepare a record and whether you can press spacebar to
      start.

* Right Arrow

    * Lets do a brief forward of one second during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Ctrl+Right Arrow

    * Moves to the next splitting point, while giving the current duration.

* Ctrl+Left Arrow

    * Moves to the previous splitting point, while giving the current
      duration.

* Shift+Right Arrow

    * Lets do a brief forward of four hundredths of seconds during playback,
      while giving the current duration.

* Shift+Left Arrow

    * Lets do a brief backwards of four hundredths of seconds during
      playback, while giving the current duration.

* S

    * Zaustavlja čitanje i daje trenutačno trajanje.

* Razmaknica

    * Ako je snimanje spremno, započni ovo snimanje.
    * Ako se snima, zaustavi snimanje postavljajući kursor na početak.
    * Ako je jedan datoteka učitana, započni čitati.
    * Ako se čita, omogućuje pauzu s davanjem trenutačnog trajanja.
    * Ako je čitanje pauzirano, omogućuje ponovno čitanje s trenutačne
      pozicije.

* Up Arrow

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of
      the beginning of selection B, while giving the location of this marker
      if a selection has been made.
    * In the volume dialog box, vocalise the previous value that can be
      reached generally with upArrow.
    * This value is not vocalized default.

* NVDA+H

    * Otvara pomoć trenutačnog dodatka.

## Kompatibilnost ##

* Dodatak je kompatibilan s NVDA verzijama 2016.4 do 2019.3.

## Promjene u inačici 19.02 ##

* Added the add-on's configuration in the settings panel available since
  nvda 2018.2;
* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

## Promjene u inačici 4.0 ##

* Dodana Kompatibilnost dodatka s Pythonom 2.7 i 3;
* Ispravljena je greška u dodatku koja je sadržavala znakove koji nisu
  ASCII.

## Promjene u inačici 3.0 ##

* Korišten je gui.guiHelper modul kako bi se potvrdio ispravan prikaz
  dijaloškog okvira konfiguracije dodatka;
* Korišten je format umjesto %s za formatirane stringove;
* Dodatak je izrađen sukladno smjernicama za implementaciju.

## Promjene u inačici 2.3 ##

* Dodana je GPL licenca u dodatak;
* Promijenjena je kratica za skriptu koja daje kraj odabira iz Kontrol +
  Šift + N u Kontrol + Šift + E jer Kontrol + Šift + N ne radi sa zadnjim
  inačicama mp3DirectCut;
* Dodana je skripta za potvrđivanje da je odabir otkazan sa 'Kontrol + r';
* Učinjene su neke ispravke u kodu appModula 'mp3directcut.py..

## Promjene u inačici 2.2 ##

* Ispravljene skripte koje daju lokacije odabranih markera.

## Promjene u inačici 2.1.1 ##

* Uklonjena skripta koja daje ukupno vrijeme a ta je informacija dodana u
  skriptu koja daje preostalo vrijeme;
* Dodana mogućnost omogućavanja ili onemogućavanja obavijesti vezanih uz
  tipku razmak u opcijama konfiguriranja modula, odvojeno od drugih
  obavijesti;
* Dodana mogućnost omogućavanja ili onemogućavanja najave postavljanja
  oznaka odabira u opcijama konfiguriranja modula;
* Dodano izgovaranje trenutnog dijela dok se krećete kroz izrezane točke;
* Ispravljene obavijesti vezanih uz vertikalne tipke;
* Dodana skripta za otvaranje pomoći trenutnog dodatka sa 'NVDA+H';
* Premješten je izbornik konfiguracije dodatka iz izbornika Alati u izbornik
  Postavki NVDA.

## Promjene u inačici 2.1 ##

* Dodana skripta za vokaliziranje prijelaza na sljedeću točku razdvajanja sa
  Kontrol+Strelicom desno;
* Dodana skripta za vokaliziranje prijelaza na prethodnu točku razdvajanja
  sa Kontrol+Strelicom lijevo;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unaprijed, sa
  Šift + strelicom desno;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unatrag, sa
  Šift+Strelicom lijevo;
* Ispravak sažetka dodatka iz 'za mp3DirectCut' u 'mp3DirectCut'.

## Promjene u inačici 2.0 ##

* Dodana skripta kako bi se saznalo preostalo vrijeme sa 'Kontrol Šift R';
* Poboljšan način čitanja trajanja uključujući sate;
* Dodana mogućnost razlikovanja tisućinki ili stotinki sekunde.

## Promjene u inačici 1.1 ##

* Added the ability to include the mp3DirectCut category into the Input
  Gestures;

    * They will be visible only during use of the mp3DirectCut software.

* Dodana mogućnost omogućavanja ili onemogućavanja automatskih poruka, u
  NVDA izborniku Alati, „mp3DirectCut konfiguracija”;

## Promjene u inačici 1.0 ##

* Inicijalna verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
