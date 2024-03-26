# mp3DirectCut #

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* download [stabil version][1]
* Download [udviklingsversion][2]

# Præsentation #

Denne tilføjelse forbedrer tilgængeligheden af softwaren mp3DirectCut med
NVDA.

Det er blevet testet med versioner af mp3DirectCut fra 212 op til 222.

## Genvejstaster ##

Denne tilføjelsespakke tilbyder følgende kommandoer, som du kan ændre ved at
gå til menuen Indstillinger / Input-bevægelser og lede efter kategorien
"mp3DirectCut":

* B

    * Bruges til at bekræfte korrekt placering af markøren for begyndelsen
      af markering B.

* Ctrl+Shift+B

    * Bruges til at angive positionen af markøren for begyndelsen af
      markering B.
    * Dobbelttryk giver dig varigheden af markeringen.

* Ctrl+Shift+D

    * Angiver varigheden fra begyndelsen af filen til den aktuelle position
      for afspilningsmarkøren.
    * Dobbelttryk giver dig den samlede varighed.

* Ctrl+R

    * Bekræfter, at valget er blevet annulleret.

* Ctrl+Shift+R

    * Angiver den resterende tid fra den aktuelle position af
      afspilningsmarkøren til slutningen af filen.

* Ctrl+Shift+E

    * Bruges til at angive positionen af markøren for slutningen af
      markering N.
    * Dobbelttryk angiver opsummerede positioner for B og N, og varigheden
      af markeringen.

* Ctrl+Shift+P

    * Angiver den del af filen, som du aktuelt arbejder med, samt det
      samlede antal dele i den aktuelle fil.

* Ctrl+Shift+mellemrum

    * Bruges til at bestemme vu-meterets aktuelle niveau under optagelse
      (lydstyrken).
    * Dobbelttryk nulstiller.

* Pil ned

    * Lader dig se den aktuelle position for afspilningshovedet.
    * Denne kommando placerer også markøren ved slutningen af markering N,
      og angiver positionen for markeringen, hvis en markering er lavet.
    * I lydstyrkedialogboksen vil du få næste værdi oplyst, som generelt kan
      nås med pil ned.
    * Denne værdi er ikke oplyst som standard.

* Slut

    * Flytter afspilningsmarkøren til slutningen af den aktuelle fil og
      oplyser den samlede tid.

* Hjem

    * Flytter afspilningsmarkøren til begyndelsen af den aktuelle fil.

* Venstre pil

    * Spoler ét sekund tilbage under afspilning og opkyser den samlede tid.
    * Denne varighed kan konfigureres i mulighederne for mp3directcut.

* Slut

    * Bruges til at bekræfte korrekt placering af markøren for slutningen af
      markeringen N.

* Side ned

    * Spoler hurtigt 10 sekunder fremad og oplyser den samlede tid.
    * Denne varighed kan konfigureres i mulighederne for mp3directcut.

* Side op

    * Spoler hurtigt 10 sekunder tilbage og oplyser den samlede tid.
    * Denne varighed kan konfigureres i mulighederne for mp3directcut.

* R

    * Gør klar til optagelse, således du kan trykke mellemrum for at
      begynde.

* Højre pil

    * Spoler ét sekund fremad under afspilning og opkyser den samlede tid.
    * Denne varighed kan konfigureres i mulighederne for mp3directcut.

* Ctrl+højre pil

    * Flytter til næste splitpunkt, mens den aktuelle varighed oplys.

* Ctrl+venstre pil

    * Flytter til det forrige splitpunkt, mens den aktuelle varighed
      oplyses.

* Skift+højre pil

    * Spoler fire hundrededele fremad af ét sekund under afspilning og
      opkyser den samlede tid.

* Skift+venstre pil

    * Spoler fire hundrededele tilbage af ét sekund under afspilning og
      opkyser den samlede tid.

* S

    * Bruges til at stoppe aflytningen og oplyse den aktuelle varighed.

* Mellemrum

    * Hvis optagelsen er klar, start denne optagelse.
    * Hvis en optagelse er i gang, stoppes denne og markøren placeres i
      begyndelsen.
    * Hvis en fil er indlæst, start afspilning.
    * Hvis en afspilning er undervejs, vil dette sætte afspilningen på pause
      og oplyse den aktuelle position.
    * Hvis afspilningen er stoppet, vil dette genoptage afspilningen fra den
      aktuelle position.

* Pil op

    * Lader dig se den aktuelle position for afspilningshovedet.
    * Dette placerer markøren ved begyndelsen af markering B og oplyse
      varrigheden, hvis du har foretaget en fuldstændig markering.
    * I dialog for lydstyrke, oplys forrig værdi. Dette gøres typisk med pil
      op.
    * Denne værdi er ikke oplyst som standard.

* NVDA+h

    * Lader os åbne hjælpen for den nuværende tilføjelse.

## Kompatibilitet ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

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

## Ændringer for version 20.12 ##

* Afbryder tale under optagelse og afspilning i seneste version af
  mp3directcut;
* Fast læsning af resterende tid for nye versioner af NVDA, der bruger
  Python 3.

## Ændringer for version 19.02 ##

* Tilføjet konfigurationen af tilføjelsen til NVDAs indstillingspanel, der
  har været tilgængeligt siden NVDA 2018.2.
* Ændret versionsnummerering til åå.MM (År i 2 cifre efterfulgt af et
  punktum, efterfulgt af måneden på 2 cifre);
* Tilføjede kompatibilitet med det nye versionsformat der benyttes i
  tilføjelser, der blev aktuelt siden NVDA 2019.1.

## Ændringer til version 4.0 ##

* Tilføjet kompatibilitet med Python 2.7 og 3;
* Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
  non-ASCII-tegn.

## Ændringer for version 3.0 ##

* Brugte gui.guiHelper modulet til at sikre korrekt udseende af
  tilføjelsespakkens konfigurationsdialog;
* Brugt format i stedet for%s for formaterede strenge;
* Brugte overholdelse af retningslinjer for implementering.

## Ændringer for version 2.3 ##

* Tilføjet GPL-licensen til tilføjelsen;
* Ændret genvejen af scriptet, der giver slutningen af markeringen fra
  CTRL+Skift+N til CTRL+Skift+E, fordi Ctrl+Skift+N ikke virker med de
  nyeste versioner af mp3DirectCut;
* Tilføjet et script for at bekræfte, at udvælgelsen er blevet annulleret
  med 'CTRL+R';
* Lavede nogle rettelser til modulet mp3directcut.py.

## Ændringer for version 2.2 ##

* rettelse af de scripts til at angive udvælgelsesmarkørens position.

## Ændringer for version 2.1.1 ##

* Fjernede det script der angav tid i alt, og tilføjede denne funktion til
  scriptet der bearbejdede resterende tid.
* Tilføjet muligheden for at aktivere eller deaktivere meddelelser relateret
  til mellemrumstasten i modulets konfiguration, adskilt fra andre
  meddelelser;
* Tilføjet muligheden for at aktivere eller deaktivere annonceringen af
  placeringen af udvælgelsesmarkørernei til modulets konfiguration;
* Tilføje annonceringen af den aktuelle del, når du flytter gennem de
  skærende punkter;
* Korrektion af annonceringer relateret til lodret taster;
* Tilføje et script for at åbne hjælp fra det aktuelle tilføjelsesprogram
  med 'NVDA + H';
* Menuen tilknytted tilføjelsespakken befinder sig nu i NVDAs menu under
  indstillinger;

## Ændringer for version 2.1 ##

* Tilføjede et script til at annoncéreflytte næste opsplitningspunkt med
  CTRL+højrepil;
* Tilføjede et script til at annoncerer når der flyttes til det forrige
  opsplitningspunkt med CTRL+Venstre pil;
* Tilføjede et script til at annoncerer 4 hundrededele af et sekund forude,
  med Shift+højre pil;
* Tilføjede et script til at annoncerer 4 hundrededele af et sekund bagude,
  med Shift+venstre pil;
* Rettelse af tilføjelsespakkens opsummering 'for mp3DirectCut' til
  'mp3DirectCut'.

## Ændringer for version 2.0 ##

* Tilføjede et script for at kende den resterende tid med CTRL+Skift+R;
* Rettede et problem med at læse varigheden, herunder timer;
* Tilføjet mulighed for at differentiere tusindedele eller hundrededele af
  sekunder;

## Ænderinger for version 1.1 ##

* Tilføjet muligheden for at inkludere mp3DirectCut-kategorien i dialogen
  "Håndter kommandoer";

    * De vil kun være synlige under brug af mp3DirectCut-softwaren.

* Tilføjet muligheden for at aktivere eller deaktivere automatiske beskeder,
  i værktøjsmenuen i NVDA, punkt 'mp3DirectCut-konfiguration';

## Ændringer for version 1.0 ##

* Oprindelige version.

[[!tag dev stable]]

[1]:
https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29/mp3DirectCut-20231229.0.0.nvda-addon

[2]:
https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29-beta/mp3DirectCut-20231229.0.1.nvda-addon
