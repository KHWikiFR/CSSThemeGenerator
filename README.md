# CSSThemeGenerator
Générateur automatique de thèmes CSS pour les modèles du wiki (palette, infobox, etc)

## Utilisation
` python KHWikiFRCssGenerator.py `

Veillez à ce que python2.7 soit installé, et si plusieurs versions de python sont installées, à employer la version 2.7

Le script utilise le fichier source __KHWikiFRCSSThemes.json__, et crée les thèmes CSS dans le fichier de sortie __KHWikiFRCSSThemes.css__, dont la version actuelle est fournie à titre d'exemple.

## Source
Le fichier __KHWikiFRCSSThemes.json__ contient une liste de thèmes. Chacun de ceux-ci est un dictionnaire, et doit contenir les paramètres suivants:

 * Name : Le nom utilisé par la classe CSS globale du modèle
 * FullName : Nom lisible (ajouté en commentaire au-dessus du code CSS du thème pour lisibilité)
 * Title : Couleur de fond pour la zone de titre principal
 * TitleFont : Couleur de police pour la zone de titre principal
 * Head : Couleur de fond pour les zones de sous-titres/labels/groupes
 * HeadFont : Couleur de police pour les zones de sous-titres/labels/groupes
 * Row : Couleur de fond pour les zones de contenu
 * RowAlt : Couleur de fond pour les zones de contenu quand celles-ci alternent de couleur

Les couleurs peuvent être renseignées au format hexadécimal ou par un nom en CSS.

# Changelog

## 0.2.0a - 2018-02-16
 * Modification du thème Monde

## 0.2.0 - 2018-02-16
 * Ajout des infobox (version de lancement)
 * Modification du thème Personnages
 * Fix & optimisation des palettes + implémentation de la bordure des sous-titres en couleur

## 0.1.2 - 2018-02-14
 * Fix des sélecteurs de cellule de contenu (classe .liste dépréciée retirée)
 * Ajout de sélecteurs pour assurer la priorité sur le thème de palette par défaut

## 0.1.1 - 2018-02-14
 * Fix du sélecteur de sous-titre pour supporter les palettes enchâssées

## 0.1.0 - 2018-02-14
 * Version de lancement
 * Script python + source JSON