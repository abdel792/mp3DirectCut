# mp3DirectCut

* Autor(i): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Predstavljanje #

ovaj dodatak poboljšava pristupačnost softvera mp3DirectCut s NVDA.

Testiran je s verzijama mp3DirectCuta od 212 do 233.

## Prečaci na tipkovnici ##

Ovaj dodatak nudi sljedeće naredbe:

* B

    * Koristi se za potvrdu ispravnog postavljanja markera početka odabira B.

* Ctrl+Shift+B

    * Koristi se za označavanje položaja markera početka odabira B.
    * Dvostruki pritisak prikazuje trajanje odabira.

* Ctrl+Shift+D

    * Daje trajanje od početka datoteke do trenutnog položaja kursora za reprodukciju.
    * Dvostruki pritisak prikazuje ukupno trajanje.

* Ctrl+R

    * Potvrđuje da je odabir otkazan.

* Ctrl+Shift+R

    * Daje preostalo vrijeme od trenutnog položaja kursora za reprodukciju do kraja datoteke.

* Ctrl+Shift+E

    * Koristi se za označavanje položaja markera kraja odabira N.
    * Dvostruki pritisak daje sažetak položaja B i N, kao i trajanje odabira.

* Ctrl+Shift+P

    * Daje referencu trenutnog dijela i ukupan broj dijelova u trenutnoj datoteci.

* Ctrl+Shift+Space

    * Koristi se za određivanje trenutne razine vu-metra tijekom snimanja.
    * Dvostruki pritisak ponovno ga postavlja.

* Strelica prema dolje

    * Omogućuje vam pregled trenutnog položaja kursora za reprodukciju.
    * Ova naredba također postavlja kursor na mjesto markera kraja odabira N, dok daje mjesto ovog markera ako je odabir napravljen.
    * U dijaloškom okviru glasnoće izgovara sljedeću vrijednost koja se općenito može dosegnuti strelicom prema dolje.
    * Ova se vrijednost prema zadanim postavkama ne izgovara.

* End

    * Pomče kursor za reprodukciju na kraj trenutne datoteke i daje ukupno vrijeme.

* Home

    * Pomče kursor za reprodukciju na početak trenutne datoteke.

* Strelica prema lijevo

    * Omogućuje kratki povratak unatrag od jedne sekunde tijekom reprodukcije, dok daje trenutno trajanje.
    * Ovo trajanje se može konfigurirati u opcijama mp3directcuta.

* N

    * Koristi se za potvrdu ispravnog postavljanja markera kraja odabira N.

* Page Down

    * Omogućuje skok naprijed od 10 sekundi tijekom reprodukcije, uz prikaz trenutnog trajanja.
    * Ovo trajanje se može konfigurirati u opcijama mp3directcuta.

* Page Up

    * Omogućuje povratak unatrag od 10 sekundi tijekom reprodukcije, uz prikaz trenutnog trajanja.
    * Ovo trajanje se može konfigurirati u opcijama mp3directcuta.

* R

    * Omogućuje pripremu snimanja i provjeru možete li pritisnuti razmaknicu za početak.

* Strelica prema desno

    * Omogućuje kratki pomak naprijed od jedne sekunde tijekom reprodukcije, dok daje trenutno trajanje.
    * Ovo trajanje se može konfigurirati u opcijama mp3directcuta.

* Ctrl+Strelica prema desno

    * Pomiče se na sljedeću točku dijeljenja, uz prikaz trenutnog trajanja.

* Ctrl+Strelica prema lijevo

    * Pomiče se na prethodnu točku dijeljenja, uz prikaz trenutnog trajanja.

* Shift+Strelica prema desno

    * Omogućuje kratki pomak naprijed od četiri stotinke sekunde tijekom reprodukcije, dok daje trenutno trajanje.

* Shift+Strelica prema lijevo

    * Omogućuje kratki povratak unatrag od četiri stotinke sekunde tijekom reprodukcije, dok daje trenutno trajanje.

* S

    * Koristi se za zaustavljanje čitanja i prikaz trenutnog trajanja.

* Space

    * Ako je snimanje spremno, pokreće ovo snimanje.
    * Ako je snimanje u tijeku, zaustavlja ga postavljanjem kursora na početak.
    * Ako je datoteka učitana, pokreće čitanje.
    * Ako je čitanje u tijeku, omogućuje pauziranje uz prikaz trenutnog trajanja.
    * Ako je čitanje pauzirano, omogućuje ponovno pokretanje čitanja s trenutnog mjesta.

* Strelica prema gore

    * Omogućuje vam pregled trenutnog položaja kursora za reprodukciju.
    * Ova naredba također postavlja kursor na mjesto markera početka odabira B, dok daje mjesto ovog markera ako je odabir napravljen.
    * U dijaloškom okviru glasnoće izgovara prethodnu vrijednost koja se općenito može dosegnuti strelicom prema gore.
    * Ova se vrijednost prema zadanim postavkama ne izgovara.

* NVDA+H

    * Omogućuje otvaranje pomoći trenutnog dodatka.

## Kompatibilnost ##

* Ovaj je dodatak kompatibilan s verzijama NVDA od 2019.3 i novijim.

## Promjene za 20240327.0.0

* Ispravljena pogreška koja je uzrokovala pogrešku u zapisniku prilikom ponovnog učitavanja dodataka, zahvaljujući Robu s nvda-addons dopisne liste;

## Promjene za 20240326.0.0

* Ažurirana kompatibilnost za nvda-2024.1.;
* Uklonjena poveznica za preuzimanje iz readme datoteke, poveznica za preuzimanje budućih ažuriranja sada će biti dostupna samo u trgovini dodataka.

## Promjene za 20231229.0.0 ##

* Dodana unazadna kompatibilna implementacija za podršku načina govora na zahtjev, koji će uskoro biti dostupan s nvda-2024.1.

## Promjene za 20231007.0.0 ##

* Nakon postavljanja točaka rezanja i nakon otvaranja prozora sa svojstvima rezanja pomoću "Ctrl+N", dodana je pristupačnost naslovu ovog prozora označavanjem indeksa dijela.
* U načinu čitanja, nakon pomicanja početnih ili krajnjih markera odabira tipkama 1 do 6 alfanumeričke tipkovnice, dodano je automatsko pokretanje čitanja s novog položaja;
* Ispravljena pogreška koja se pojavljivala pri provjeri preostalog vremena pomoću "control+shift+r" od početka zapisa.

## Promjene za 20230728.0.0 ##

* Primijenjena pravila flake8 i mypy na kod;
* Promijenjena minimalna podržana verzija NVDA na 2019.3 radi podrške anotacijama uvedenim u Pythonu 3.

## Promjene za 20230607.0.0 ##

* Dodani su sljedeći tijekovi rada:
 * auto-update-translations - za automatsko ažuriranje prijevoda iz NVDA-ovog prevoditeljskog sustava.
 * release-on-tag..yaml: za izradu i objavu dodatka čim se gurne nova oznaka (tag);
 * manual-release.yaml: za ručnu izradu i izdavanje novih verzija dodatka.
* Ažurirani prijevodi.

## Promjene za verziju 20230508.0.0 i novije ##

* Promijenjen broj verzije, minimalna verzija NVDA i poveznica za preuzimanje prema konvencijama/zahtjevima trgovine.

## Promjena za verziju 20.12 ##

* Zaustavljanje govora tijekom snimanja i čitanja za najnovije verzije mp3DirectCuta;
* Ispravljeno čitanje preostalog vremena za nove verzije NVDA koje koriste Python 3.

## Promjena za verziju 19.02 ##

* Dodana konfiguracija dodatka na ploči s postavkama dostupnoj od nvda 2018.2;
* Promijenjeno numeriranje verzija pomoću formato GGGG.MM (godina u 2 znamenke, nakon čega slijedi točka, nakon čega slijedi mjesec u 2 znamenke);
* Dodana kompatibilnost s novim formatom verzija dodataka, koji se pojavio od nvda 2019.1.

## Promjena za verziju 4.0 ##

* Dodana kompatibilnost dodatka s Pythonom 2.7 i 3;
* Ispravljena pogreška s putanjama dodatka koje sadrže znakove koji nisu ASCII.

## Promjena za verziju 3.0 ##

* Upotrijebljen modul gui.guiHelper kako bi se osigurao ispravan izgled konfiguracijskog dijaloškog okvira dodatka;
* Upotrijebljen format umjesto %s za formatirane nizove;
* Primijenjena usklađenost sa smjernicama za implementaciju.

## Promjena za verziju 2.3 ##

* Dodana GPL licenca dodatku;
* Promijenjen prečac skripte koja daje kraj odabira s Ctrl + Shift + N na Ctrl + Shift + E jer Ctrl + Shift + N ne radi s najnovijim verzijama mp3DirectCuta;
* Dodana skripta za potvrdu da je odabir otkazan s 'Ctrl+r';
* Napravljene neke korekcije u kodu appModule 'mp3directcut.py'.

## Promjena za verziju 2.2 ##

* Ispravak skripti koje daju lokacije markera odabira.

## Promjena za verziju 2.1.1 ##

* Uklanjanje skripte koja daje ukupno vrijeme i dodavanje ove informacije skripti koja daje proteklo vrijeme;
* Dodana mogućnost omogućavanja ili onemogućavanja najava povezanih s tipkom razmaknice u konfiguracijskim opcijama modula, odvojeno od ostalih najava;
* Dodana mogućnost omogućavanja ili onemogućavanja najave postavljanja markera odabira u konfiguracijskim opcijama modula;
* Dodavanje najave trenutnog dijela pri kretanju kroz točke dijeljenja;
* Ispravak najava povezanih s okomitim tipkama;
* Dodavanje skripte za otvaranje pomoći trenutnog dodatka s 'NVDA+H';
* Premještanje konfiguracijskog izbornika dodatka iz izbornika Alati u izbornik Postavke NVDA.

## Promjena za verziju 2.1 ##

* Dodavanje skripte za izgovaranje pomicanja na sljedeću točku dijeljenja s Control+Strelica prema desno;
* Dodavanje skripte za izgovaranje pomicanja na prethodnu točku dijeljenja s Control+Strelica prema lijevo;
* Dodavanje skripte za izgovaranje pomaka od 4 stotinke sekunde unaprijed, sa Shift+Strelica prema desno;
* Dodavanje skripte za izgovaranje pomaka od 4 stotinke sekunde unatrag, sa Shift+Strelica prema lijevo;
* Ispravak sažetka dodatka iz 'for mp3DirectCut' u 'mp3DirectCut'.

## Promjena za verziju 2.0 ##

* Dodavanje skripte za saznavanje preostalog vremena s 'Control Shift R';
* Ispravljeno čitanje trajanja uključujući sate;
* Dodana mogućnost razlikovanja tisućinki ili stotinki sekunde.

## Promjena za verziju 1.1 ##

* Dodana mogućnost uključivanja kategorije mp3DirectCut u geste unosa;

    * Bit će vidljive samo tijekom korištenja softvera mp3DirectCut.

* Dodana mogućnost omogućavanja ili onemogućavanja automatskih poruka, u izborniku alata NVDA, stavka 'mp3DirectCut konfiguracija';

## Promjena za verziju 1.0 ##

* Početna verzija.
