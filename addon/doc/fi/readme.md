# mp3DirectCut #

*	 Tekijät: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Lataa [vakaa versio][1]
*	 Lataa [kehitysversio][2]

# Esittely #

Tämä lisäosa parantaa mp3DirectCut-ohjelman esteettömyyttä NVDA:n kanssa.

Toimivuus on testattu mp3DirectCutin versioilla 2.12 - 2.22.

## Pikanäppäimet ##

Tämä lisäosa tarjoaa seuraavat näppäinkomennot, joita voidaan muuttaa
valitsemalla Asetukset-valikosta Syöte-eleet ja mp3DirectCut-kategoria:

*	B
	*	Asettaa valinnan aloitusmerkin nykyiseen sijaintiin.
*	Ctrl+Shift+B
	*	Ilmoittaa valinnan aloitusmerkin sijainnin.
	*	Kahdesti painettaessa kerrotaan valinnan kesto.
*	Ctrl+Shift+D
	*	Ilmoittaa keston tiedoston alusta toistokohdistimen nykyiseen sijaintiin saakka.
	*	Kahdesti painettaessa ilmoitetaan koko tiedoston kesto.
*	Ctrl+Shift+R
	*	Ilmoittaa jäljellä olevan ajan toistokohdistimen nykyisestä sijainnista tiedoston loppuun saakka.
*	Ctrl+Shift+N
	*	Ilmoittaa valinnan lopetusmerkin sijainnin.
	*	Antaa kahdesti painettaessa yhteenvedon valinnan aloitus- ja lopetusmerkkien sijainneista sekä ilmoittaa valinnan keston.
*	Ctrl+Shift+P
	*	Ilmoittaa nykyisen osan sekä tiedostossa olevien osien määrän.
*	Ctrl+Shift+Space
	*	Ilmoittaa VU-mittarin nykyisen tason äänityksen aikana.
	*	Kahdesti painaminen nollaa tason.
*	Nuoli alas
	*	Ilmoittaa toistokohdistimen nykyisen sijainnin.
	*	Lisäksi, mikäli valinta on tehty, tämä komento siirtää kohdistimen valinnan lopetusmerkin kohdalle ja ilmoittaa sen sijainnin.
	*	Puhuu äänenvoimakkuusvalintaikkunassa seuraavan arvon.
	*	Oletuksena tätä arvoa ei puhuta.
*	End
	*	Siirtää toistokohdistimen tiedoston loppuun ja ilmoittaa kokonaiskeston.
*	Home
	*	Siirtää toistokohdistimen tiedoston alkuun.
*	Nuoli vasemmalle
	*	Siirtää toistettaessa sekunnin taaksepäin ja ilmoittaa samalla nykyisen sijainnin.
	*	Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä komento siirtää.
*	N
	*	Asettaa valinnan lopetusmerkin nykyiseen sijaintiin.
*	Page down
	*	Siirtää toistettaessa kymmenen sekuntia eteenpäin ja ilmoittaa samalla nykyisen sijainnin.
	*	Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä komento siirtää.
*	Page up
	*	Siirtää toistettaessa 10 sekuntia taaksepäin ja ilmoittaa samalla nykyisen sijainnin.
	*	Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä komento siirtää.
*	R
	*	Aktivoi äänityksen, jonka voit aloittaa painamalla Välilyöntiä.
*	Oikea nuoli
	*	Siirtää toistettaessa sekunnin eteenpäin ja ilmoittaa samalla nykyisen sijainnin.
	*	Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä komento siirtää.
*	Ctrl+Nuoli oikealle
	*	Siirtää seuraavaan leikkauskohtaan ja ilmoittaa sen sijainnin.
*	Ctrl+Nuoli vasemmalle
	*	Siirtää edelliseen leikkauskohtaan ja ilmoittaa sen sijainnin.
*	Shift+Nuoli oikealle
	*	Siirtää toistettaessa neljä sekunnin sadasosaa eteenpäin ja ilmoittaa nykyisen sijainnin.
*	Shift+Nuoli vasemmalle
	*	Siirtää toistettaessa neljä sekunnin sadasosaa taaksepäin ja ilmoittaa nykyisen sijainnin.
*	S
	*	Keskeyttää toiston ja ilmoittaa nykyisen sijainnin.
*	Välilyönti
	*	Mikäli äänitys on valmiina aloitettavaksi, aloittaa sen.
	*	Mikäli äänitys on käynnissä, pysäyttää sen ja siirtää tiedoston alkuun.
	*	Aloittaa toiston, mikäli tiedosto on avoinna.
	*	Mikäli toisto on käynnissä, pysäyttää sen ja ilmoittaa nykyisen sijainnin.
	*	Mikäli toisto on pysäytetty, jatkaa sitä nykyisestä sijainnista.
*	Nuoli ylös
	*	Puhuu toistokohdistimen nykyisen sijainnin.
	*	Lisäksi, mikäli valinta on tehty,  tämä komento siirtää kohdistimen valinnan aloitusmerkin kohdalle ja puhuu sen sijainnin.
	*	Puhuu äänenvoimakkuusvalintaikkunassa edellisen arvon.
	*	Tätä ei puhuta oletuksena.
*	NVDA+H
	*	Avaa lisäosan ohjeen.

## Muutokset versiossa 2.2 ##

*     Valitun alueen  merkkien sijainnit ilmoittavat skriptit korjattu.

## Muutokset versiossa 2.1.1 ##

*	 Kokonaisajan ilmoittava skripti poistettu ja lisätty sen antamat tiedot
   jäljellä olevan ajan ilmoitukseen;
*	 Lisäosan asetuksiin lisätty mahdollisuus muista ilmoituksista erillisten
   välilyöntinäppäimeen liittyvien ilmoitusten käyttöön ottamiseen tai
   käytöstä poistamiseen;
*	 Lisäosan asetuksiin lisätty mahdollisuus valintamerkkien
   sijainti-ilmoituksen käyttöön ottamiseen tai käytöstä poistamiseen;
*	 Lisätty mahdollisuus nykyisen sijainnin ilmoittamiseen leikkauskohtien
   välillä liikuttaessa;
*	 Korjattu nuoli ylös- ja nuoli alas -näppäimiin liittyvät ilmoitukset;
*	 Lisätty skripti lisäosaohjeen avaamiseen näppäinkomennolla NVDA+H;
*	 Siirretty lisäosan asetusvalintaikkuna Työkalut-valikosta
   Asetukset-valikkoon.

## Muutokset versiossa 2.1 ##

*	 Lisätty skripti, joka puhuu seuraavan leikkauskohdan siirryttäessä siihen
   näppäinkomennolla Control+Nuoli oikealle;
*	 Lisätty skripti, joka puhuu edellisen leikkauskohdan siirryttäessä siihen
   näppäinkomennolla Control+Nuoli vasemmalle;
*	 Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
   eteenpäin näppäinkomennolla Shift+Nuoli oikealle;
*	 Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
   taaksepäin näppäinkomennolla Shift+Nuoli vasemmalle;
*	 Korjattu lisäosan yhteenvedoksi "mp3DirectCut".

## Muutokset versiossa 2.0 ##

*	 Lisätty jäljellä olevan ajan ilmoittava komento Control+Shift+R;
*	 Korjattu keston, tunnit mukaan lukien, lukeminen;
*	 Lisätty mahdollisuus sekunnin tuhannes- ja sadasosien erottamiseen
   toisistaan.

## Muutokset versiossa 1.1 ##

*	 Syöte-eleet-valintaikkunaan lisätty mp3DirectCut-kategoria;
	*	 sen sisältämät komennot ovat näkyvissä vain ohjelman ollessa käynnissä.
*	 Lisätty mahdollisuus automaattisten ilmoitusten käyttöön ottamiseen tai käytöstä poistamiseen NVDA:n Työkalut-valikon mp3DirectCut-kohteeseen;

## Muutokset versiossa 1.0 ##

*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
