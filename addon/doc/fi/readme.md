# mp3DirectCut

* Tekijä(t): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Esittely #

Tämä lisäosa parantaa mp3DirectCut-ohjelmiston saavutettavuutta NVDA-ruudunlukuohjelman kanssa.

Se on testattu mp3DirectCut-versioilla 212–233.

## Pikanäppäimet ##

Tämä lisäosa tarjoaa seuraavat komennot:

* B

    * Käytetään vahvistamaan valinnan alun B-merkin oikea sijoitus.

* Ctrl+Shift+B

    * Käytetään ilmoittamaan valinnan alun B-merkin sijainti.
    * Kaksoispainallus ilmoittaa valinnan keston.

* Ctrl+Shift+D

    * Kertoo keston tiedoston alusta toistokursorin nykyiseen sijaintiin.
    * Kaksoispainallus ilmoittaa kokonaiskeston.

* Ctrl+R

    * Vahvistaa, että valinta on peruttu.

* Ctrl+Shift+R

    * Kertoo jäljellä olevan ajan toistokursorin nykyisestä sijainnista tiedoston loppuun.

* Ctrl+Shift+E

    * Käytetään ilmoittamaan valinnan lopun N-merkin sijainti.
    * Kaksoispainallus antaa yhteenvedon B- ja N-merkkien sijainneista sekä valinnan kestosta.

* Ctrl+Shift+P

    * Kertoo nykyisen osan tunnisteen ja osien kokonaismäärän nykyisessä tiedostossa.

* Ctrl+Shift+Space

    * Käytetään määrittämään tasomittarin nykyinen taso tallennuksen aikana.
    * Kaksoispainallus nollaa sen.

* Nuoli alas

    * Näyttää toistokursorin nykyisen sijainnin.
    * Tämä komento siirtää kursorin myös valinnan lopun N-merkin kohdalle ja ilmoittaa tämän merkin sijainnin, jos valinta on tehty.
    * Äänenvoimakkuuden valintaikkunassa puhuu seuraavan arvon, joka voidaan yleensä saavuttaa alanuolella.
    * Tätä arvoa ei puhuta oletusarvoisesti.

* End

    * Siirtää toistokursorin nykyisen tiedoston loppuun ja kertoo kokonaisajan.

* Home

    * Siirtää toistokursorin nykyisen tiedoston alkuun.

* Nuoli vasemmalle

    * Tekee lyhyen, yhden sekunnin palautuksen taaksepäin toiston aikana ja ilmoittaa nykyisen keston.
    * Tämä kesto on määritettävissä mp3DirectCutin asetuksissa.

* N

    * Käytetään vahvistamaan valinnan lopun N-merkin oikea sijoitus.

* Page Down

    * Tekee 10 sekunnin hypyn eteenpäin toiston aikana ja ilmoittaa nykyisen keston.
    * Tämä kesto on määritettävissä mp3DirectCutin asetuksissa.

* Page Up

    * Tekee 10 sekunnin palautuksen taaksepäin toiston aikana und ilmoittaa nykyisen keston.
    * This duration is configurable in the options of mp3directcut.

* R

    * Mahdollistaa tallennuksen valmistelun ja kertoo, voiko tallennuksen aloittaa painamalla välilyöntiä.

* Nuoli oikealle

    * Tekee lyhyen, yhden sekunnin siirron eteenpäin toiston aikana ja ilmoittaa nykyisen keston.
    * Tämä kesto on määritettävissä mp3DirectCutin asetuksissa.

* Ctrl+Nuoli oikealle

    * Siirtyy seuraavaan jakopisteeseen ja ilmoittaa nykyisen keston.

* Ctrl+Nuoli vasemmalle

    * Siirtyy edelliseen jakopisteeseen ja ilmoittaa nykyisen keston.

* Shift+Nuoli oikealle

    * Tekee lyhyen, neljän sekunninsadasosan siirron eteenpäin toiston aikana ja ilmoittaa nykyisen keston.

* Shift+Nuoli vasemmalle

    * Tekee lyhyen, neljän sekunninsadasosan palautuksen taaksepäin toiston aikana ja ilmoittaa nykyisen keston.

* S

    * Käytetään pysäyttämään toisto ja ilmoittamaan nykyinen kesto.

* Space

    * Jos tallennus on valmis, aloittaa tämän tallennuksen.
    * Jos tallennus on käynnissä, pysäyttää sen ja sijoittaa kursorin alkuun.
    * Jos tiedosto on ladattu, aloittaa toiston.
    * Jos toisto on käynnissä, mahdollistaa tauon tekemisen ja ilmoittaa nykyisen keston.
    * Jos toisto on tauotettu, mahdollistaa toiston aloittamisen uudelleen nykyisestä kohdasta.

* Nuoli ylös

    * Näyttää toistokursorin nykyisen sijainnin.
    * Tämä komento siirtää kursorin myös valinnan alun B-merkin kohdalle ja ilmoittaa tämän merkin sijainnin, jos valinta on tehty.
    * Äänenvoimakkuuden valintaikkunassa puhuu edellisen arvon, joka voidaan yleensä saavuttaa ylänuolella.
    * Tätä arvoa ei puhuta oletusarvoisesti.

* NVDA+H

    * Avaa nykyisen lisäosan ohjeen.

## Yhteensopivuus ##

* Tämä lisäosa on yhteensopiva NVDA-versioiden 2019.3 ja sitä uudempien kanssa.

## Muutokset versiossa 20240327.0.0

* Korjattu virhe, joka aiheutti lokivirheen laajennuksia uudelleenladattaessa; kiitos Robille nvda-addons-postituslistalta;

## Muutokset versiossa 20240326.0.0

* Päivitetty yhteensopivuus nvda-2024.1-versiolle.;
* Poistettu latauslinkki luettelotiedostosta, tulevien päivitysten latauslinkki on jatkossa saatavilla vain lisäosakaupasta.

## Muutokset versiossa 20231229.0.0 ##

* Lisätty taaksepäin yhteensopiva toteutus tukemaan "puhe pyydettäessä" -tilaa, joka tulee pian saataville nvda-2024.1-version myötä.

## Muutokset versiossa 20231007.0.0 ##

* Jakopisteiden asettamisen ja leikkausominaisuuksien ikkunan avaamisen ("Ctrl+N") jälkeen lisätty saavutettavuus tämän ikkunan otsikkoon ilmoittamalla osan indeksi.
* Lukutilassa, kun valintojen alku- tai loppumerkkejä on siirretty alfanumeerisen näppäimistön näppäimillä 1–6, lisätty automaattinen toiston aloitus uudesta sijainnista;
* Korjattu virhe, joka ilmeni tarkistettaessa jäljellä olevaa aikaa näppäinyhdistelmällä "control+shift+r" raidan alusta.

## Muutokset versiossa 20230728.0.0 ##

* Sovellettu flake8- ja mypy-sääntöjä koodiin;
* Muutettu pienin tuettu NVDA-versio versioksi 2019.3 Python 3:ssa esiteltyjen annotaatioiden tukemiseksi.

## Muutokset versiossa 20230607.0.0 ##

* Lisätty seuraavat työvuo-prosessit:
 * auto-update-translations - käännösten automaattiseen päivittämiseen NVDA:n käännösjärjestelmästä.
 * release-on-tag..yaml: lisäosan kääntämiseen ja julkaisemiseen heti, kun uusi tagi pushetaan;
 * manual-release.yaml: lisäosan uusien versioiden manuaaliseen kääntämiseen ja julkaisemiseen.
* Päivitetty käännökset.

## Muutokset versiossa 20230508.0.0 ja uudemmissa ##

* Muutettu versionumero, NVDA:n vähimmäisversio ja latauslinkki kaupan käytäntöjen/vaatimusten mukaisesti.

## Muutokset versiossa 20.12 ##

* Puheen pysäyttäminen tallennuksen ja toiston aikana mp3DirectCutin uusimmilla versioilla;
* Korjattu jäljellä olevan ajan lukeminen uusilla NVDA-versioilla, jotka käyttävät Python 3 -versiota.

## Muutokset versiossa 19.02 ##

* Lisätty lisäosan määritykset asetuspaneeliin, joka on ollut käytettävissä nvda 2018.2 -versiosta lähtien;
* Muutettu versionumerointi muotoon VV.KK (vuosi 2 numerolla, jota seuraa piste ja kuukausi 2 numerolla);
* Lisätty yhteensopivuus lisäosien uuden versiointimuodon kanssa, joka tuli käyttöön nvda 2019.1 -versiosta lähtien.

## Muutokset versiossa 4.0 ##

* Lisätty lisäosan yhteensopivuus sekä Python 2.7- että Python 3 -versioiden kanssa;
* Korjattu virhe lisäosan poluissa, jotka sisältävät muita kuin ASCII-merkkejä.

## Muutokset versiossa 3.0 ##

* Käytetty gui.guiHelper-moduulia varmistamaan lisäosan määritysikkunan oikea ulkoasu;
* Käytetty format-metodia %s-muotoilun sijasta merkkijonojen muotoiluun;
* Käytetty toteutusohjeiden noudattamista.

## Muutokset versiossa 2.3 ##

* Lisätty GPL-lisenssi lisäosaan;
* Muutettu valinnan lopun ilmoittavan skriptin pikanäppäin muodosta Ctrl + Shift + N muotoon Ctrl + Shift + E, koska Ctrl + Shift + N ei toimi mp3DirectCutin uusimpien versioiden kanssa;
* Lisätty skripti vahvistamaan, että valinta on peruttu näppäinyhdistelmällä 'Ctrl+r';
* Tehty joitakin korjauksia appModule-tiedoston 'mp3directcut.py' koodiin.

## Muutokset versiossa 2.2 ##

* Korjattu skriptit, jotka ilmoittavat valintamerkkien sijainnit.

## Muutokset versiossa 2.1.1 ##

* Poistettu kokonaisajan ilmoittava skripti ja lisätty tämä tieto kuluneen ajan ilmoittavaan skriptiin;
* Lisätty mahdollisuus ottaa käyttöön tai poistaa käytöstä välilyöntinäppäimeen liittyvät ilmoitukset moduulin asetuksissa, erillään muista ilmoituksista;
* Lisätty mahdollisuus ottaa käyttöön tai poistaa käytöstä valintamerkkien sijoittamiseen liittyvät ilmoitukset moduulin asetuksissa;
* Lisätty nykyisen osan ilmoittaminen liikuttaessa jakopisteiden välillä;
* Korjattu pystysuuntaisiin näppäimiin liittyvät ilmoitukset;
* Lisätty skripti nykyisen lisäosan ohjeen avaamiseksi näppäinyhdistelmällä 'NVDA+H';
* Siirretty lisäosan asetukset NVDA:n Työkalut-valikosta Asetukset-valikkoon.

## Muutokset versiossa 2.1 ##

* Lisätty skripti puhumaan siirtyminen seuraavaan jakopisteeseen näppäinyhdistelmällä Control+Nuoli oikealle;
* Lisätty skripti puhumaan siirtyminen edelliseen jakopisteeseen näppäinyhdistelmällä Control+Nuoli vasemmalle;
* Lisätty skripti puhumaan siirtyminen 4 sekunninsadasosaa eteenpäin näppäinyhdistelmällä Shift+Nuoli oikealle;
* Lisätty skripti puhumaan siirtyminen 4 sekunninsadasosaa taaksepäin näppäinyhdistelmällä Shift+Nuoli vasemmalle;
* Korjattu lisäosan kuvaus muodosta 'for mp3DirectCut' muotoon 'mp3DirectCut'.

## Muutokset versiossa 2.0 ##

* Lisätty skripti jäljellä olevan ajan selvittämiseksi näppäinyhdistelmällä 'Control Shift R';
* Korjattu kestojen lukeminen silloin, kun ne sisältävät tunteja;
* Lisätty mahdollisuus erottaa sekunnin tuhannesosat tai sadasosat toisistaan.

## Muutokset versiossa 1.1 ##

* Lisätty mahdollisuus sisällyttää mp3DirectCut-luokka syöte-eleisiin (Input Gestures);

    * Ne ovat näkyvissä vain mp3DirectCut-ohjelmistoa käytettäessä.

* Lisätty mahdollisuus ottaa käyttöön tai poistaa käytöstä automaattiset viestit NVDA:n työkalut-valikon kohdassa 'mp3DirectCut-asetukset';

## Muutokset versiossa 1.0 ##

* Alkuperäinen versio.
