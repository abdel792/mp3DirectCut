# mp3DirectCut #

*	 Autor(i) Abdel, Rémy, Abdellah zineddine, Jean-François COLAS: 
*	 Preuzmi [stable version][1]
*	 Preuzmi [development version][2]

# Prezentacija #

Ovaj dodatak poboljšava pristupačnost programa mp3DirectCut sa NVDA.

Testiran je s mp3DirectCut inačicama u rasponu od 212 do 223.

## Tipkovni prečaci  ##

Ovaj dodatak nudi sljedeće naredbe: 

*	B
	*	Koristi se za potvrdu početka izbora slovom B.
*	Kontrol+Šift+B
	*	Koristi se za izgovor pozicije početka izbora slovom B.
	*	Dvostruki pritisak vam daje ukupno trajanje izbora.
*	Kontrol+Šift+D
	*	Daje trajanje od početka datoteke do pozicije kursora.
	*	Dvostruki pritisak vam daje ukupno trajanje.
*	Kontrol+Šift+R
	*	Daje preostalo vrijeme od trenutne pozicije kursora do kraja datoteke.
*	Kontrol+Šift+N
	*	Koristi se za izgovor pozicije završnog izbora teksta slovom N.
	*	Dvostruki pritisak daje bliske pozicije slovom B i N, i trajanje izbora.
*	Kontrol+Šift+P
	*	Daje broj dijela i ukupan broj dijelova trenutne datoteke.
*	Kontrol+Šift+razmak
	*	Koristi se za trenutni nivo gornjeg metra, u toku snimanja.
	*	Dvostruki pritisak ga vraća.
*	Strelica dolje
	*	Dozvoljava  vam da vidite trenutnu poziciju reprodukcije.
	*	Ova naredba također postavlja kursor na poziciju završnog izbora slovom N, dok ako je izabran daje lokaciju markera.
	*	U dijaloškom okviru za jačinu, pronađite sljedeću vrijednost koju možete postaviti strelicom dolje.
	*	Ova vrijednost nije podešena podrazumijevano.
*	End
	*	Pomjera kursor reprodukcije na kraj trenutne datoteke i daje ukupno vrijeme.
*	Home
	*	Pomjera kursor reprodukcije na početak trenutne datoteke.
*	Strelica lijevo
	*	Dozvoljava vam vraćanje za jednu sekundu u toku reprodukcije, i daje trenutno trajanje.
	*	Ovo trajanje se može podesiti u podešavanjima.
*	N
	*	Koristi se za potvrdu mjesta završnog markera slovom N.
*	Page Down
	*	Dozvoljava vam skok za deset sekundi naprijed u toku reprodukcije, i daje trenutno trajanje.
	*	Ovo trajanje se može podesiti u podešavanjima programa mp3directcut.
*	Page Up
	*	Dozvoljava vam vraćanje za deset sekundi u toku reprodukcije, i daje trenutno trajanje.
	*	Ovo trajanje se može podesiti u podešavanjima programa mp3directcut.
*	R
	*	Dozvoljava pripremu snimanja i da li se može pritisnuti razmak za početak.
*	Strelica desno
	*	Dozvoljava kratak skok od jedne sekunde u toku reprodukcije, i daje trenutno trajanje.
	*	Ovo trajanje se može podesiti u podešavanjima programa mp3directcut.
*	Kontrol+strelica desno
	*	Pomjera se na sljedeću točku odvajanja, i daje trenutno trajanje.
*	Kontrol+strelica lijevo
	*	Pomjera se na prethodnu točku odvajanja, i daje trenutno trajanje.
*	Šift+strelica desno
	*	Dozvoljava skok za četiri stotinke u toku reprodukcije, i daje trenutno trajanje.
*	Šift+strelica lijevo
	*	Dozvoljava mali skok od četiri stotinke nazad u toku reprodukcije, i daje trenutno trajanje. 
*	S
	*	Koristi se za zaustavljanje čitanja i izgovor trenutnog trajanja.
*	Razmak
	*	Ako je snimanje spremno, započinje snimanje.
	*	Ako je snimanje u toku, zaustavlja ga i postavlja kursor na početak.
	*	Ako je datoteka učitana, započinje čitanje.
	*	Ako je čitanje u toku, dozvoljava pauzu i daje trenutno trajanje.
	*	Ako je čitanje pauzirano, dozvoljava početak čitanja od trenutne lokacije.
*	Strelica gore
	*	Dozvoljava vam da vidite trenutnu poziciju reprodukcije.
	*	Ova naredba također postavlja kursor na lokaciju početnog markera slovom B, i daje lokaciju markera ako je izbor podešen.
	*	U dijaloškom okviru za jačinu, pronalazi prethodnu vrijednost koja se može promijeniti strelicom gore.
	*	Ova vrijednost nije podešena podrazumijevano.
*	NVDA+H
	*	Dozvoljava vam da otvorite pomoć dodatka.

## Promjene u inačici 4.0 ##

*	 Dodana Kompatibilnost dodatka s Pythonom 2.7 i 3;
*	 Ispravljena je greška u dodatku koja je sadržavala znakove koji nisu
   ASCII.

## Promjene u inačici 3.0 ##

*	 Korišten je gui.guiHelper modul kako bi se potvrdio ispravan prikaz
   dijaloškog okvira konfiguracije dodatka;
*	 Korišten je format umjesto %s za formatirane stringove;
*	 Dodatak je izrađen sukladno smjernicama za implementaciju.

## Promjene u inačici 2.3 ##

*	 Dodana je GPL licenca u dodatak;
*	 Promijenjena je kratica za skriptu koja daje kraj odabira iz Kontrol +
   Šift + N u Kontrol + Šift + E jer Kontrol + Šift + N ne radi sa zadnjim
   inačicama mp3DirectCut;
*	 Dodana je skripta za potvrđivanje da je odabir otkazan sa 'Kontrol + r';
*	 Učinjene su neke ispravke u kodu appModula 'mp3directcut.py..

## Promjene u inačici 2.2 ##

*	 Ispravljene skripte koje daju lokacije odabranih markera.

## Promjene u inačici 2.1.1 ##

*	 Uklonjena skripta koja daje ukupno vrijeme a ta je informacija dodana u
   skriptu koja daje preostalo vrijeme;
*	 Dodana mogućnost omogućavanja ili onemogućavanja obavijesti vezanih uz
   tipku razmak u opcijama konfiguriranja modula, odvojeno od drugih
   obavijesti;
*	 Dodana mogućnost omogućavanja ili onemogućavanja najave postavljanja
   oznaka odabira u opcijama konfiguriranja modula;
*	 Dodano izgovaranje trenutnog dijela dok se krećete kroz izrezane točke;
*	 Ispravljene obavijesti vezanih uz vertikalne tipke;
*	 Dodana skripta za otvaranje pomoći trenutnog dodatka sa 'NVDA+H';
*	 Premješten je izbornik konfiguracije dodatka iz izbornika Alati u
   izbornik Postavki NVDA. 

## Promjene u inačici 2.1 ##

*	 Dodana skripta za vokaliziranje prijelaza na sljedeću točku razdvajanja
   sa Kontrol+Strelicom desno;
*	 Dodana skripta za vokaliziranje prijelaza na prethodnu točku razdvajanja
   sa Kontrol+Strelicom lijevo;
*	 Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unaprijed,
   sa Šift + strelicom desno;
*	 Dodana skripta za vokaliziranje pomaka od 4 stotinke sekunde unatrag, sa
   Šift+Strelicom lijevo;
*	 Ispravak sažetka dodatka iz 'za mp3DirectCut' u 'mp3DirectCut'.

## Promjene u inačici 2.0 ##

*	 Dodana skripta kako bi se saznalo preostalo vrijeme sa 'Kontrol Šift R';
*	 Poboljšan način čitanja trajanja uključujući sate;
*	 Dodana mogućnost razlikovanja tisućinki ili stotinki sekunde.

## Promjene u inačici 1.1 ##

*	 Dodana mogućnost uključivanja kategorije mp3DirectCut u Ulazne geste;
	*	 One će biti vidljive samo tijekom korištenja programa mp3DirectCut.
*	 Dodana mogućnost omogućavanja ili onemogućavanja automatskih poruka, u izborniku alata NVDA, stavka 'mp3DirectCut konfiguracija'

## Promjene u inačici 1.0 ##

*	 Inicijalna verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
