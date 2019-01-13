# CSSThemeGenerator
Générateur automatique de thèmes CSS pour les modèles du wiki (palette, infobox, etc)

## Utilisation
` python KHWikiFRCssGenerator.py `

Veillez à ce que python2.7 soit installé, et si plusieurs versions de python sont installées, à employer la version 2.7

Le script utilise le fichier source __KHWikiFRCSSThemes.json__, et crée les thèmes CSS dans le fichier de sortie __KHWikiFRCSSThemes.css__, dont la version actuelle est fournie à titre d'exemple.

## Source
Le fichier __KHWikiFRCSSThemes.json__ contient une liste de thèmes. Chacun de ceux-ci est un dictionnaire, et doit contenir les paramètres suivants:

 * Name : Le nom utilisé par la classe CSS globale du modèle.
 * FullName : Nom lisible (ajouté en commentaire au-dessus du code CSS du thème pour lisibilité).
 * Title : Couleur de fond pour la zone de titre principal. Sert aussi à séparer les lignes dans les sous-groupes d'infobox.
 * TitleFont : Couleur de police pour la zone de titre principal.
 * Head : Couleur de fond pour les zones de titre de groupe des palettes, et les lignes de contenu standard des infobox. Sert aussi à la ligne qui souligne les sous-titres de palette.
 * HeadFont : Couleur de police pour les zones affectées par Head.
 * Row : Couleur de fond pour les zones de contenu des palettes.
 * RowAlt : Couleur de fond pour les zones de contenu des palettes quand celles-ci alternent de couleur, et les lignes de contenu de sous-groupes des infobox.
 * RowAltFont: Couleur de police pour les zones affectées par RowAlt.

Les couleurs peuvent être renseignées au format hexadécimal ou par un nom en CSS.

# Changelog

## 0.3.2 - 2018-06-27
 * Nouvelle itération des liens dans les champs d'infobox utilisant la couleur Head

## 0.3.1a - 2018-06-09
 * Fix des liens infobox dans les sous-groupes

## 0.3.1 - 2018-06-09
 * Fix des liens dans les champs utilisant la couleur Head dans les infobox et palettes

## 0.3.0a - 2018-03-04
 * Uniformisation des thèmes de l'Organisation

## 0.3.0 - 2018-02-28
 * Suppression du code déprécié (plus nécessaire)

## 0.2.3 - 2018-02-26
 * Fix des priorités pour les headers

## 0.2.2 - 2018-02-26
 * Fix des infobox: les sous-groupes ont maintenant une couleur de police fixée au lieu d'hériter HeadFont

## 0.2.1 - 2018-02-16
 * Ajout du CSS pour les infobox utilisant row-items
 * Modification du thème Monde

## 0.2.0 - 2018-02-16
 * Ajout des infobox (version de lancement)
 * Modification du thème Personnages
 * Fix & optimisation des palettes + implémentation de la bordure des sous-titres en couleur
 
## 0.1.2a - 2018-02-14
 * Fix du thème Sceptre (mal importé)

## 0.1.2 - 2018-02-14
 * Fix des sélecteurs de cellule de contenu (classe .liste dépréciée retirée)
 * Ajout de sélecteurs pour assurer la priorité sur le thème de palette par défaut

## 0.1.1 - 2018-02-14
 * Fix du sélecteur de sous-titre pour supporter les palettes enchâssées

## 0.1.0 - 2018-02-14
 * Version de lancement
 * Script python + source JSON