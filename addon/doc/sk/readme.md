# mp3DirectCut

* Autor(i): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Prezentácia #

Doplnok zlepšuje prístupnosť programu mp3DirectCut v kombinácii s čítačkou obrazovky NVDA.

Bol testovaný s verziami programu mp3DirectCut od 212 do 233.

## Klávesové skratky ##

Tento doplnok ponúka nasledujúce príkazy:

* B

    * Slúži na potvrdenie správneho umiestnenia značky začiatku výberu B.

* Ctrl+Shift+B

    * Slúži na označenie pozície značky začiatku výberu B.
    * Dvojité stlačenie umožňuje zistiť trvanie výberu.

* Ctrl+Shift+D

    * Uvádza trvanie od začiatku súboru po aktuálnu pozíciu kurzora prehrávania.
    * Dvojité stlačenie umožňuje zistiť celkové trvanie.

* Ctrl+R

    * Potvrdzuje, že výber bol zrušený.

* Ctrl+Shift+R

    * Uvádza zostávajúci čas od aktuálnej pozície kurzora prehrávania po koniec súboru.

* Ctrl+Shift+E

    * Slúži na označenie pozície značky konca výberu N.
    * Dvojité stlačenie zobrazí súhrn pozícií B a N a trvanie výberu.

* Ctrl+Shift+P

    * Uvádza číslo aktuálnej časti a celkový počet častí v otvorenom súbore.

* Ctrl+Shift+Space

    * Slúži na určenie aktuálnej úrovne indikátora hlasitosti (VU metra) počas nahrávania.
    * Dvojité stlačenie ho resetuje.

* Šípka nadol

    * Umožňuje skontrolovať aktuálnu pozíciu kurzora prehrávania.
    * Tento príkaz tiež nastaví kurzor na miesto značky konca výberu N, pričom zároveň oznámi pozíciu tejto značky, ak bol vytvorený výber.
    * V dialógovom okne hlasitosti prečíta nasledujúcu hodnotu, ktorú možno vo všeobecnosti dosiahnuť šípkou nadol.
    * Táto hodnota sa predvolene nečíta.

* End

    * Presunie kurzor prehrávania na koniec aktuálneho súboru a oznámi celkový čas.

* Home

    * Presunie kurzor prehrávania na začiatok aktuálneho súboru.

* Šípka vľavo

    * Umožňuje krátky návrat späť o jednu sekundu počas prehrávania, pričom oznámi aktuálny čas.
    * Tento čas je možné nakonfigurovať v nastaveniach programu mp3DirectCut.

* N

    * Slúži na potvrdenie správneho umiestnenia značky konca výberu N.

* Page Down

    * Umožňuje skočiť dopredu o 10 sekúnd počas prehrávania, pričom oznámi aktuálny čas.
    * Tento čas je možné nakonfigurovať v nastaveniach programu mp3DirectCut.

* Page Up

    * Umožňuje návrat späť o 10 sekúnd počas prehrávania, pričom oznámi aktuálny čas.
    * Tento čas je možné nakonfigurovať v nastaveniach programu mp3DirectCut.

* R

    * Umožňuje pripraviť nahrávanie a informuje, či môžete stlačiť medzerník na spustenie.

* Šípka vpravo

    * Umožňuje krátky posun dopredu o jednu sekundu počas prehrávania, pričom oznámi aktuálny čas.
    * Tento čas je možné nakonfigurovať v nastaveniach programu mp3DirectCut.

* Ctrl+Šípka vpravo

    * Presunie na nasledujúci bod rozdelenia, pričom oznámi aktuálny čas.

* Ctrl+Šípka vľavo

    * Presunie na predchádzajúci bod rozdelenia, pričom oznámi aktuálny čas.

* Shift+Šípka vpravo

    * Umožňuje krátky posun dopredu o štyri stotiny sekundy počas prehrávania, pričom oznámi aktuálny čas.

* Shift+Šípka vľavo

    * Umožňuje krátky návrat späť o štyri stotiny sekundy počas prehrávania, pričom oznámi aktuálny čas.

* S

    * Slúži na zastavenie prehrávania a oznámenie aktuálneho času.

* Space

    * Ak je nahrávanie pripravené, spustí proces nahrávania.
    * Ak prebieha nahrávanie, zastaví ho a nastaví kurzor na začiatok.
    * Ak je súbor načítaný, spustí prehrávanie.
    * Ak prebieha prehrávanie, umožní ho pozastaviť (pauza) a oznámi aktuálny čas.
    * Ak je prehrávanie pozastavené, umožní ho obnoviť od aktuálneho miesta.

* Šípka nahor

    * Umožňuje skontrolovať aktuálnu pozíciu kurzora prehrávania.
    * Tento príkaz tiež nastaví kurzor na miesto značky začiatku výberu B, pričom zároveň oznámi pozíciu tejto značky, ak bol vytvorený výber.
    * V dialógovom okne hlasitosti prečíta predchádzajúcu hodnotu, ktorú možno vo všeobecnosti dosiahnuť šípkou nahor.
    * Táto hodnota sa predvolene nečíta.

* NVDA+H

    * Umožňuje otvoriť pomocníka pre aktuálny doplnok.

## Kompatibilita ##

* Tento doplnok je kompatibilný s verziami NVDA od 2019.3 a novšími.

## Zmeny v 20240327.0.0

* Opravená chyba, ktorá spôsobovala chybu v logu pri opätovnom načítaní doplnkov, vďaka Robovi z e-mailovej konferencie nvda-addons;

## Zmeny v 20240326.0.0

* Aktualizovaná kompatibilita pre nvda-2024.1.;
* Odstránený odkaz na stiahnutie zo súboru readme, odkaz na stiahnutie budúcich aktualizácií bude teraz dostupný výhradne v obchode s doplnkami (add-on store).

## Zmeny v 20231229.0.0 ##

* Pridaná spätne kompatibilná implementácia podporujúca režim reči na vyžiadanie, ktorý bude čoskoro dostupný v nvda-2024.1.

## Zmeny v 20231007.0.0 ##

* Po umiestnení bodov strihu a otvorení okna vlastností strihu pomocou „Ctrl+N“ bola pridaná prístupnosť k názvu tohto okna uvádzaním indexu časti.
* V režime čítania bola po presunutí značiek začiatku alebo konca výberu pomocou klávesov 1 až 6 na alfanumerickej klávesnici pridaná funkcia automatického spustenia prehrávania od novej pozície;
* Opravená chyba, ktorá sa vyskytovala pri zisťovaní zostávajúceho času pomocou „control+shift+r“ od začiatku skladby.

## Zmeny v 20230728.0.0 ##

* Na kód boli aplikované pravidlá flake8 a mypy;
* Zmenená minimálna podporovaná verzia NVDA na 2019.3 z dôvodu podpory anotácií zavedených v Pythone 3.

## Zmeny v 20230607.0.0 ##

* Pridané nasledujúce pracovné postupy (workflows):
 * auto-update-translations - na automatickú aktualizáciu prekladov zo systému prekladov NVDA.
 * release-on-tag..yaml: na zostavenie a publikovanie doplnku hneď, ako je odoslaná nová značka (tag);
 * manual-release.yaml: na manuálne zostavenie a vydávanie nových verzií doplnku.
* Aktualizované preklady.

## Zmeny vo verzii 20230508.0.0 a novších ##

* Zmenené číslo verzie, minimálna verzia NVDA a odkaz na stiahnutie v súlade s konvenciami/požiadavkami obchodu.

## Zmeny vo verzii 20.12 ##

* Zastavenie reči počas nahrávania a prehrávania v najnovších verziách mp3DirectCut;
* Opravené čítanie zostávajúceho času pre nové verzie NVDA využívajúce Python 3.

## Zmeny vo verzii 19.02 ##

* Pridaná konfigurácia doplnku v paneli nastavení, ktorý je dostupný od verzie nvda 2018.2;
* Zmenené číslovanie verzií na formát RR.MM (rok zapísaný pomocou 2 číslic, bodka, mesiac zapísaný pomocou 2 číslic);
* Pridaná kompatibilita s novým formátom verzií doplnkov, ktorý sa objavil od verzie nvda 2019.1.

## Zmeny vo verzii 4.0 ##

* Pridaná kompatibilita doplnku s Pythonom 2.7 aj 3;
* Opravená chyba s cestami doplnku, ktoré obsahovali iné ako ASCII znaky.

## Zmeny vo verzii 3.0 ##

* Použitý modul gui.guiHelper na zabezpečenie správneho vzhľadu dialógového okna konfigurácie doplnku;
* Použitá metóda format namiesto %s pre formátované reťazce;
* Uplatnený súlad s pokynmi pre implementáciu.

## Zmeny vo verzii 2.3 ##

* Do doplnku bola pridaná licencia GPL;
* Zmenená skratka skriptu uvádzajúceho koniec výberu z Ctrl + Shift + N na Ctrl + Shift + E, pretože Ctrl + Shift + N v najnovších verziách mp3DirectCut nefunguje;
* Pridaný skript na potvrdenie zrušenia výberu pomocou 'Ctrl+r';
* Vykonaných niekoľko opráv v kóde appModule 'mp3directcut.py'.

## Zmeny vo verzii 2.2 ##

* Oprava skriptov uvádzajúcich pozície značiek výberu.

## Zmeny vo verzii 2.1.1 ##

* Odstránenie skriptu uvádzajúceho celkový čas a pridanie tejto informácie do skriptu, ktorý uvádza uplynutý čas;
* Pridaná možnosť zapnúť alebo vypnúť oznamovanie spojené s medzerníkom v nastaveniach konfigurácie modulu, nezávisle od iných oznámení;
* Pridaná možnost zapnúť alebo vypnúť oznamovanie umiestnenia značiek výberu v nastaveniach konfigurácie modulu;
* Pridané oznamovanie aktuálnej časti pri pohybe po bodoch rozdelenia;
* Oprava oznamovania spojeného s vertikálnymi klávesmi;
* Pridaný skript na otvorenie pomocníka pre aktuálny doplnok pomocou 'NVDA+H';
* Presunuté menu konfigurácie doplnku z menu Nástroje do menu Možnosti v NVDA.

## Zmeny vo verzii 2.1 ##

* Pridaný skript na oznamovanie presunu na nasledujúci bod rozdelenia pomocou Control+Šípka vpravo;
* Pridaný skript na oznamovanie presunu na predchádzajúci bod rozdelenia pomocou Control+Šípka vľavo;
* Pridaný skript na oznamovanie posunu o 4 stotiny sekundy dopredu pomocou Shift+Šípka vpravo;
* Pridaný skript na oznamovanie posunu o 4 stotiny sekundy dozadu pomocou Shift+Šípka vľavo;
* Opravený súhrn doplnku z 'for mp3DirectCut' na 'mp3DirectCut'.

## Zmeny vo verzii 2.0 ##

* Pridaný skript na zistenie zostávajúceho času pomocou 'Control Shift R';
* Opravené čítanie trvania obsahujúceho hodiny;
* Pridaná možnosť rozlíšiť tisíciny alebo stotiny sekundy.

## Zmeny vo verzii 1.1 ##

* Pridaná možnosť zahrnúť kategóriu mp3DirectCut do klávesových skratiek (Input Gestures);

    * Budú viditeľné iba počas používania programu mp3DirectCut.

* Pridaná možnosť zapnúť alebo vypnúť automatické oznámenia v menu nástrojov NVDA, položka 'Nastavenie mp3DirectCut';

## Zmeny vo verzii 1.0 ##

* Počiatočná verzia.
