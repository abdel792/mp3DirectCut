# mp3DirectCut #

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Popis #

Doplnok upravuje prístupnosť aplikácie mp3DirectCut s NVDA.

Je testovaný s mp3DirectCut od verzie 212 do 223.

## Klávesové skratky ##

Dostupné sú tieto klávesové skratky:

* B

    * Umiestni počiatočnú značku.

* Ctrl+Shift+B

    * Oznámi pozíciu počiatočnej značky.
    * Stlačené dvakrát rýchlo za sebou oznámi celkový čas označeného úseku.

* Ctrl+Shift+D

    * Oznámi čas od začiatku súboru po kurzor.
    * Stlačené dvakrát rýchlo za sebou oznámi celkové trvanie súboru.

* Ctrl+R

    * Zruší výber.

* Ctrl+Shift+R

    * Oznámi zostávajúci čas od kurzora do konca súboru.

* Ctrl+Shift+E

    * Oznámi pozíciu koncovej značky.
    * Stlačené dvakrát rýchlo za sebou oznámi pozíciu počiatočnej, koncovej
      značky a celkový čas vybratého úseku.

* Ctrl+Shift+P

    * Oznámi číslo časti a počet častí v aktuálnom súbore.

* Ctrl+Shift+medzera

    * Prečíta maximálnu nameranú úroveň hlasitosti počas nahrávania.
    * Stlačené dvakrát rýchlo za sebou vynuluje meranie.

* šípka dole

    * Oznámi pozíciu prehrávacieho kurzora.
    * Takisto presunie kurzor na koncovú značku a oznámi pozíciu, ak bolo
      niečo vybraté.
    * V dialógu s nastavením hlasitosti povie nasledujúcu hodnotu.
    * Predvolene táto hodnota nie je oznamovaná.

* End

    * Presunie kurzor na koniec súboru a oznámi celkové trvanie nahrávky.

* Home

    * Presunie kurzor na začiatok súboru.

* ľavá šípka

    * vráti sa o sekundu späť a oznámi pozíciu kurzora.
    * Oznamovanie sa dá vypnúť a zapnúť v nastaveniach doplnku.

* N

    * Umiestni koncovú značku.

* Page Down

    * Prejde o 10 sekúnd dopredu a oznámi pozíciu kurzora.
    * Oznamovanie sa dá vypnúť a zapnúť v nastaveniach doplnku.

* Page Up

    * Vráti sa o 10 sekúnd a oznámi pozíciu kurzora.
    * Oznamovanie sa dá vypnúť a zapnúť v nastaveniach doplnku.

* R

    * Prepne do režimu nahrávania, kde je možné samotné nahrávanie spustiť
      medzerou.

* šípka doprava

    * Presunie kurzor o sekundu dopredu a oznámi pozíciu kurzora.
    * Oznamovanie sa dá vypnúť a zapnúť v nastaveniach doplnku.

* Ctrl+pravá šípka

    * Prejde na rozdelenie a oznámi čas.

* Ctrl+ľavá šípka

    * Prejde na predchádzajúce rozdelenie a oznámi pozíciu kurzora.

* Shift+pravá šípka

    * Preskočí o 4 stotiny sekundy dopredu a oznámi pozíciu kurzora.

* Shift+ľavá šípka

    * Prejde o 4 stotiny sekundy dozadu a oznámi pozíciu kurzora.

* S

    * Zastaví prehrávanie a povie pozíciu kurzora.

* Medzera

    * V režime nahrávania spustí nahrávanie.
    * Ak je už nahrávanie spustené, zastaví ho a presunie kurzor na začiatok
      nahrávky.
    * Ak je načítaný súbor, spustí prehrávanie.
    * Ak je spustené prehrávanie, pozastaví ho a povie aktuálnu pozíciu
      kurzora.
    * Ak je prehrávanie pozastavené, spustí prehrávanie od pozície kurzora.

* Šípka hore

    * Oznámi pozíciu prehrávacieho kurzora.
    * Presunie kurzor na počiatočnú značku a povie jej pozíciu.
    * V dialógu s nastavením hlasitosti prečíta predchádzajúcu dostupnú
      hodnotu.
    * Predvolene táto hodnota nie je oznamovaná.

* NVDA+H

    * Otvorí pomocníka pre doplnok.

## Kompatibilita ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

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

## Changes for 20231007.0.0 ##

* After placing the cutting points and after opening the cutting properties
  window, with "Ctrl+N", adding accessibility to the title of this window by
  indicating the part index.
* In reading mode, after moving the start or end markers of selections with
  keys 1 to 6 of the alphanumeric pad, addition of automatic start of
  reading from the new position;
* Fixed a bug that occurred when consulting the remaining time with
  "control+shift+r" from the beginning of the track.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Change for version 20.12 ##

* Stop speech during recording and reading for the latest versions of
  mp3directcut;
* Fixed reading remaining time for new versions of NVDA using Python 3.

## Verzia 19.2 ##

* Nastavenie doplnku presunuté do stromu s nastaveniami NVDA;
* Verzie sú číslované v tvare yy.mm (dve číslice pre rok, dve číslice pre
  mesiac);
* Pridaná podpora pre nové čísla verzii uvedené v NVDA 2č019.1.

## Verzia 4.0 ##

* Pridaná kompatibilita s prostredím Python 2.7 a 3;
* Opravené problémy, ktoré nastávali, ak boli v názvoch ciest znaky mimo
  ASCII rozsahu.

## Verzia 3.0 ##

* Používame nový modul gui.guiHelper na správne zobrazenie dialógu s
  nastavením;
* V prekladoch sa namiesto %s používa presnejšie pomenovanie premenných.
* Upravené podľa zásad a pravidiel doplnkov.

## Verzia 2.3 ##

* Pridaná GPL licencia;
* Skratka na zistenie koncovej značky zmenená z ctrl+shift+n na ctrl+shift+e
  lebo ctrl+shift+n nefunguje v posledných verziách mp3DirectCut;
* Pridaná skratka ctrl+r, ktorá oznámi zrušenie výberu;
* Drobné úpravy v aplikačnom module.

## Verzia 2.2 ##

* Opravené funkcie na zistenie pozície počiatočnej a koncovej značky.

## Verzia 2.1.1 ##

* Odstránená funkcia na oznámenie celkového času. Celkový čas teraz oznamuje
  funkcia na oznámenie uplynutého času.
* Pridaná možnosť výrečnosti pri stlačení medzerníka;
* Pridaná možnosť vypnúť a zapnúť oznamovanie umiestnenia značiek;
* Pridaná možnosť zapnúť a vypnúť oznamovanie čísla časti pri prechode cez
  rozdelenie;
* Opravené oznamovanie pri použití šípky hore a dole;
* Pridaný pomocník doplnku pod skratku nvda+h.
* Nastavenie doplnku presunuté z menu nástroje do menu nastavenia.

## Verzia 2.1 ##

* Pridané oznamovanie pri prechode na rozdelenie skratkou ctrl+pravá šípka;
* Pridané oznamovanie pri prechode na rozdelenie skratkou ctrl+ľavá šípka;
* Pridané oznamovanie pri pohybe skratkou shift+pravá šípka;
* Pridané oznamovanie pri pohybe skratkou shift+ľavá šípka;
* Opravený preklep v informácii o doplnku.

## Verzia 2.0 ##

* Skratka ctrl+shift+r oznamuje zostávajúci čas;
* Opravené čítanie času, teraz číta aj hodiny;
* Rozlišuje stotiny a tisíciny sekundy;

## Verzia 1.1 ##

* Pridaná kategória mp3DirectCut do dialógu klávesové skratky;

    * Zobrazí sa, len ak dialóg otvoríte z okna mp3DirectCut.

* Pridaná možnosť nastaviť výrečnosť;

## Verzia 1.0 ##

* Prvé vydanie.

[[!tag dev stable]]
