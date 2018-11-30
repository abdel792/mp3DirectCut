# mp3DirectCut #

*	 Forfattere: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 download [stabil version][1]
*	 Download [udviklingsversion][2]

# Præsentation #

Denne tilføjelse forbedrer tilgængeligheden af softwaren mp3DirectCut med
NVDA.

Det er blevet testet med versioner af mp3DirectCut fra 212 op til 222.

## Genvejstaster ##

Denne tilføjelsespakke tilbyder følgende kommandoer, som du kan ændre ved at
gå til menuen Indstillinger / Input-bevægelser og lede efter kategorien
"mp3DirectCut":

*	B
	*	Brugt til at bekræfte korrekt placering af markøren ved begyndelsen af markering B.
*	Ctrl+Skift+B
	*	Brugt til at indikere positionen af markøren af begyndelsen for markering B.
	*	Tryk to gange for at få varigheden af markeringen oplyst.
*	Ctrl+skift+D
	*	Oplyser varigheden fra den aktuelle  fil til den aktuelle position af afspilningsmarkøren.
	*	Double pressure lets give you the total duration.
*	Ctrl+skift+R
	*	GOplyser den resterende tid fra afspilningsmarkørens aktuelle position til filens slutning.
*	Ctrl+skift+E
	*	Brugt til at oplyse positionen af markøren af slutningen af det markerede ved markering N.
	*	 Tryk to gange for at få begge positioner oplyst B og N, og the varigheden af det valgte.
*	Ctrl+skift+P
	*	Referere den aktuelle del og giver antallet af dele i hele filen.
*	Ctrl+skift+mellemrum
	*	Brugt til at oplyse det aktuelle niveau af Vu-meteret.
	*	Tryk to gange for at nulstille.
*	Pil ned
	*	Lader dig se den aktuelle position af afspillingen.
	*	Denne kommando placerer også markøren ved markøren der viser slutningen på markering N, og giver positionen af denne markør hvis en markering er foretaget.
	*	I dialogboksen til lydstyrke, annoncérer den næste værdi der kan nåes, generelt ved brug af pil ned.
	*	Denne værdi er ikke meddelt som standard.
*	End
	*	Flytter afspilningsmarkøren til slutningen af filen og oplyser afspilningens varighed.
*	Hjem
	*	Flytter afspilningsmarkøren til starten af filen.
*	Venstre pil
	*	Spoler et sekund tilbage og annoncérer den aktuelle varighed.
	*	Varigheden kan indstilles i indstillingerne for mp3DirectCut.
*	N
	*	Brugt til at bekræfte den korrekte placering af slutningen på markering N.
*	Side Ned
	*	Lader dig springe 10 sekunder frem og oplyser den aktuelle varighed.
	*	Varigheden kan indstilles i indstillingerne for mp3DirectCut.
*	Side Op
	*	Lader dig springe 10 sekunder tilbage og oplyser den aktuelle varighed.
	*	Varigheden kan indstilles i indstillingerne for mp3DirectCut.
*	R
	*	Lader dig forberede en optagelse. Tryk mellemrum for at begynde optagelsen.
*	Højre pil
	*	Lader dig gå fremad et sekund og oplyser den aktuelle varighed.
	*	Varigheden kan indstilles i indstillingerne for mp3DirectCut.
*	Ctrl+Højre pil
	*	Flytter til næste opsplitningspunkt og oplyser den aktuelle varighed.
*	Ctrl+venstre pil
	*	Flytter til forrige opsplitningspunkt og oplyser den aktuelle varighed
*	Skift+højre pil
	*	Lader dig springe fremad firehundrededele af et sekund og oplyser den aktuelle varighed.
*	Skift+venstre pil
	*	Lader dig gå tilbage firehundrededele af et sekund og oplyser den aktuelle varighed. 
*	S
	*	Brugt til at stoppe afspilningen og oplyse den aktuelle varighed.
*	Mellemrum
	*	Hvis en optagelse er forberedt, starter denne optagelse.
	*	Hvis en optagelse er i gang, stopper den aktuelle optagelse og placerer markøren i begyndelsen.
	*	Hvis en fil er indlæst, starter afspilning.
	*	Hvis en afspilning er i gang, sætter afspilningen på pause og oplæser den aktuelle varighed.
	*	Hvis afspilningen er sat på pause, genoptager afspilningen fra den aktuelle position.
*	Pil op
	*	Lader dig se den aktuelle position af afspilningen.
	*	Denne kommando placerer også markøren ved markøren der viser slutningen på markering B, og giver positionen af denne markør hvis en markering er foretaget.
	*	I dialogboksen til lydstyrke, annoncérer den forrige værdi der kan nåes, generelt ved brug af pil op.
	*	Denne værdi er ikke meddelt som standard.
*	NVDA+H
	*	Åbner hjælpen for denne tilføjelsespakke.

## Ændringer til version 4.0 ##

*	 Tilføjet kompatibilitet med Python 2.7 og 3;
*	 Rettede en fejl med stier tilhørende tilføjelsespakken der indholder
   non-ASCII-tegn.

## Ændringer for version 3.0 ##

*	 Brugte gui.guiHelper modulet til at sikre korrekt udseende af
   tilføjelsespakkens konfigurationsdialog;
*	 Brugt format i stedet for%s for formaterede strenge;
*	 Brugte overholdelse af retningslinjer for implementering.

## Ændringer for version 2.3 ##

*	 Tilføjet GPL-licensen til tilføjelsen;
*	 Ændret genvejen af scriptet, der giver slutningen af markeringen fra
   CTRL+Skift+N til CTRL+Skift+E, fordi Ctrl+Skift+N ikke virker med de
   nyeste versioner af mp3DirectCut;
*	 Tilføjet et script for at bekræfte, at udvælgelsen er blevet annulleret
   med 'CTRL+R';
*	 Lavede nogle rettelser til modulet mp3directcut.py.

## Ændringer for version 2.2 ##

*	 rettelse af de scripts til at angive udvælgelsesmarkørens position.

## Ændringer for version 2.1.1 ##

*	 Fjernede det script der angav tid i alt, og tilføjede denne funktion til
   scriptet der bearbejdede resterende tid.
*	 Tilføjet muligheden for at aktivere eller deaktivere meddelelser
   relateret til mellemrumstasten i modulets konfiguration, adskilt fra
   andre meddelelser;
*	 Tilføjet muligheden for at aktivere eller deaktivere annonceringen af
   placeringen af udvælgelsesmarkørernei til modulets konfiguration;
*	 Tilføje annonceringen af den aktuelle del, når du flytter gennem de
   skærende punkter;
*	 Korrektion af annonceringer relateret til lodret taster;
*	 Tilføje et script for at åbne hjælp fra det aktuelle tilføjelsesprogram
   med 'NVDA + H';
*	 Menuen tilknytted tilføjelsespakken befinder sig nu i NVDAs menu under
   indstillinger;

## Ændringer for version 2.1 ##

*	 Tilføjede et script til at annoncéreflytte næste opsplitningspunkt med
   CTRL+højrepil;
*	 Tilføjede et script til at annoncerer når der flyttes til det forrige
   opsplitningspunkt med CTRL+Venstre pil;
*	 Tilføjede et script til at annoncerer 4 hundrededele af et sekund forude,
   med Shift+højre pil;
*	 Tilføjede et script til at annoncerer 4 hundrededele af et sekund bagude,
   med Shift+venstre pil;
*	 Rettelse af tilføjelsespakkens opsummering 'for mp3DirectCut' til
   'mp3DirectCut'.

## Ændringer for version 2.0 ##

*	 Tilføjede et script for at kende den resterende tid med CTRL+Skift+R;
*	 Rettede et problem med at læse varigheden, herunder timer;
*	 Tilføjet mulighed for at differentiere tusindedele eller hundrededele af
   sekunder;

## Ænderinger for version 1.1 ##

*	 Tilføjet muligheden for at medtage kategorien mp3DirectCut i Input-bevægelser;
	*	 De vil kun ses under anvendelse af mp3DirectCut software.
*	 Tilføjet muligheden for at aktivere eller deaktivere automatisk beskeder i menuen Værktøjer i NVDA, menupunktet 'mp3DirectCut konfiguration';

## Ændringer for version 1.0 ##

*	 Oprindelige version.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
