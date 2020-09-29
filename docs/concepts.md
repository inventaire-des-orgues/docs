# Choix de conception

## Identification et localisation

L'inventaire national des orgues comporte une forte dimension géographique.
Nous avons fait le choix d'un positionnement très précis et fiable des orgues sur le territoire français.
Tout instrument est reconnu par son emplacement.

L'emplacement d'un orgue est défini de deux façons :
- d'une part une approche géographique : tout simplement par ses latitude et longitude,
- d'autre part une approche toponymique : pays > commune > édifice > placement dans l'édifice

Pour des raisons pratiques, les coordonnées géographiques n'étant à l'origine de l'inventaire que rarement connues, l'approche toponymique a prévalu lors de la construction de l'inventaire.

Bien que non indispensable pour la localisation dès lors que l'inventaire travaille avant tout sur les communes, sont indiquées aussi :
région, département, commune associée, déléguée ou ancienne commune, adresse

## L'instrument

Dans l'inventaire, tout orgue est compris informatiquement sous l'angle d'une modélisation `objet`.

Un `orgue` est décrit par divers attributs, le plus souvent textuels.

Il possède un ensemble de `plans sonores` et des `accessoires`.
Chaque plan sonore comporte des `jeux`.
Un `jeu` est défini par son libellé et soit sa hauteur en pieds, soit son nombre de rangs.
Un jeu n'est pas associé en base de donnée à plusieurs plans sonores (dit autrement, il n'y a pas de représentation informatique d'un emprunt).


Un orgue possède aussi un `historique`, ensemble d'`évènements` comportant chacun une date, une liste de facteurs d'orgue acteurs de l'évènement etun descriptif.

Un `facteur` est une entité propre en base de donnée.

Des fichiers peuvent être joints à la description d'un orgue :
- des `images`;
- d'autres types de `fichiers`.
Une `image principale` peut être associée à un orgue.

Des mentions de `sources` peuvent être associées à un orgue.