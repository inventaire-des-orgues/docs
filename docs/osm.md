# OpenStreetMap et l'inventaire des orgues

L'inventaire des orgues utilise pour une bonne part les coordonnées géographiques issues de la plate-forme OpenStreetMap, car il s'agit d'un projet libre, open source et open data.
De plus, les données des édifices religieux français sont bien plus complètes que sur Google Maps.

## Mode simple, accessible à tous

### Directement sur le site OpenStreetMap

La façon la plus simple, si l'on ne recherche les coordonnées géographiques que pour quelques instruments seulements, 
de les capter manuellement depuis le site OpenStreetMap.

- se connecter au site [OpenStreetMap](https://www.openstreetmap.org)
- rechercher un édifice à l'aide du moteur de recherche (par exemple : "église saint-thomas la flèche")
- vérifier sur la carte qu'il s'agit bien du bon édifice
- récupérer l'id du l'objet représentant l'édifice (il est affiché en parenthèse dans le titre, "37420047" dans notre exemple)
- récupérer le type d'objet représentant l'édifice (il débute le titre, "Chemin" dans notre exemple)
- renseigner cet id et ce type dans l'inventaire des orgues, à l'onglet *Localisation* de la fiche

C'est tout ! Nous pourrons alors automatiquement récupérer les latitude et longitude de l'édifice.

## Mode expert, pour les administrateurs ou geeks

### Visionner les données OSM

#### QGIS

Level0
https://wiki.openstreetmap.org/wiki/Level0
http://level0.osmz.ru/?url=node/71893023

L'import dans une couche vecteur QGIS donne :
-	Une couche lines
-	Une couche multilinestrings : vide 
-	Une couche multipolygons : les way OSM
-	Une couche points : les node OSM disposant d'un tag au moins
-	Une couche other_relations : les relation OSM pour lesquelles leurs member OSM n'ont pas de role OSM (ou qui n'ont pas le type multipolygon ?

### Utiliser les données OSM

Notre objectif : récupérer les données géographiques des édifices hébergeant des orgues.

OpenStreetMap (OSM) ne propose que 3 type d'objets :
- node
- way
- relation

Les édifices contenant un orgue sont généralement des chemins ('way'), mais peuvent être d'autres types : simples noeuds ('node') ou bien regroupement d'objet ('relation').

Filtrer par attribut permet de limiter le nombre de données extraites
- Attribut building
  - cathedral
  - chapel
  - church

Plusieurs types de requêtes

#### OSM

#### Base de données OSM

Il est possible de parcourir directement les fichiers OSM :
http://download.geofabrik.de/
http://download.geofabrik.de/europe/france.html

#### PostgreSQL et PostGIS
PostGIS
-	PostgreSQL : prendre la version zippée, pour inclusion dans d'autres distributions
-	Version 12
-	PgAdmin4 : prendre le Wheel Python
-	Installer avec un script Python appelant pip

Initialiser postgre :
.\initdb.exe  -D ..\..\..\Downloads\OSM\data
.\postgres.exe -D ..\..\..\Downloads\OSM\data\
Lancer PgAdmin4 (faire un petit .bat)
cd D:\Users\poullennecgwi\Portable\WPy64-3720\python-3.7.2.amd64
python.exe .\Lib\site-packages\pgadmin4\pgAdmin4.py

createuser -s -d gwilherm
createdb dit que poullennecgwi existe déjà (créé par initdb ?)

Dans pgadmin : serveur : localhost, base : poullennecgwi, user gwilherm


#### Overpass

[Overpass](http://overpass-turbo.eu/) est un outil en ligne de requête dans les bases OSM.

https://www.openstreetmap.org/way/351261994

http://overpass-turbo.eu
https://wiki.openstreetmap.org/wiki/FR:Overpass_turbo
https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide

Deux langages de requêtes sont disponibles :
-	Langage ad hoc
-	Langage XML

Requête pouvant être passée dans l'IHM ou par API.
Exemple :
https://towardsdatascience.com/loading-data-from-openstreetmap-with-python-and-the-overpass-api-513882a27fd0


#### Python

Un script basé sur les modules standard XML (etree pour fichiers pas trop gros) permet la lecture des way, node, relation et leur traitement.


### Modifier les données d'OpenStreetMap

#### JOSM
Nécessite JAVA 1.7
