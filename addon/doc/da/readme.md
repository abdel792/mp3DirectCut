# mp3DirectCut

* Forfatter(e): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Præsentation #

Denne tilføjelse forbedrer tilgængeligheden af programmet mp3DirectCut ved brug sammen med NVDA.

Den er blevet testet med versionerne 212 til 233 af mp3DirectCut.

## Tastaturgenveje ##

Denne tilføjelse tilbyder følgende kommandoer:

* B

    * Bruges til at bekræfte, at markøren for begyndelsen af markeringen B er placeret korrekt.

* Ctrl+Shift+B

    * Bruges til at oplyse placeringen af markøren for begyndelsen af markeringen B.
    * Et dobbelttryk oplyser markeringens varighed.

* Ctrl+Shift+D

    * Oplyser varigheden fra filens begyndelse til afspilningsmarkørens aktuelle position.
    * Et dobbelttryk oplyser den samlede varighed.

* Ctrl+R

    * Bekræfter, at markeringen er blevet annulleret.

* Ctrl+Shift+R

    * Oplyser den resterende tid fra afspilningsmarkørens aktuelle position til filens slutning.

* Ctrl+Shift+E

    * Bruges til at oplyse placeringen af markøren for slutningen af markeringen N.
    * Et dobbelttryk oplyser placeringerne af markørerne B og N samt markeringens varighed.

* Ctrl+Shift+P

    * Oplyser nummeret på den aktuelle del samt det samlede antal dele i den aktuelle fil.

* Ctrl+Shift+Space

    * Bruges til at bestemme det aktuelle niveau på VU-meteret under optagelse.
    * Et dobbelttryk nulstiller det.

* Down Arrow

    * Oplyser den aktuelle position for afspilningsmarkøren.
    * Denne kommando flytter også markøren til placeringen af markøren for slutningen af markeringen N og oplyser dens placering, hvis der er foretaget en markering.
    * I dialogboksen for lydstyrke oplyses den næste værdi, som normalt kan vælges med Pil ned.
    * Denne værdi oplyses ikke som standard.

* End

    * Flytter afspilningsmarkøren til slutningen af den aktuelle fil og oplyser den samlede varighed.

* Home

    * Flytter afspilningsmarkøren til begyndelsen af den aktuelle fil.

* Left Arrow

    * Springer ét sekund tilbage under afspilning og oplyser den aktuelle tid.
    * Denne varighed kan konfigureres i indstillingerne for mp3DirectCut.

* N

    * Bruges til at bekræfte, at markøren for slutningen af markeringen N er placeret korrekt.

* Page Down

    * Springer 10 sekunder frem under afspilning og oplyser den aktuelle tid.
    * Denne varighed kan konfigureres i indstillingerne for mp3DirectCut.

* Page Up

    * Springer 10 sekunder tilbage under afspilning og oplyser den aktuelle tid.
    * Denne varighed kan konfigureres i indstillingerne for mp3DirectCut.

* R

    * Gør en optagelse klar og oplyser, at du kan trykke på mellemrumstasten for at starte.

* Right Arrow

    * Springer ét sekund frem under afspilning og oplyser den aktuelle tid.
    * Denne varighed kan konfigureres i indstillingerne for mp3DirectCut.

* Ctrl+Right Arrow

    * Flytter til det næste opdelingspunkt og oplyser den aktuelle tid.

* Ctrl+Left Arrow

    * Flytter til det forrige opdelingspunkt og oplyser den aktuelle tid.

* Shift+Right Arrow

    * Springer fire hundrededele af et sekund frem under afspilning og oplyser den aktuelle tid.

* Shift+Left Arrow

    * Springer fire hundrededele af et sekund tilbage under afspilning og oplyser den aktuelle tid.

* S

    * Stopper afspilningen og oplyser den aktuelle tid.

* Space

    * Hvis optagelsen er klar, starter den optagelsen.
    * Hvis en optagelse er i gang, stopper den optagelsen og placerer markøren ved begyndelsen.
    * Hvis en fil er indlæst, starter den afspilningen.
    * Hvis afspilning er i gang, sætter den afspilningen på pause og oplyser den aktuelle tid.
    * Hvis afspilningen er sat på pause, genoptager den afspilningen fra den aktuelle position.

* Up Arrow

    * Oplyser den aktuelle position for afspilningsmarkøren.
    * Denne kommando flytter også markøren til placeringen af markøren for begyndelsen af markeringen B og oplyser dens placering, hvis der er foretaget en markering.
    * I dialogboksen for lydstyrke oplyses den forrige værdi, som normalt kan vælges med Pil op.
    * Denne værdi oplyses ikke som standard.

* NVDA+H

    * Åbner hjælpen til den aktuelle tilføjelse.

## Kompatibilitet ##

* Denne tilføjelse er kompatibel med NVDA-versioner fra 2019.3 og nyere.

## Ændringer i 20240327.0.0

* Rettede en fejl, som forårsagede en logfejl ved genindlæsning af plugins, takket være Rob fra mailinglisten nvda-addons;

## Ændringer i 20240326.0.0

* Opdaterede kompatibiliteten med nvda-2024.1.;
* Fjernede downloadlinket fra readme-filen. Downloadlinket til fremtidige opdateringer vil fremover kun være tilgængeligt via Tilføjelsesbutikken.

## Ændringer i 20231229.0.0 ##

* Tilføjede en bagudkompatibel implementering for at understøtte tilstanden "Tale efter behov" (Speak on Demand), som snart bliver tilgængelig i nvda-2024.1.

## Ændringer i 20231007.0.0 ##

* Efter placering af klippepunkterne og åbning af vinduet med klippeegenskaber ved hjælp af "Ctrl+N" blev tilgængeligheden forbedret ved at få vinduets titel til at oplyse delens indeks.
* I afspilningstilstand starter afspilningen nu automatisk fra den nye position, efter at begyndelses- eller slutmarkøren for markeringen er flyttet med tasterne 1 til 6 på det numeriske tastatur.
* Rettede en fejl, der opstod ved forespørgsel på den resterende tid med "Control+Shift+R" fra begyndelsen af sporet.

## Ændringer i 20230728.0.0 ##

* Anvendte reglerne fra flake8 og mypy på koden;
* Ændrede den mindste understøttede NVDA-version til 2019.3 for at understøtte annotationer, som blev introduceret i Python 3.

## Ændringer i 20230607.0.0 ##

* Tilføjede følgende arbejdsgange:
 * auto-update-translations - til automatisk opdatering af oversættelser fra NVDAs oversættelsessystem.
 * release-on-tag..yaml: til at bygge og udgive tilføjelsen automatisk, så snart et nyt tag bliver oprettet;
 * manual-release.yaml: til manuelt at bygge og udgive nye versioner af tilføjelsen.
* Opdaterede oversættelserne.

## Ændringer for version 20230508.0.0 og nyere ##

* • Ændrede versionsnummeret, den minimale NVDA-version og downloadlinket i overensstemmelse med Tilføjelsesbutikkens krav.

## Ændringer for version 20.12 ##

* Stopper tale under optagelse og afspilning i de nyeste versioner af mp3DirectCut;
* Rettede oplæsningen af resterende tid i nye versioner af NVDA, der anvender Python 3.

## Ændringer for version 19.02 ##

* Tilføjede tilføjelsens indstillinger til indstillingspanelet, som har været tilgængeligt siden NVDA 2018.2;
* Ændrede versionsnummereringen til YY.MM (året med 2 cifre efterfulgt af et punktum og derefter måneden med 2 cifre);
* Tilføjede kompatibilitet med det nye versionsformat for tilføjelser, som blev indført i NVDA 2019.1.

## Ændringer for version 4.0 ##

* Tilføjede kompatibilitet med både Python 2.7 og Python 3;
* Rettede en fejl med stier til tilføjelsen, som indeholder tegn uden for ASCII.

## Ændringer for version 3.0 ##

* Anvendte modulet gui.guiHelper for at sikre korrekt visning af dialogboksen til konfiguration af tilføjelsen;
* Anvendte format i stedet for %s til formaterede strenge;
* Tilpassede implementeringen, så den følger de gældende udviklingsretningslinjer.

## Ændringer for version 2.3 ##

* Tilføjede GPL-licensen til tilføjelsen;
* Ændrede genvejen til scriptet, der oplyser slutningen af markeringen, fra Ctrl + Shift + N til Ctrl + Shift + E, da Ctrl + Shift + N ikke fungerer med de nyeste versioner af mp3DirectCut;
* Tilføjede et script, der bekræfter, at markeringen er blevet annulleret, med 'Ctrl+R';
* Foretog nogle rettelser i koden til appModule 'mp3directcut.py'.

## Ændringer for version 2.2 ##

* Rettede de scripts, der oplyser markeringernes placering.

## Ændringer for version 2.1.1 ##

* Fjernede scriptet, der oplyser den samlede varighed, og tilføjede i stedet denne information til scriptet, der oplyser den forløbne tid;
* Tilføjede mulighed for at aktivere eller deaktivere meddelelser relateret til mellemrumstasten i modulets konfigurationsindstillinger, uafhængigt af de øvrige meddelelser;
* Tilføjede mulighed for at aktivere eller deaktivere meddelelser om placeringen af markeringsmarkørerne i modulets konfigurationsindstillinger;
* Tilføjede oplysning om den aktuelle del ved flytning mellem klippepunkterne;
* Rettede meddelelser relateret til piletasterne;
* Tilføjede et script til at åbne hjælpen til den aktuelle tilføjelse med 'NVDA+H';
* Flyttede tilføjelsens konfigurationsmenu fra menuen "Funktioner" til menuen "Indstillinger" i NVDA.

## Ændringer for version 2.1 ##

* Tilføjede et script, der oplyser flytning til det næste opdelingspunkt med Control+Right Arrow;
* Tilføjede et script, der oplyser flytning til det forrige opdelingspunkt med Control+Left Arrow;
* Tilføjede et script, der oplyser flytning 4 hundrededele af et sekund frem med Shift+Right Arrow;
* Tilføjede et script, der oplyser flytning 4 hundrededele af et sekund tilbage med Shift+Left Arrow;
* Rettede tilføjelsens beskrivelse fra 'for mp3DirectCut' til 'mp3DirectCut'.

## Ændringer for version 2.0 ##

* Tilføjede et script til at oplyse den resterende tid med 'Control Shift R';
* Rettede oplæsning af tidsangivelser, der omfatter timer;
* Tilføjede mulighed for at skelne mellem tusindedele og hundrededele af et sekund.

## Ændringer for version 1.1 ##

* Tilføjede mulighed for at inkludere kategorien mp3DirectCut under "Inputbevægelser";

    * Den vil kun være synlig, når programmet mp3DirectCut er i brug.

* Tilføjede mulighed for at aktivere eller deaktivere automatiske meddelelser via menuen "Funktioner" i NVDA under punktet "Konfiguration af mp3DirectCut";

## Ændringer for version 1.0 ##

* Første version.
