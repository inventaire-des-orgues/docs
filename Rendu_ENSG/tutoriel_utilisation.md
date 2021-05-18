# Présentation générale du site

Lors de l'arrivée sur le site l'utilisateur peut naviguer entre cinq onglets. Il a le choix entre la page d'accueil qui est ouverte par défaut, la carte de localisation des orgues, la recherche sur les orgues, le lexique et une foire aux questions (FAQ).

## Accueil

La page d'accueil est constituée de plusieurs blocs. Le premier permet la recherche d'orgues selon le département ou un mot-clé (commune, facteur, église), qui renvoie à l'onglet "Les orgues" avec les informations entrées pré-remplies après recherche. L'utilisateur peut également accéder à une documentation pour éditer la photo principale d'une fiche d'orgue.

Le deuxième bloc constituant l'accueil est celui de la carte nationale interactive de la France. Cette carte est associée à différentes statistiques : le nombre d'orgues, le nombre d'entre elles qui sont inscrits ou classés, l'avancement des contributions et l'état de celles-ci. Ces statistiques changent en fonction du niveau de zoom : au début l'utilisateur se situe au niveau national, et au survol d'un département les statistiques vont changer et se baser sur la région survolée. Au clic, l'utilisateur peut accéder au niveau départemental et accéder aux départements de la région choisit. Pour accéder aux données du département il faut simplement cliquer dessus. Ensuite, lors du zoom sur les département, l'utilisateur peut revenir à la vue nationale en cliquant sur le bouton "Retour".

Le troisième bloc est un petit texte explicatif de pourquoi cet inventaire existe et son but.

## Carte

## Les orgues

Il s'agit d'un onglet permettant de rechercher un orgue spécifique. L'interface est très simple : comme décrit précédemment pour l'accueil, la recherche d'un orgue se fait par département ou par mot-clé. Par défaut, si rien n'est rentré, des orgues sont tout de même affichés. L'affichage des orgues se fait sous forme de vignette : l'utilisateur voit le nom, la ville et le département de l'orgue ainsi que sa localisation dans le batîment. La localisation est rappelée voire précisée avec le champ "Localisation", et le facteur d'orgues est également renseigné. Lorque l'on clique sur une vignette, l'utilisateur arrive sur la fiche de l'orgue sélectionné et peut ainsi compléter ou modifier la fiche d'information dans une certaine mesure.

### Fiche d'un orgue

Lorsque l'utilisateur clique sur un orgue, il a accès à la fiche d'un orgue. Le nom est affiché, la photo principale puis une large description de celle-ci (composition, description...). Un bandeau est également présent avec de multiples informations : facteurs, propriétaire, localisation... Au dessus de ce bandeau se situe un bouton "Compléter la fiche", permettant si l'utilisateur est connecté de la modifier (sinon l'utilisateur est renvoyé à une page de connexion). L'utilisateur peut ainsi naviguer dans tous les onglets et modifier les informations souhaitées, hormis certaines étant réservées aux admins (code insee, département, référence palissy, code inventaire régional...). Enfin, l'utilisateur à juste à enregistrer ses modifications en bas de page, les informations seront ainsi mises à jour à son nom.

## Lexique

Le lexique est un onglet permettant de se renseigner sur le vocabulaire du monde de l'Orgue, qui permet ainsi à l'utilisateur de se renseigner et d'acquérir des connaissances dans la matière lorsqu'il voit des mots qui lui sont inconnus.

## Questions/Réponses

Cet onglet est une foire une question, qui renvoie parfois l'utilisateur à la documentation pour l'aider à naviguer à travers le site ou à l'utiliser.

# Différentes commandes utilisées

## Les facteurs d'orgues

### Webscrapping des facteurs

Ouvrez le fichier Rendu_ENSG/programmes_annexes/requetes_facteurs.py. Lancez le programme. Il fournit un fichier datas.json contenant le nom du facteur d'orgues, le nom de la manufacture d'orgues et l'adresse.
Ouvrez le fichier Rendu_ENSG/programmes_annexes/geocodage_manufactures.py. Ce programme prend en entrée le fichier datas.json et donne en sortie le fichier facteurs_localisation.json contenant pour chaque manufacture les coordonnées en latitude/longitude. 
Chargez les coordonnées dans la base de données :
```shell script
python manage.py import_organ_builder_lonlat chemin/vers/facteurs_localisation.json
```

### Gestion des facteurs d'orgue

Il existe plusieurs commandes qui permettent de manipuler les facteurs d'orgue.

Il arrive qu'un facteur d'orgues soit présent plusieurs fois avec exactement le même nom dans la base de données. La commande suivante permet de supprimer ces doublons : 
```shell script
python manage.py delete_organ_builder_duplication
```

Dans d'autres cas, il est possible qu'un facteur d'orgues soit présent plusieurs fois dans la base de données sous des noms différents. Le mieux est de créer un fichier csv qui contient deux colonnes séparées par un point-virgule. La première colonne contient le facteur d'orgues à supprimer, la deuxième le facteur qui doit remplacer. 
Dans certains cas, le nom du facteur contient une association de deux facteurs qu'il faut séparer en deux facteurs (par exemple Jaquot-Dider doit se transformer en Nicolas Jaquot et Charles Didier). La première colonne contient le nom du facteur à supprimer, toutes les suivantes les noms des facteurs qui doivent apparaître.
```shell script
python manage.py replace_organ_builder --delete chemin/vers/facteurs_remplacement.csv
```
L'option --delete supprime de la base les facteurs d'orgue

## Localisation des orgues

Une partie des orgues n'a pas de coordonnées. Afin de les obtenir, nous passons par Open Street Map afin d'associer chaque orgue à un bâtiment pour calculer ainsi les coordonnées de l'orgue. 

### Association à un objet OSM

Pour les orgues de la base qui n'ont pas d'identifiant OSM renseigné, un programme en arrière-plan se charge d'effectuer une recherche afin d'appairer l'orgue et un objet OSM, en partant du code INSEE de la commune et le nom de l'édifice où se trouve l'orgue. Pour cela, utilisez la commande :
```shell script
python manage.py appariement_osm 01
```
La valeur en fin de ligne correspond au département dont on souhaite traiter les orgues non localisés. Il est possible de remplacer le code de département par all afin de lancer le programme sur l'ensemble de la base de données.
Cette commande fournit 4 fichiers json dans le dossier /appariement :
- appariements_osm_01.json  Ce fichier comprend tous les orgues appairés, avec l'identifiant et le type de l'objet OSM.
- multi-appariements_osm_01.json  Ce fichier comprend les cas où plusieurs édifices correspondaient à l'orgue, avec les informations nécessaires pour permettre à un administrateur de sélectionner le bon édifice.
- appariements_partiels_osm_01.json  Ce fichier comprend les cas où plusieurs édifices ont une correspondance partielle avec l'orgue, avec les informations nécessaires pour permettre à un administrateur de sélectionner le bon édifice.
- non-appariements_osm_01.json  Ce fichier comprend les derniers cas particuliers dont appariement n'a pas pu être possible et pour lesquels une recherche manuelle est nécessaire.



### Calcul des coordonnées à partir de l'id OSM

Pour chaque orgue, l'utilisateur peut renseigner l'identifiant de l'édifice dans Open Street Map et le type du bâtiment (noeud, chemin, relation). C'est une manipulation plus facile pour l'utilisateur que de rentrer des coordonnées en latitude/longitude. Il faut donc un programme en arrière-plan qui puisse faire la conversion. Pour cela, utilisez la commande : 
```shell script
python manage.py calcul_barycenter_osm --calculall
```
Cette commande fournit un fichier coordonnees_osm.json qui contient la codification des orgues et les coordonnées latitude/longitude associées. Par défaut, le programme ne calcule la position que pour les orgues dont les champs latitude et longitude ne sont pas renseignés. Pour appliquer le calcul à tous les orgues, utilisez l'option --calculall.

Il reste ensuite à insérer ces données dans la base de données. Pour cela, utilisez la commande suivante :
```shell script
python manage.py import_organ_lonlat chemin/vers/coordonnees_osm.json
```
Par défaut, la commande ne complète que les coordonnées pour les orgues dont la position n'a pas déjà été renseignée. Pour écraser toutes les coordonnées, utilisez l'option --ecraseall. L'option --ecraseif ne remplace la position que si les champs n'étaient pas remplis ou si la distance entre les deux positions est supérieure à 30 mètres.

