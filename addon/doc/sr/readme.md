# mp3DirectCut #

*	 Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Preuzmi[stabilnu verziju][1]
*	 Preuzmi[razvojnu verziju][2]

# Predstavljanje #

Ovaj dodatak poboljšava pristupačnost programa mp3DirectCut sa programom
NVDA.

Testiran je sa verzijama programa mp3DirectCut od 212 do 222.

## Prečice ##

Ovaj dodatak pruža sledeće komande, koje možete promeniti iz menija
podešavanja/ ulazne komande' u kategoriji 'mp3DirectCut':

*	B
	*	Koristi se za potvrdu početka izbora tasterom B.
*	Kontrol+Šift+B
	*	Koristi se za izgovor pozicije početka izbora tasterom B.
	*	Dvostruki pritisak vam daje ukupno trajanje izbora.
*	Kontrol+Šift+D
	*	Daje trajanje od početka datoteke do pozicije kursora.
	*	Dvostruki pritisak vam daje ukupno trajanje.
*	Kontrol+Šift+R
	*	Daje preostalo vreme od trenutne pozicije kursora do kraja datoteke.
*	Kontrol+Šift+N
	*	Koristi se za izgovor pozicije završnog izbora teksta tasterom N.
	*	Dvostruki pritisak daje bliske pozicije tasterom B i N, i trajanje izbora.
*	Kontrol+Šift+P
	*	Daje broj dela i ukupan broj delova trenutne datoteke.
*	Kontrol+Šift+razmak
	*	Koristi se za trenutni nivo gornjeg metra, u toku snimanja.
	*	Dvostruki pritisak ga vraća.
*	Strelica dole
	*	Dozvoljava  vam da vidite trenutnu poziciju reprodukcije.
	*	Ova komanda takođe postavlja kursor na poziciju završnog izbora tasterom N, dok ako je izabran daje lokaciju markera.
	*	U dijalogu za jačinu, pronađite sledeću vrednost koju možete postaviti strelicom dole.
	*	Ova vrednost nije podešena podrazumevano.
*	End
	*	Pomera kursor reprodukcije na kraj trenutne datoteke i daje ukupno vreme.
*	Home
	*	Pomera kursor reprodukcije na početak trenutne datoteke.
*	Strelica levo
	*	Dozvoljava vam vraćanje za jednu sekundu u toku reprodukcije, i daje trenutno trajanje.
	*	Ovo trajanje se može podesiti u podešavanjima.
*	N
	*	Koristi se za potvrdu mesta završnog markera tasterom N.
*	Page Down
	*	Dozvoljava vam skok za deset sekundi napred u toku reprodukcije, i daje trenutno trajanje.
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
	*	Pomera se na sledeću tačku odvajanja, i daje trenutno trajanje.
*	Kontrol+strelica levo
	*	Pomera se na prethodnu tačku odvajanja, i daje trenutno trajanje.
*	Šift+strelica desno
	*	Dozvoljava skok za četiri stotinke u toku reprodukcije, i daje trenutno trajanje.
*	Šift+strelica levo
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
	*	Ova komanda takođe postavlja kursor na lokaciju početnog markera tasterom B, i daje lokaciju markera ako je izbor podešen.
	*	U dijalogu za jačinu, pronalazi prethodnu vrednost koja se može promeniti strelicom gore.
	*	Ova vrednost nije podešena podrazumevano.
*	NVDA+H
	*	Dozvoljava vam da otvorite pomoć dodatka.

## Promene u verziji 2.2 ##

*     Popravljene prečice za lokaciju izbora

## Promene u verziji 2.1.1 ##

*	 Uklonjena prečica za ukupno vreme i prebačena na prečicu za preostalo
   vreme
*	 Dodata mogućnost da onemogućite izgovor razmaka, odvojeno od drugih
   objava
*	 Dodata mogućnost podešavanja izgovora izbora
*	 Dodat  izgovor isečenih delova kada se krećete kroz zapis
*	 Popravljen izgovor uspravnih tastera
*	 Dodata prečica za otvaranje pomoći dodatka komandom NVDA+h
*	 Pomeranje stavke za podešavanje dodatka iz menija alati u meni
   podešavanja

## Promene u verziji 2.1 ##

*	 Dodata prečica za izgovor pomeranja na sledeću stavku komandom
   Kontrol+strelica desno
*	 Dodata prečica za izgovor pomeranja na prethodnu stavku komandom
   Kontrol+strelica levo
*	 Dodata prečica za izgovor pomeranja komandom šift+ strelica desno
*	 Dodata prečica za izgovor pomeranja komandom šift+ strelica levo
*	 Popravljeno ime dodatka iz 'for mp3DirectCut' u 'mp3DirectCut'.

## Promene u verziji 2.0 ##

*	 Dodata prečica za izgovor preostalog vremena 'Control Shift R';
*	 Popravljeno čitanje trajanja uključujući sate
*	 Dodata sposobnost razlikovanja desetinki i stotinki

## Promene u verziji 1.1 ##

*	 Dodata sposobnost prepoznavanja MP3 DirectCut u ulaznim komandama;
	*	 Biće dostupne samo kada koristite MP3 DirectCut program.
*	 Dodata sposobnost da omogućite ili onemogućite automatske poruke, u meniju alati NVDA menija, stavka 'mp3DirectCut podešavanja';

## Promene u verziji 1.0 ##

*	 Prva verzija.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
