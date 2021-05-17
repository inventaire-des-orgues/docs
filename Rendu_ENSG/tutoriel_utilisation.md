# Présentation générale du site

Lors de l'arrivée sur le site l'utilisateur peut naviguer entre cinq onglets. Il a le choix entre la page d'accueil qui est ouverte par défaut, la carte de localisation des orgues, la recherche sur les orgues, le lexique et une foire aux questions (FAQ).

## Accueil

La page d'accueil est constitué de plusieurs blocs. Le premier permet la recherche d'orgues selon le département ou un mot-clé (commune, facteur, église), qui renvoie à l'onglet "Les orgues" avec les informations entrée pré-remplit après recherche. L'utilisateur peut également accéder à une documentation pour éditer la photo principale d'une fiche d'orgue.

Le deuxième bloc constituant l'accueil est celui de la carte nationale interactive de la France. Cette carte est associée à différentes statistiques : le nombre d'orgues, le nombre d'entre elles qui sont inscrits ou classés, l'avancement des contributions et l'état de celles-ci. Ces statistiques changent en fonction du niveau de zoom : au début l'utilisateur se situe au niveau national, et au survol d'un département les statistiques vont changer et se baser sur la région survolée. Au clic, l'utilisateur peut accéder au niveau départemental et accéder aux départements de la région choisit. Pour accéder aux données du département il faut simplement cliquer dessus. Ensuite, lors du zoom sur les département, l'utilisateur peut revenir à la vue nationale en cliquant sur le bouton "Retour".

Le troisième bloc est un petit texte explicatif de pourquoi cet inventaire existe et son but.

## Carte

L'onglet carte contient une carte centrée sur la France, avec le nombre d'ogues localisés, c'est-à-dire possédant actuellement un id OSM. Lorsque l'utilisateur zoom sur la carte de France, les étiquettes se divisent et affichent ainsi plus d'informations : comme l'utilisateur zoom sur la carte, la surface visible est plus grande et ainsi le nombre d'étiquettes de cluster peut être plus important. L'utilisateur peut également filtrer les orgues selon le facteur ou la manufacture de celles-ci s'il souhaite faire une recherche plus précise.

## Les orgues

Il s'agit d'un onlet permettant de rechercher un orgue spécifique. L'interface est très simple : comme décrit précédemment pour l'accueil, la recherche d'un orgue se fait par département ou par mot-clé. Par défaut, si rien est rentré, des orgues sont tout de même affichés. L'affichage des orgues se fait sous forme de vignette : l'utilisateur voit le nom, la ville et le département de l'orgue ainsi que sa localisation dans le batiement. La localisation est rappelée voire précisé avec le champ "Localisation", et le facteur d'ogue est également renseigné. Lorque l'on clique sur une vignette, l'utilisateur arrive sur la fiche de l'orgue sélectionné et peut ainsi compléter ou modifier la fiche d'information dans une certaine mesure.

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
