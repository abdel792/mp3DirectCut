# mp3DirectCut #

* Autori: Abdel, Rémy, Abdellah Zineddine, Jean-François COLAS
* Preuzmi [stabilnu verziju][1]
* Preuzmi [razvojnu verziju][2]

# Objašnjenje #

Ovaj dodatak poboljšava pristupanje programu mp3DirectCut s NVDA čitačem.

Testiran je s mp3DirectCut verzijama 212 do 223.

## Tipkovni prečaci ##

Ovaj dodatak nudi sljedeće naredbe:

* B

    * Koristi se za potvrđivanje ispravnosti položaja oznake za početak B
      odabira.

* Ctrl+Shift+B

    * Koristi se za označavanje položaja oznake za početak B odabira.
    * Dvostrukim pritiskom se dobiva trajanje odabira.

* Ctrl+Shift+D

    * Navodi trajanje od početka datoteke do trenutačnog položaja kursora
      reprodukcije.
    * Dvostrukim pritiskom se navodi ukupno trajanje.

* Ctrl+R

    * Potvrđuje da je odabir otkazan.

* Ctrl+Shift+R

    * Navodi preostalo vrijeme od trenutačnog položaja kursora reprodukcije
      do kraja datoteke.

* Ctrl+Shift+E

    * Koristi se za označavanje položaja oznake za kraj N odabira.
    * Dvostrukim pritiskom se navode položaji za B i N kao i trajanje
      odabira.

* Ctrl+Shift+P

    * Navedi referencu stvarnog dijela i ukupni broj dijelova u trenutačnoj
      datoteci.

* Ctrl+Shift+razmaknica

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

* Ctrl+strelica Desno

    * Premješta se na sljedeću točku podjele, uz istodobno navođenje
      trajanja.

* Ctrl+strelica Lijevo

    * Premješta se na prethodnu točku podjele, uz istodobno navođenje
      trajanja.

* Shift+strelica Desno

    * Omogućuje pomak naprijed od jedne stotinke sekunde tijekom
      reprodukcije, uz istodobno navođenje trajanja.

* Shift+strelica Lijevo

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

* Dodatak je kompatibilan s NVDA verzijama 2016.4 do 2019.3.

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
* Promijenjena je kratica za skriptu koja daje kraj odabira iz Kontrol +
  Šift + N u Kontrol + Šift + E jer Kontrol + Šift + N ne radi sa zadnjim
  inačicama mp3DirectCut;
* Dodana je skripta za potvrđivanje da je odabir otkazan sa 'Kontrol + r';
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

* Dodana skripta za vokaliziranje prijelaza na sljedeću točku razdvajanja sa
  Kontrol+Strelicom desno;
* Dodana skripta za vokaliziranje prijelaza na prethodnu točku razdvajanja
  sa Kontrol+Strelicom lijevo;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unaprijed, sa
  Šift + strelicom desno;
* Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unatrag, sa
  Šift+Strelicom lijevo;
* Ispravak sažetka dodatka iz 'za mp3DirectCut' u 'mp3DirectCut'.

## Promjene u verziji 2.0 ##

* Dodana skripta kako bi se saznalo preostalo vrijeme sa 'Kontrol Šift R';
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

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
