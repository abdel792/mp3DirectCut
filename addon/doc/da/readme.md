# mp3DirectCut #

* Forfattere: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
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

    * Confirms that the selection has been canceled.

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

    * Moves the playback cursor at the end of the current file and give the
      total time.

* Home

    * Moves the playback cursor at the beginning of the current file.

* Left Arrow

    * Lets make a brief return back of one second during playback, while
      giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* N

    * Used to confirm correct placement of the marker of the end of the
      selection N.

* Page Down

    * Lets make a leap forward of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Page Up

    * Lets make a return back of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* R

    * Allows to prepare a record and whether you can press spacebar to
      start.

* Right Arrow

    * Lets do a brief forward of one second during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Ctrl+Right Arrow

    * Moves to the next splitting point, while giving the current duration.

* Ctrl+Left Arrow

    * Moves to the previous splitting point, while giving the current
      duration.

* Shift+Right Arrow

    * Lets do a brief forward of four hundredths of seconds during playback,
      while giving the current duration.

* Shift+Left Arrow

    * Lets do a brief backwards of four hundredths of seconds during
      playback, while giving the current duration.

* S

    * Used to stop the reading and give the current duration.

* Space

    * If the recording is ready, start this recording.
    * If a recording is in progress, stop it by positioning the cursor at
      the beginning.
    * If a file is loaded, start the reading.
    * If a read is in progress, allows to do a pause by giving current
      duration.
    * If read is paused, allows to restart the reading from the current
      location.

* Up Arrow

    * Lader dig se den aktuelle position for afspilningshovedet.
    * This command also position the cursor at the location of the marker of
      the beginning of selection B, while giving the location of this marker
      if a selection has been made.
    * In the volume dialog box, vocalise the previous value that can be
      reached generally with upArrow.
    * Denne værdi er ikke oplyst som standard.

* NVDA+H

    * Lets open the help of the current add-on.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2016.4
  until 2020.3 or higher.

## Change for version 20.12 ##

* Stop speech during recording and reading for the latest versions of
  mp3directcut;
* Fixed reading remaining time for new versions of NVDA using Python 3.

## Change for version 19.02 ##

* Added the add-on's configuration in the settings panel available since
  nvda 2018.2;
* Changed version numbering using YY.MM (The year in 2 digits, followed by a
  dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared
  since nvda 2019.1.

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

* Added the ability to include the mp3DirectCut category into the Input
  Gestures;

    * They will be visible only during use of the mp3DirectCut software.

* Added the ability to enable or disable automatic messages, in the tools
  menu of NVDA, item 'mp3DirectCut configuration';

## Ændringer for version 1.0 ##

* Oprindelige version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
