# mp3DirectCut #

* Auteur(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Présentation #

Cette extension améliore l'accessibilité du logiciel mp3DirectCut avec NVDA.

Elle a été testée avec les versions de mp3DirectCut allant de la 212 jusqu'à
la 223.

## Raccourcis-clavier ##

Cette extension offre les commandes suivantes :

* B

    * Permet de confirmer le bon placement du marqueur de début de sélection
      B.

* Contrôle+Maj+B

    * Permet d'indiquer l'emplacement du marqueur de début de sélection B.
    * Une double pression donne la durée de la sélection.

* Contrôle+Maj+D

    * Donne la durée parcourue depuis le début du fichier jusqu'à
      l'emplacement actuel du curseur de lecture.
    * Une double pression donne la durée totale.

* Contrôle+R

    * Confirme que la sélection a été annulée.

* Contrôle+Maj+R

    * Donne la durée restante depuis l'emplacement actuel du curseur de
      lecture jusqu'à la fin du fichier.

* Contrôle+Maj+E

    * Permet d'indiquer l'emplacement du marqueur de fin de sélection N.
    * Une double pression donne un récapitulatif de l'emplacement des
      marqueurs B et N, ainsi que la durée de la sélection.

* Contrôle+Maj+P

    * Donne la référence de la plage actuelle, ainsi que le nombre totale de
      plages.

* Contrôle+Maj+Espace

    * Permet d'indiquer la valeur actuelle du niveau du vu-mètre.
    * Une double pression permet de réinitialiser ce niveau.

* Flèche basse

    * Permet de donnée la durée en cours.
    * Si une sélection a été faite, positionne le curseur à l'emplacement du
      marqueur de fin de sélection N tout en donnant l'emplacement de ce
      marqueur.
    * Dans les options du contrôle du volume de mp3directcut, donne la
      valeur suivante à laquelle on accède habituellement avec flèche basse.
    * Et qui n'est pas vocalisée par défaut.

* Fin

    * Permet de déplacer le curseur de lecture tout à la fin du morceau en
      cours et donne la durée totale.

* Début ou Origine

    * Permet de déplacer le curseur de lecture tout au début du morceau en
      cours.

* Flèche gauche

    * Permet de faire un retour en arrière d'une seconde durant une lecture,
      tout en donnant la durée en cours.
    * La durée de ce retour est configurable dans les options de
      mp3directcut.

* N

    * Permet de confirmer le bon placement du marqueur de fin de sélection
      N.

* Page suivante

    * Permet de faire un saut en avant de 10 secondes durant une lecture,
      tout en donnant la durée en cours.
    * La durée de ce retour est configurable dans les options de
      mp3directcut.

* Page précédente

    * Permet de faire un saut en arrière de 10 secondes durant une lecture,
      tout en donnant la durée en cours.
    * La durée de ce retour est configurable dans les options de
      mp3directcut.

* R

    * Permet de préparer un enregistrement et indique si vous pouvez appuyer
      sur espace pour le commencer.

* Flèche droite

    * Permet d'avancer d'une secondes durant une lecture, tout en donnant la
      durée en cours.
    * La durée de ce retour est configurable dans les options de
      mp3directcut.

* Contrôle+Flèche droite

    * Permet de se déplacer au prochain point de coupe, tout en donnant la
      durée actuelle.

* Contrôle+Flèche gauche

    * Permet de se déplacer au point de coupe précédent, tout en donnant la
      durée actuelle.

* Maj+Flèche droite

    * Permet de faire un petit saut de quatre centièmes de secondes en avant
      durant une lecture, tout en donnant la durée en cours.

* Maj+Flèche gauche

    * Permet de faire un petit saut de quatre centièmes de secondes en
      arrière durant une lecture, tout en donnant la durée en cours.

* S

    * Permet d'arrêter la lecture en cours, tout en donnant la durée
      courante.

* Espace

    * Si l'enregistrement est prêt, permet de commencer celui-ci.
    * Si un enregistrement est en cours, permet de le stopper, tout en
      positionnant le curseur tout au début du fichier.
    * Si un fichier est ouvert, permet d'en commencer la lecture.
    * Si une lecture est en cours, permet d'effectuer une pause, tout en
      donnant la durée en cours.
    * Si une lecture est en pause, permet de relancer la lecture à partir de
      l'emplacement courant.

* Flèche haute

    * Permet de donnée la durée en cours.
    * Si une sélection a été faite, positionne le curseur à l'emplacement du
      marqueur de début de sélection B, tout en donnant l'emplacement de ce
      marqueur.
    * Dans les options du contrôle du volume de mp3directcut, donne la
      valeur précédente à laquelle on accède habituellement avec flèche
      haute.
    * Et qui n'est pas vocalisée par défaut.

* NVDA+H

    * Permet d'ouvrir l'aide de l'extension courante.

## Compatibilité ##

* Cette extension est compatible avec les versions de NVDA allant de 2019.3
  et au-delà.

## Changements pour la version 20240327.0.0

* Correction d'un bug qui provoquait une erreur dans le journal lors du
  rechargement des plugins, grâce à Rob, depuis la liste de diffusion
  nvda-addons ;

## Changements pour la version 20240326.0.0

* Compatibilité mise à jour pour NVDA-2024.1. ;
* Lien de téléchargement supprimé du fichier readme, le lien de
  téléchargement pour les futures mises à jour ne sera désormais disponible
  que dans l'add-on store.

## Changements pour la version 20231229.0.0 ##

* Ajout d'une implémentation rétrocompatible pour prendre en charge le mode
  Parler à la demande, qui sera bientôt disponible avec nvda-2024.1.

## Changements pour la version 20231007.0.0 ##

* Après avoir placé les points de coupe et après avoir ouvert la fenêtre des
  propriétés des points de coupe, avec "Contrôle+N", ajout de
  l'accessibilité au titre de cette fenêtre en indiquant la plage de
  l'index.
* En mode lecture, après avoir déplacé les marqueurs de début ou de fin de
  sélection avec les touches 1 à 6 du pavé alphanumérique, ajout du
  démarrage automatique de la lecture à partir de la nouvelle position ;
* Correction d'un bug qui survenait lors de la consultation de la durée
  restante avec "Contrôle + Maj + R" depuis le début du morceau.

## Changements pour la version 20230728.0.0 ##

* Appliqué les règles flake8 et mypy au code ;
* Modifiée la version minimale de NVDA prise en charge vers la 2019.3 pour
  prendre en charge les annotations introduites dans Python 3.

## Changements pour la version 20230508.0.0 et au-delà ##

* Numéro de version modifiée, version minimale NVDA et lien de
  téléchargement en fonction des conventions / exigences de la store.

## Changements pour la version 20.12 ##

* Arrête la parole pendant l'enregistrement et la lecture dans la dernière
  version de MP3DirectCut ;
* Correction de la lecture du temps restants pour les nouvelles versions de
  NVDA utilisant Python 3.

## Changements pour la version 19.02 ##

* Ajout de la configuration de l'extension dans le panneau Paramètres
  disponible depuis nvda 2018.2;
* Modification de la numérotation des versions en utilisant YY.MM (L'année
  en 2 chiffres, suivie d'un point, suivie du mois en 2 chiffres);
* Ajout de la compatibilité avec le nouveau format de gestion des versions
  des extensions, apparu depuis nvda 2019.1.

## Changements pour la version 4.0 ##

* Ajout de la compatibilité de l'extension avec Python 2.7 et 3;
* Correction d'un bug avec les chemins d'extension contenant des caractères
  non-ASCII.

## Changements pour la version 3.0 ##

* Utilisation du module gui.guiHelper pour assurer la bonne apparence de la
  boîte de dialogue de configuration de l'extension;
* Utilisation de format à la place de %s pour les chaînes formatées;
* Utilisation de la conformité avec les règles du guidelines pour
  l'implémentation.

## Changements pour la version 2.3 ##

* Ajout de la licence GPL à l'extension;
* Changement du raccourci-clavier du script donnant la fin de la sélection
  de "Ctrl+Shift+N" en "Ctrl+Shift+E" car "Ctrl+Shift+N" ne fonctionne pas
  avec les dernières versions de mp3DirectCut;
* Ajout d'un script pour confirmer que la sélection a été annulée avec
  "Ctrl+R";
* Apporté quelques corrections dans le code de l'appModule
  "mp3directcut.py".

## Changements pour la version 2.2 ##

* Correction des scripts donnant les emplacements des marqueurs de
  sélection.

## Changements pour la version 2.1.1 ##

* Suppression du script permettant de donner la durée totale et ajout de
  cette information au script donnant le temps écoulé;
* Ajout de la possibilité d'activer ou non les annonces liées à la touche
  espace dans les options de configuration de l'extension, distinctement des
  autres annonces;
* Ajout de la possibilité d'activer ou non l'annonce du bon placement des
  marqueures de sélection dans les options de configuration de l'extension;
* Ajout de l'annonce de la plage courante lors du déplacement parmi les
  points de coupe;
* Correction des annonces liées aux touches verticales;
* Ajout d'un script pour ouvrir l'aide de l'extension accessible grâce au
  racourci-clavier "NVDA+H";
* Déplacement du menu de configuration de l'extension du menu Outils vers le
  menu Préférences de NVDA.

## Changements pour la version 2.1 ##

* Ajout d'un script pour vocaliser le déplacement vers le point de coupe
  suivant avec Contrôle+Flèche droite;
* Ajout d'un script pour vocaliser le déplacement vers le point de coupe
  précédent avec Contrôle+Flèche gauche;
* Ajout d'un script pour vocaliser le déplacement de 4 centièmes de secondes
  en avant, avec Maj+Flèche droite;
* Ajout d'un script pour vocaliser le déplacement de 4 centièmes de secondes
  en arrière, avec Maj+Flèche gauche;
* Corection du summary de l'extension de "Pour mp3DirectCut" en
  "mp3DirectCut".

## Changements pour la version 2.0 ##

* Ajout d'un script pour connaître la durée restante avec "Contrôle + Maj +
  R";
* Correction de la lecture des durées comportant des heures;
* Ajout de la possibilité de différencier les millièmes ou centièmes de
  secondes.

## Changements pour la version 1.1 ##

* Ajout de la possibilité d'inclure la catégorie mp3DirectCut dans les
  gestes de commandes;

    * Ils ne seront visibles que pendant l'utilisation du logiciel
      mp3DirectCut.

* Ajout de la possibilité d'activer ou de désactiver les messages
  automatiques, dans le menu Outils de NVDA, élément "Configuration de
  mp3DirectCut";

## Changements pour la version 1.0 ##

* Première version.

[[!tag dev stable]]
