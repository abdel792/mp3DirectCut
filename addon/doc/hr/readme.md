# mp3DirectCut #

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Objašnjenje #

Ovaj dodatak poboljšava pristupanje programu mp3DirectCut s NVDA čitačem.

Testiran je s mp3DirectCut verzijama 212 do 223.

## Tipkovni prečaci ##

Ovaj dodatak nudi sljedeće naredbe:

* B

    * Koristi se za potvrđivanje ispravnosti položaja oznake za početak B
      odabira.

* Kontrol+šift+B

    * Koristi se za označavanje položaja oznake za početak B odabira.
    * Dvostrukim pritiskom se dobiva trajanje odabira.

* Kontrol+šift+D

    * Navodi trajanje od početka datoteke do trenutačnog položaja kursora
      reprodukcije.
    * Dvostrukim pritiskom se navodi ukupno trajanje.

* Kontrol+R

    * Potvrđuje da je odabir otkazan.

* Kontrol+šift+R

    * Navodi preostalo vrijeme od trenutačnog položaja kursora reprodukcije
      do kraja datoteke.

* Kontrol+šift+E

    * Koristi se za označavanje položaja oznake za kraj N odabira.
    * Dvostrukim pritiskom se navode položaji za B i N kao i trajanje
      odabira.

* Kontrol+šift+P

    * Navedi referencu stvarnog dijela i ukupni broj dijelova u trenutačnoj
      datoteci.

* Kontrol+šift+razmaknica

    * Koristi se za određivanje trenutačne razine vu-metra za vrijeme
      snimanja.
    * Dvostrukim pritiskom se resetira.

* Strelica dolje

    * Omogućuje prikaz trenutačnog položaja reprodukcije.
    * Ova naredba također smješta kursor na mjesto oznake kraja odabira N, a
      istodobno navodi položaj te oznake, ako je nešto odabrano.
    * U dijaloškom okviru glasnoće izgovori sljedeću vrijednost do koje se
      općenito može doći pomoću strelice Dolje.
    * Ova vrijednost se standardno ne izgovara.

* End

    * Premješta kusora za reprodukciju na kraj trenutačne datoteke i navodi
      ukupno vrijeme.

* Home

    * Premješta kusora za reprodukciju na početak trenutačne datoteke.

* Strelica lijevo

    * Omogućuje pomak natrag od jedne sekunde tijekom reprodukcije, uz
      istodobno navođenje trajanja.
    * Trajanje je moguće konfigurirati u opcijama za mp3directcut.

* N

    * Koristi se za potvrđivanje ispravnosti pozicije oznake za kraj N
      odabira.

* Page Down

    * Omogućuje pomak naprijed od deset sekundi tijekom reprodukcije, uz
      istodobno navođenje trajanja.
    * Trajanje je moguće konfigurirati u opcijama za mp3directcut.

* Page Up

    * Omogućuje pomak natrag od deset sekundi tijekom reprodukcije, uz
      istodobno navođenje trajanja.
    * Trajanje je moguće konfigurirati u opcijama za mp3directcut.

* R

    * Omogućuje pripremiti snimanje i odlučiti, hoće li se za pokretanje
      snimanja koristiti razmaknica.

* Strelica desno

    * Omogućuje pomak naprijed od jedne sekunde tijekom reprodukcije, uz
      istodobno navođenje trajanja.
    * Trajanje je moguće konfigurirati u opcijama za mp3directcut.

* Kontrol+strelica desno

    * Premješta se na sljedeću točku podjele, uz istodobno navođenje
      trajanja.

* Kontrol+strelica lijevo

    * Premješta se na prethodnu točku podjele, uz istodobno navođenje
      trajanja.

* Shift+strelica desno

    * Omogućuje pomak naprijed od jedne stotinke sekunde tijekom
      reprodukcije, uz istodobno navođenje trajanja.

* Shift+strelica lijevo

    * Omogućuje pomak natrag od jedne stotinke sekunde tijekom reprodukcije,
      uz istodobno navođenje trajanja.

* S

    * Zaustavlja čitanje i daje trenutačno trajanje.

* Razmaknica

    * Ako je snimanje spremno, započni ovo snimanje.
    * Ako se snima, zaustavi snimanje postavljajući kursor na početak.
    * Ako je jedan datoteka učitana, započni čitati.
    * Ako se čita, omogućuje pauzu s davanjem trenutačnog trajanja.
    * Ako je čitanje pauzirano, omogućuje ponovno čitanje s trenutačne
      pozicije.

* Strelica gore

    * Omogućuje prikaz trenutačnog položaja reprodukcije.
    * Ova naredba također smješta kursor na mjesto oznake početka odabira B,
      a istodobno navodi pložaj te oznake, ako je nešto odabrano.
    * U dijaloškom okviru glasnoće izgovori prethodnu vrijednost do koje se
      općenito može doći pomoću strelice Gore.
    * Ova vrijednost se standardno ne izgovara.

* NVDA+H

    * Otvara pomoć trenutačnog dodatka.

## Kompatibilnost ##

* Ovaj je dodatak kompatibilan s NVDA verzijom 2019.3 i novijim verzijama.

## Changes for 20240327.0.0

* Fixed a bug that caused a log error when reloading plugins, thanks to Rob,
  from nvda-addons mailing list;

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Promjene u 20231007.0.0 ##

* After placing the cutting points and after opening the cutting properties
  window, with "Ctrl+N", adding accessibility to the title of this window by
  indicating the part index.
* In reading mode, after moving the start or end markers of selections with
  keys 1 to 6 of the alphanumeric pad, addition of automatic start of
  reading from the new position;
* Fixed a bug that occurred when consulting the remaining time with
  "control+shift+r" from the beginning of the track.

## Promjene u 20230728.0.0 ##

* Programskom kodu su dodana flake8 i mypy pravila;
* Namjanja podržana NVDA verzija je promijenjena na 2019.3 kako bi se
  podržale zabilješke koje su uvedene u Python 3.

## Promjene u 20230508.0.0 i novijim verzijama ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Promjene u verziji 20.12 ##

* Zaustavi govor tijekom snimanja i čitanja za najnovije verzije
  mp3directcut-a;
* Ispravljeno je čitanje preostalog vremena za nove NVDA verzije pomoću
  Pythona 3.

## Promjene u verziji 19.02 ##

* Dodana je konfiguracija dodatka na ploči s postavkama koja je dostupna od
  nvda verzije 2018.2;
* Promijenjeno je numeriranje verzija koristeći YY.MM (Dvije znamenke za
  godinu, slijedi točka, a zatim dvije znamenke za mjesec);
* Dodana je kompatibilnost s novim formatom za određivanje verzije, pojavila
  se u nvda 2019.1.

## Promjene u verziji 4.0 ##

* Dodana Kompatibilnost dodatka s Pythonom 2.7 i 3;
* Ispravljena je greška u dodatku koja je sadržavala znakove koji nisu
  ASCII.

## Promjene u verziji 3.0 ##

* Korišten je gui.guiHelper modul kako bi se potvrdio ispravan prikaz
  dijaloškog okvira konfiguracije dodatka;
* Korišten je format umjesto %s za formatirane stringove;
* Dodatak je izrađen sukladno smjernicama za implementaciju.

## Promjene u verziji 2.3 ##

* Dodana je GPL licenca u dodatak;
* Promijenjen je prečac za skriptu koja daje kraj odabira, iz Kontrol+Šift+N
  u Kontrol+Šift+E, jer Kontrol+Šift+N ne radi sa zadnjim mp3DirectCut
  verzijama;
* Dodana je skripta za potvrđivanje da je odabir otkazan sa 'Kontrol+r';
* Učinjene su neke ispravke u kodu appModula 'mp3directcut.py..

## Promjene u verziji 2.2 ##

* Ispravljene skripte koje daju lokacije odabranih markera.

## Promjene u verziji 2.1.1 ##

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

## Promjene u verziji 2.1 ##

* Dodana skripta za vokaliziranje prijelaza na sljedeću točku razdvajanja s
  kontrol+strelica desno;
* Dodana skripta za vokaliziranje prijelaza na prethodnu točku razdvajanja s
  kontrol+strelica lijevo;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unaprijed, sa
  šift+strelica desno;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unatrag, sa
  šift+strelica lijevo;
* Ispravak sažetka dodatka iz 'za mp3DirectCut' u 'mp3DirectCut'.

## Promjene u verziji 2.0 ##

* Dodana je skripta, kako bi se saznalo preostalo vrijeme s 'kontrol šift
  R';
* Poboljšan način čitanja trajanja uključujući sate;
* Dodana mogućnost razlikovanja tisućinki ili stotinki sekunde.

## Promjene u verziji 1.1 ##

* Dodana je mogućnost uvrštavanja mp3DirectCut kategorije u Ulazne geste;

    * Oni će biti vidljivi samo tijekom korištenja softvera mp3DirectCut.

* Dodana mogućnost omogućavanja ili onemogućavanja automatskih poruka, u
  NVDA izborniku Alati, „mp3DirectCut konfiguracija”;

## Promjene u verziji 1.0 ##

* Prva verzija.

[[!tag dev stable]]
