# mp3DirectCut #

* Tekijät: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

# Esittely #

Tämä lisäosa parantaa mp3DirectCut-ohjelman esteettömyyttä NVDA:n kanssa.

Toimivuus on testattu mp3DirectCutin versioilla 2.12 - 2.23.

## Pikanäppäimet ##

Tämä lisäosa tarjoaa seuraavat komennot:

* B

    * Asettaa valinnan aloitusmerkin.

* Ctrl+Vaihto+B

    * Ilmoittaa valinnan aloitusmerkin sijainnin.
    * Kahdesti painettaessa ilmoitetaan valinnan kesto.

* Ctrl+Vaihto+D

    * Ilmoittaa keston tiedoston alusta toistokohdistimen nykyiseen
      sijaintiin saakka.
    * Kahdesti painettaessa ilmoitetaan kokonaiskesto.

* Ctrl+R

    * Vahvistaa, että valinta on peruttu.

* Ctrl+Vaihto+R

    * Ilmoittaa jäljellä olevan ajan toistokohdistimen nykyisestä
      sijainnista tiedoston loppuun saakka.

* Ctrl+Vaihto+E

    * Ilmoittaa valinnan lopetusmerkin sijainnin.
    * Kahdesti painettaessa annetaan yhteenveto valinnan aloitus- ja
      lopetusmerkkien sijainneista sekä valinnan kestosta.

* Ctrl+Vaihto+P

    * Ilmoittaa nykyisen osan sekä tiedostossa olevien osien kokonaismäärän.

* Ctrl+Vaihto+Väli

    * Ilmoittaa VU-mittarin nykyisen tason äänityksen aikana.
    * Kahdesti painaminen nollaa tason.

* Nuoli alas

    * Ilmoittaa toistokohdistimen nykyisen sijainnin.
    * Lisäksi, mikäli valinta on tehty, tämä komento siirtää kohdistimen
      valinnan lopetusmerkin kohdalle ja ilmoittaa sen sijainnin.
    * Ilmoittaa äänenvoimakkuusvalintaikkunassa seuraavan arvon.
    * Oletuksena arvoa ei ilmoiteta.

* End

    * Siirtää toistokohdistimen tiedoston loppuun ja ilmoittaa
      kokonaiskeston.

* Home

    * Siirtää toistokohdistimen tiedoston alkuun.

* Nuoli vasemmalle

    * Siirtää toistettaessa sekunnin taaksepäin ja ilmoittaa nykyisen
      sijainnin.
    * Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä
      komento siirtää.

* N

    * Asettaa valinnan lopetusmerkin.

* Page down

    * Siirtää toistettaessa kymmenen sekuntia eteenpäin ja ilmoittaa
      nykyisen sijainnin.
    * Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä
      komento siirtää.

* Page up

    * Siirtää toistettaessa 10 sekuntia taaksepäin ja ilmoittaa nykyisen
      sijainnin.
    * Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä
      komento siirtää.

* R

    * Valmistelee sovelluksen äänitystä varten. Äänitys aloitetaan
      painamalla Väli-näppäintä.

* Nuoli oikealle

    * Siirtää toistettaessa sekunnin eteenpäin ja ilmoittaa nykyisen
      sijainnin.
    * Mp3DirectCutin asetuksista on mahdollista määrittää, paljonko tämä
      komento siirtää.

* Ctrl+Nuoli oikealle

    * Siirtää seuraavaan leikkauskohtaan ja ilmoittaa sen sijainnin.

* Ctrl+Nuoli vasemmalle

    * Siirtää edelliseen leikkauskohtaan ja ilmoittaa sen sijainnin.

* Vaihto+Nuoli oikealle

    * Siirtää toistettaessa neljä sekunnin sadasosaa eteenpäin ja ilmoittaa
      nykyisen sijainnin.

* Vaihto+Nuoli vasemmalle

    * Siirtää toistettaessa neljä sekunnin sadasosaa taaksepäin ja ilmoittaa
      nykyisen sijainnin.

* S

    * Keskeyttää toiston ja ilmoittaa nykyisen sijainnin.

* Väli

    * Aloittaa äänityksen, jos se on valmiina aloitettavaksi.
    * Keskeyttää äänityksen, mikäli se on käynnissä, ja siirtää tiedoston
      alkuun.
    * Aloittaa toiston, mikäli tiedosto on avoinna.
    * Pysäyttää toiston, mikäli se on käynnissä, ja ilmoittaa nykyisen
      sijainnin.
    * Jatkaa toistoa nykyisestä sijainnista, mikäli se on pysäytetty.

* Nuoli ylös

    * Ilmoittaa toistokohdistimen nykyisen sijainnin.
    * Mikäli valinta on tehty, siirtää toistokohdistimen valinnan
      aloitusmerkin kohdalle ja ilmoittaa sen sijainnin.
    * Ilmoittaa äänenvoimakkuusvalintaikkunassa edellisen arvon.
    * Oletuksena arvoa ei ilmoiteta.

* NVDA+H

    * Avaa lisäosan ohjeen.

## Yhteensopivuus ##

* NVDA-versiot 2016.4:stä eteenpäin ovat yhteensopivia tämän lisäosan
  kanssa.

## Muutokset versiossa 20230508.0.0 ja sitä uudemmissa ##

* • Versionumerointi, NVDA-version vähimmäisvaatimus ja latauslinkki
  muutettu lisäosakaupan käytäntöjen/vaatimusten mukaisiksi.

## Muutokset versiossa 20.12 ##

* Keskeytä puhe nauhoituksen ja mp3directcutin viimeisimmän version
  tarkistuksen aikana;
* Korjattu jäljellä olevan ajan lukeminen uusilla Python 3:a käyttävillä
  NVDA-versioilla.

## Muutokset versiossa 19.02 ##

* Lisäosan asetukset lisätty asetuspaneeliin, joka on ollut käytössä NVDA
  2018.2:sta lähtien;
* Versionumerointi muutettu muotoon vv.kk (vuosi kahdella numerolla, piste
  ja kuukausi kahdella numerolla);
* Lisätty yhteensopivuus lisäosien uudelle versionumeroinnille, joka
  otettiin käyttöön NVDA 2019.1:ssä.

## Muutokset versiossa 4.0 ##

* Lisäosa on nyt yhteensopiva sekä Python 2.7:n että 3:n kanssa;
* Korjattu bugi lisäosan hakemistopolkujen nimissä, jotka sisältävät muita
  kuin ASCII-merkkejä.

## Muutokset versiossa 3.0 ##

* Käytetään gui.guiHelper-moduulia lisäosan asetusvalintaikkunan
  asianmukaisen ulkoasun varmistamiseen;
* Käytetään muotoa %s:n asemesta muotoilluille merkkijonoille;
* Noudatetaan toteutusohjeita.

## Muutokset versiossa 2.3 ##

* Lisätty GPL-lisenssi;
* Muutettu valinnan lopetuskohdan ilmoittavan komennon pikanäppäin
  Ctrl+Shift+N:stä Ctrl+Shift+E:ksi, koska ensin mainittu ei toimi
  mp3DirectCutin uusimmissa versioissa;
* Lisätty skripti, joka varmistaa näppäinkomennolla Ctrl+R, että valinta on
  peruttu;
* Tehty joitakin korjauksia mp3directcut.py-sovellusmoduulin koodiin.

## Muutokset versiossa 2.2 ##

* Valitun alueen  merkkien sijainnit ilmoittavat skriptit korjattu.

## Muutokset versiossa 2.1.1 ##

* Kokonaisajan ilmoittava skripti poistettu ja lisätty sen antamat tiedot
  jäljellä olevan ajan ilmoitukseen;
* Lisäosan asetuksiin lisätty mahdollisuus muista ilmoituksista erillisten
  välilyöntinäppäimeen liittyvien ilmoitusten käyttöön ottamiseen tai
  käytöstä poistamiseen;
* Lisäosan asetuksiin lisätty mahdollisuus valintamerkkien
  sijainti-ilmoituksen käyttöön ottamiseen tai käytöstä poistamiseen;
* Lisätty mahdollisuus nykyisen sijainnin ilmoittamiseen leikkauskohtien
  välillä liikuttaessa;
* Korjattu nuoli ylös- ja nuoli alas -näppäimiin liittyvät ilmoitukset;
* Lisätty skripti lisäosaohjeen avaamiseen näppäinkomennolla NVDA+H;
* Siirretty lisäosan asetusvalintaikkuna Työkalut-valikosta
  Asetukset-valikkoon.

## Muutokset versiossa 2.1 ##

* Lisätty skripti, joka puhuu seuraavan leikkauskohdan siirryttäessä siihen
  näppäinkomennolla Control+Nuoli oikealle;
* Lisätty skripti, joka puhuu edellisen leikkauskohdan siirryttäessä siihen
  näppäinkomennolla Control+Nuoli vasemmalle;
* Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
  eteenpäin näppäinkomennolla Shift+Nuoli oikealle;
* Lisätty skripti, joka puhuu siirryttäessä neljä sekunnin sadasosaa
  taaksepäin näppäinkomennolla Shift+Nuoli vasemmalle;
* Korjattu lisäosan yhteenvedoksi "mp3DirectCut".

## Muutokset versiossa 2.0 ##

* Lisätty jäljellä olevan ajan ilmoittava komento Control+Shift+R;
* Korjattu keston, tunnit mukaan lukien, lukeminen;
* Lisätty mahdollisuus sekunnin tuhannes- ja sadasosien erottamiseen
  toisistaan.

## Muutokset versiossa 1.1 ##

* Lisätty Mp3DirectCut-kategoria Näppäinkomennot-valintaikkunaan;

    * Se on näkyvissä vain sovellusta käytettäessä.

* Lisäosan asetuksiin lisätty mahdollisuus automaattisten ilmoitusten
  käyttöön ottamiseen tai käytöstä poistamiseen;

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut


[2]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut
