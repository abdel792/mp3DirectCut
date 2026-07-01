# mp3DirectCut

* Autor(i): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Predstavljanje #

Ovaj dodatak poboljšava pristupačnost programa mp3DirectCut sa NVDA.

Testiran je sa verzijama mp3DirectCut-a od 212 do 233.

## Prečice na tastaturi ##

Ovaj dodatak nudi sledeće komande:

* B

    * Koristi se za potvrdu ispravnog postavljanja markera početka izbora B.

* Ctrl+Shift+B

    * Koristi se za označavanje pozicije markera početka izbora B.
    * Dvostruki pritisak prikazuje trajanje izbora.

* Ctrl+Shift+D

    * Daje trajanje od početka datoteke do trenutne pozicije kursora za reprodukciju.
    * Dvostruki pritisak prikazuje ukupno trajanje.

* Ctrl+R

    * Potvrđuje da je izbor otkazan.

* Ctrl+Shift+R

    * Daje preostalo vreme od trenutne pozicije kursora za reprodukciju do kraja datoteke.

* Ctrl+Shift+E

    * Koristi se za označavanje pozicije markera kraja izbora N.
    * Dvostruki pritisak daje rezime pozicija B i N, kao i trajanje izbora.

* Ctrl+Shift+P

    * Daje referencu trenutnog dela i ukupan broj delova u trenutnoj datoteci.

* Ctrl+Shift+Space

    * Koristi se za određivanje trenutnog nivoa vu-metra tokom snimanja.
    * Dvostruki pritisak ga resetuje.

* Strelica nadole

    * Omogućava vam da pregledate trenutnu poziciju kursora za reprodukciju.
    * Ova komanda takođe postavlja kursor na mesto markera kraja izbora N, dok daje mesto ovog markera ako je izbor napravljen.
    * U dijalogu za jačinu zvuka, izgovara sledeću vrednost koja se uglavnom može dostići strelicom nadole.
    * Ova vrednost se podrazumevano ne izgovara.

* End

    * Pomera kursor za reprodukciju na kraj trenutne datoteke i daje ukupno vreme.

* Home

    * Pomera kursor za reprodukciju na početak trenutne datoteke.

* Strelica nalevo

    * Omogućava kratak povratak unazad od jedne sekunde tokom reprodukcije, dok daje trenutno trajanje.
    * Ovo trajanje se može konfigurisati u opcijama mp3directcut-a.

* N

    * Koristi se za potvrdu ispravnog postavljanja markera kraja izbora N.

* Page Down

    * Omogućava skok unapred od 10 sekundi tokom reprodukcije, uz prikaz trenutnog trajanja.
    * Ovo trajanje se može konfigurisati u opcijama mp3directcut-a.

* Page Up

    * Omogućava povratak unazad od 10 sekundi tokom reprodukcije, uz prikaz trenutnog trajanja.
    * Ovo trajanje se može konfigurisati u opcijama mp3directcut-a.

* R

    * Omogućava pripremu snimanja i proveru da li možete pritisnuti razmaknicu za početak.

* Strelica nadesno

    * Omogućava kratak pomak unapred od jedne sekunde tokom reprodukcije, dok daje trenutno trajanje.
    * Ovo trajanje se može konfigurisati u opcijama mp3directcut-a.

* Ctrl+Strelica nadesno

    * Pomera se na sledeću tačku deljenja, uz prikaz trenutnog trajanja.

* Ctrl+Strelica nalevo

    * Pomera se na prethodnu tačku deljenja, uz prikaz trenutnog trajanja.

* Shift+Strelica nadesno

    * Omogućava kratak pomak unapred od četiri stotinke sekunde tokom reprodukcije, dok daje trenutno trajanje.

* Shift+Strelica nalevo

    * Omogućava kratak povratak unazad od četiri stotinke sekunde tokom reprodukcije, dok daje trenutno trajanje.

* S

    * Koristi se za zaustavljanje čitanja i prikaz trenutnog trajanja.

* Space

    * Ako je snimanje spremno, pokreće ovo snimanje.
    * Ako je snimanje u toku, zaustavlja ga postavljanjem kursora na početak.
    * Ako je datoteka učitana, pokreće čitanje.
    * Ako je čitanje u toku, omogućava pauziranje uz prikaz trenutnog trajanja.
    * Ako je čitanje pauzirano, omogućava ponovno pokretanje čitanja sa trenutnog mesta.

* Strelica nagore

    * Omogućava vam da pregledate trenutnu poziciju kursora za reprodukciju.
    * Ova komanda takođe postavlja kursor na mesto markera početka izbora B, dok daje mesto ovog markera ako je izbor napravljen.
    * U dijalogu za jačinu zvuka, izgovara prethodnu vrednost koja se uglavnom može dostići strelicom nagore.
    * Ova vrednost se podrazumevano ne izgovara.

* NVDA+H

    * Omogućava otvaranje pomoći trenutnog dodatka.

## Kompatibilnost ##

* Ovaj dodatak je kompatibilan sa verzijama NVDA od 2019.3 i novijim.

## Promene za 20240327.0.0

* Ispravljena greška koja je uzrokovala grešku u dnevniku prilikom ponovnog učitavanja dodataka, hvala Robu sa nvda-addons dopisne liste;

## Promene za 20240326.0.0

* Ažurirana kompatibilnost za nvda-2024.1.;
* Uklonjena veza za preuzimanje iz readme datoteke, veza za preuzimanje budućih ažuriranja sada će biti dostupna samo u prodavnici dodataka.

## Promene za 20231229.0.0 ##

* Dodata unazad kompatibilna implementacija za podršku režima govora na zahtev, koji će uskoro biti dostupan sa nvda-2024.1.

## Promene za 20231007.0.0 ##

* Nakon postavljanja tačaka rezanja i nakon otvaranja prozora sa svojstvima rezanja pomoću "Ctrl+N", dodata je pristupačnost naslovu ovog prozora označavanjem indeksa dela.
* U režimu čitanja, nakon pomeranja početnih ili krajnjih markera izbora tasterima 1 do 6 alfanumeričke tastature, dodato je automatsko pokretanje čitanja sa nove pozicije;
* Ispravljena greška koja se pojavljivala pri proveri preostalog vremena pomoću "control+shift+r" od početka zapisa.

## Promene za 20230728.0.0 ##

* Primenjena pravila flake8 i mypy na kod;
* Promenjena minimalna podržana verzija NVDA na 2019.3 radi podrške anotacijama uvedenim u Python-u 3.

## Promene za 20230607.0.0 ##

* Dodati su sledeći tokovi posla (workflows):
 * auto-update-translations - za automatsko ažuriranje prevoda iz NVDA-ovog prevodilačkog sistema.
 * release-on-tag..yaml: za izradu i objavu dodatka čim se gurne nova oznaka (tag);
 * manual-release.yaml: za ručnu izradu i izdavanje novih verzija dodatka.
* Ažurirani prevodi.

## Promene za verziju 20230508.0.0 i novije ##

* Promenjen broj verzije, minimalna verzija NVDA i veza za preuzimanje prema konvencijama/zahtevima prodavnice.

## Promena za verziju 20.12 ##

* Zaustavljanje govora tokom snimanja i čitanja za najnovije verzije mp3DirectCut-a;
* Ispravljeno čitanje preostalog vremena za nove verzije NVDA koje koriste Python 3.

## Promena za verziju 19.02 ##

* Dodata konfiguracija dodatka na panelu sa podešavanjima dostupnoj od nvda 2018.2;
* Promenjeno numerisanje verzija pomoću formata GG.MM (godina u 2 cifre, nakon čega sledi tačka, nakon čega sledi mesec u 2 cifre);
* Dodata kompatibilnost sa novim formatom verzija dodataka, koji se pojavio od nvda 2019.1.

## Promena za verziju 4.0 ##

* Dodata kompatibilnost dodatka sa Python-om 2.7 i 3;
* Ispravljena greška sa putanjama dodatka koje sadrže znakove koji nisu ASCII.

## Promena za verziju 3.0 ##

* Upotrebljen modul gui.guiHelper kako bi se osigurao ispravan izgled konfiguracionog dijaloga dodatka;
* Upotrebljen format umesto %s za formatirane niske;
* Primenjena usklađenost sa smernicama za implementaciju.

## Promena za verziju 2.3 ##

* Dodata GPL licenca dodatku;
* Promenjena prečica skripte koja daje kraj izbora sa Ctrl + Shift + N na Ctrl + Shift + E jer Ctrl + Shift + N ne radi sa najnovijim verzijama mp3DirectCut-a;
* Dodata skripta za potvrdu da je izbor otkazan sa 'Ctrl+r';
* Napravljene neke korekcije u kodu appModule 'mp3directcut.py'.

## Promena za verziju 2.2 ##

* Ispravka skripti koje daju lokacije markera izbora.

## Promena za verziju 2.1.1 ##

* Uklanjanje skripte koja daje ukupno vreme i dodavanje ove informacije skripti koja daje proteklo vreme;
* Dodata mogućnost omogućavanja ili onemogućavanja najava povezanih sa tasterom razmaknice u konfiguracionim opcijama modula, odvojeno od ostalih najava;
* Dodata mogućnost omogućavanja ili onemogućavanja najave postavljanja markera izbora u konfiguracionim opcijama modula;
* Dodavanje najave trenutnog dela pri kretanju kroz tačke deljenja;
* Ispravak najava povezanih sa vertikalnim tasterima;
* Dodavanje skripte za otvaranje pomoći trenutnog dodatka sa 'NVDA+H';
* Premeštanje konfiguracionog menija dodatka iz menija Alatke u meni Postavke NVDA.

## Promena za verziju 2.1 ##

* Dodavanje skripte za izgovaranje pomeranja na sledeću tačku deljenja sa Control+Strelica nadesno;
* Dodavanje skripte za izgovaranje pomeranja na prethodnu tačku deljenja sa Control+Strelica nalevo;
* Dodavanje skripte za izgovaranje pomaka od 4 stotinke sekunde unapred, sa Shift+Strelica nadesno;
* Dodavanje skripte za izgovaranje pomaka od 4 stotinke sekunde unazad, sa Shift+Strelica nalevo;
* Ispravak rezimea dodatka iz 'for mp3DirectCut' u 'mp3DirectCut'.

## Promena za verziju 2.0 ##

* Dodavanje skripte za saznavanje preostalog vremena sa 'Control Shift R';
* Ispravljeno čitanje trajanja uključujući sate;
* Dodata mogućnost razlikovanja hiljaditih ili stotinitih delova sekunde.

## Promena za verziju 1.1 ##

* Dodata mogućnost uključivanja kategorije mp3DirectCut u gestove unosa;

    * Biće vidljive samo tokom korišćenja programa mp3DirectCut.

* Dodata mogućnost omogućavanja ili onemogućavanja automatskih poruka, u meniju alatki NVDA, stavka 'mp3DirectCut konfiguracija';

## Promena za verziju 1.0 ##

* Početna verzija.
