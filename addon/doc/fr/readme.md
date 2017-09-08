# mp3DirectCut #

*	 Auteur(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Télécharger [version stable][1]
*	 Télécharger [version de développement][2]

# Présentation #

Ce module complémentaire permet d'améliorer l'accessibilité du logiciel
mp3DirectCut avec NVDA.

Il a été testé avec les versions de mp3DirectCut allant de la 212 jusqu'à la
223.

## Raccourcis-clavier ##

Ce module complémentaire offre les commandes suivantes :

*	B
	*	Permet de confirmer le bon placement du marqueur de début de sélection B.
*	Contrôle+Maj+B
	*	Permet d'indiquer l'emplacement du marqueur de début de sélection B.
	*	Une double pression donne la durée de la sélection.
*	Contrôle+Maj+D
	*	Donne la durée parcourue depuis le début du fichier jusqu'à l'emplacement actuel du curseur de lecture.
	*	Une double pression donne la durée totale.
*	Contrôle+R
	*	Confirme que la sélection a été annulée.
*	Contrôle+Maj+R
	*	Donne la durée restante depuis l'emplacement actuel du curseur de lecture jusqu'à la fin du fichier.
*	Contrôle+Maj+E
	*	Permet d'indiquer l'emplacement du marqueur de fin de sélection N.
	*	Une double pression donne un récapitulatif de l'emplacement des marqueurs B et N, ainsi que la durée de la sélection.
*	Contrôle+Maj+P
	*	Donne la référence de la plage actuelle, ainsi que le nombre totale de plages.
*	Contrôle+Maj+Espace
	*	Permet d'indiquer la valeur actuelle du niveau du vu-mètre.
	*	Une double pression permet de réinitialiser ce niveau.
*	Flèche basse
	*	Permet de donnée la durée en cours.
	*	Si une sélection a été faite, positionne le curseur à l'emplacement du marqueur de fin de sélection N tout en donnant l'emplacement de ce marqueur.
	*	Dans les options du contrôle du volume de mp3directcut, donne la valeur suivante à laquelle on accède habituellement avec flèche basse.
	*	Et qui n'est pas vocalisée par défaut.
*	Fin
	*	Permet de déplacer le curseur de lecture tout à la fin du morceau en cours et donne la durée totale.
*	Début ou Origine
	*	Permet de déplacer le curseur de lecture tout au début du morceau en cours.
*	Flèche gauche
	*	Permet de faire un retour en arrière d'une seconde durant une lecture, tout en donnant la durée en cours.
	*	La durée de ce retour est configurable dans les options de mp3directcut.
*	N
	*	Permet de confirmer le bon placement du marqueur de fin de sélection N.
*	Page suivante
	*	Permet de faire un saut en avant de 10 secondes durant une lecture, tout en donnant la durée en cours.
	*	La durée de ce saut en avant est configurable dans les options de mp3directcut.
*	Page précédente
	*	Permet de faire un saut en arrière de 10 secondes durant une lecture, tout en donnant la durée en cours.
	*	La durée de ce saut en arrière est configurable dans les options de mp3directcut.
*	R
	*	Permet de préparer un enregistrement et indique si vous pouvez appuyer sur espace pour le commencer.
*	Flèche droite
	*	Permet d'avancer d'une secondes durant une lecture, tout en donnant la durée en cours.
	*	La durée de cette avancée est configurable dans les options de mp3directcut.
*	Contrôle+Flèche droite
	*	Permet de se déplacer au prochain point de coupe, tout en donnant la durée actuelle.
*	Contrôle+Flèche gauche
	*	Permet de se déplacer au point de coupe précédent, tout en donnant la durée actuelle.
*	Maj+Flèche droite
	*	Permet de faire un petit saut de quatre centièmes de secondes en avant durant une lecture, tout en donnant la durée en cours.
*	Maj+Flèche gauche
	*	Permet de faire un petit saut de quatre centièmes de secondes en arrière durant une lecture, tout en donnant la durée en cours.
*	S
	*	Permet d'arrêter la lecture en cours, tout en donnant la durée courante.
*	Espace
	*	Si l'enregistrement est prêt, permet de commencer celui-ci.
	*	Si un enregistrement est en cours, permet de le stopper, tout en positionnant le curseur tout au début du fichier.
	*	Si un fichier est ouvert, permet d'en commencer la lecture.
	*	Si une lecture est en cours, permet d'effectuer une pause, tout en donnant la durée en cours.
	*	Si une lecture est en pause, permet de relancer la lecture à partir de l'emplacement courant.
*	Flèche haute
	*	Permet de donnée la durée en cours.
	*	Si une sélection a été faite, positionne le curseur à l'emplacement du marqueur de début de sélection B, tout en donnant l'emplacement de ce marqueur.
	*	Dans les options du contrôle du volume de mp3directcut, donne la valeur précédente à laquelle on accède habituellement avec flèche haute.
	*	Et qui n'est pas vocalisée par défaut.
*	NVDA+H
	*	Permet d'ouvrir l'aide du module complémentaire courant.

## Changements pour la version 3.0 ##

*	 Utilisation du module gui.guiHelper pour assurer la bonne apparence de la
   boîte de dialogue de configuration du module complémentaire;
*	 Utilisation de format à la place de %s pour les chaînes formatées;
*	 Utilisation de la conformité avec les règles du guidelines pour
   l'implémentation.

## Changements pour la version 2.3 ##

*	 Ajout de la licence GPL pour le module complémentaire;
*	 Changement du raccourci-clavier du script donnant la fin de la sélection
   de "Ctrl+Shift+N" en "Ctrl+Shift+E" car "Ctrl+Shift+N" ne fonctionne pas
   avec les dernières versions de mp3DirectCut;
*	 Ajout d'un script pour confirmer que la sélection a été annulée avec
   "Ctrl+R";
*	 Réalisation de certaines corrections dans le appModule "mp3directcut.py".

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
