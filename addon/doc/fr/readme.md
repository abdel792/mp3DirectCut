# mp3DirectCut #

*	 Auteur(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Télécharger [version stable][1]
*	 Télécharger [version de développement][2]

# Présentation #

Ce module complémentaire permet d'améliorer l'accessibilité du logiciel
mp3DirectCut avec NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Raccourcis-clavier ##

This addon offers the following commands:

*	B
	*	Used to confirm correct placement of the marker of the beginning of the selection B.
*	Ctrl+Shift+B
	*	Used to indicate the position of the marker of the beginning of selection B.
	*	Double pressure lets give you the duration of the selection.
*	Ctrl+Shift+D
	*	Gives the duration from the beginning of the file to the current position of the playback cursor.
	*	Double pressure lets give you the total duration.
*	Ctrl+R
	*	Confirms that the selection has been canceled.
*	Ctrl+Shift+R
	*	Gives the time remaining from the current position of the playback cursor to the end of the file.
*	Ctrl+Shift+E
	*	Used to indicate the position of the marker of the end of selection N.
	*	Double pressure gives recapitulatif positions B and N, and the duration of the selection.
*	Ctrl+Shift+P
	*	Give the reference of the actual part and the total number of parts in the current file.
*	Ctrl+Shift+Space
	*	Used to determine the current level of the vu-meter, during recording.
	*	Double pressure reset it.
*	Down Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the end of selection N, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the next value that can be reached generally with downArrow.
	*	This value is not vocalized default.
*	End
	*	Moves the playback cursor at the end of the current file and give the total time.
*	Home
	*	Moves the playback cursor at the beginning of the current file.
*	Left Arrow
	*	Lets make a brief return back of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	N
	*	Used to confirm correct placement of the marker of the end of the selection N.
*	Page Down
	*	Lets make a leap forward of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Page Up
	*	Lets make a return back of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	R
	*	Allows to prepare a record and whether you can press spacebar to start.
*	Right Arrow
	*	Lets do a brief forward of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Ctrl+Right Arrow
	*	Moves to the next splitting point, while giving the current duration.
*	Ctrl+Left Arrow
	*	Moves to the previous splitting point, while giving the current duration.
*	Shift+Right Arrow
	*	Lets do a brief forward of four hundredths of seconds during playback, while giving the current duration.
*	Shift+Left Arrow
	*	Lets do a brief backwards of four hundredths of seconds during playback, while giving the current duration. 
*	S
	*	Used to stop the reading and give the current duration.
*	Space
	*	If the recording is ready, start this recording.
	*	If a recording is in progress, stop it by positioning the cursor at the beginning.
	*	If a file is loaded, start the reading.
	*	If a read is in progress, allows to do a pause by giving current duration.
	*	If read is paused, allows to restart the reading from the current location.
*	Up Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the beginning of selection B, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the previous value that can be reached generally with upArrow.
	*	This value is not vocalized default.
*	NVDA+H
	*	Lets open the help of the current add-on.

## Change for version 3.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   addon's configuration dialog;
*	 Used format instead of %s for formatted strings;
*	 Used compliance with guidelines for implementation.

## Change for version 2.3 ##

*	 Added the GPL license to the addon;
*	 Changed the shortcut of the script giving the end of selection from Ctrl
   + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work
   with the latest versions of mp3DirectCut;
*	 Added a script to confirm that the selection has been canceled with
   'Ctrl+r';
*	 Maked some correction in the code of the appModule 'mp3directcut.py'.

## Changements pour la version 2.2 ##

*	 Correction des scripts donnant les emplacements des marqueurs de
   sélection.

## Changements pour la version 2.1.1 ##

*	 Suppression du script permettant de donner la durée totale et ajout de
   cette information au script donnant le temps écoulé;
*	 Ajout de la possibilité d'activer ou non les annonces liées à la touche
   espace dans les options de configuration du module, distinctement des
   autres annonces;
*	 Ajout de la possibilité d'activer ou non l'annonce du bon placement des
   marqueures de sélection dans les options de configuration du module;
*	 Ajout de l'annonce de la plage courante lors du déplacement parmi les
   points de coupe;
*	 Correction des annonces liées aux touches verticales;
*	 Ajout d'un script pour ouvrir l'aide du module complémentaire accessible
   grâce au racourci-clavier "NVDA+H";
*	 Déplacement du menu de configuration du module complémentaire du menu
   Outils vers le menu Préférences de NVDA.

## Changements pour la version 2.1 ##

*	 Ajout d'un script pour vocaliser le déplacement vers le point de coupe
   suivant avec Contrôle+Flèche droite;
*	 Ajout d'un script pour vocaliser le déplacement vers le point de coupe
   précédent avec Contrôle+Flèche gauche;
*	 Ajout d'un script pour vocaliser le déplacement de 4 centièmes de
   secondes en avant, avec Maj+Flèche droite;
*	 Ajout d'un script pour vocaliser le déplacement de 4 centièmes de
   secondes en arrière, avec Maj+Flèche gauche;
*	 Corection du summary de l'addon de "Pour mp3DirectCut" en "mp3DirectCut".

## Changements pour la version 2.0 ##

*	 Ajout d'un script pour connaître la durée restante avec "Contrôle + Maj +
   R";
*	 Correction de la lecture des durées comportant des heures;
*	 Ajout de la possibilité de différencier les millièmes ou centièmes de
   secondes.

## Changements pour la version 1.1 ##

*	 Ajout de la possibilité de faire figurer les commandes de l'addon parmi les gestes de commandes, dans la catégorie "mp3DirectCut";
*	 Elles ne seront visible que durant une utilisation du logiciel mp3DirectCut.
*	 Ajout de la possibilité d'activer ou de désactiver les messages automatiques dans le menu outils de NVDA, item "Configuration de mp3DirectCut";

## Changements pour la version 1.0 ##

*	 Première version

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
