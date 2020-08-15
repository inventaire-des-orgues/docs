# Structure de la fiche descriptive d'un orgue de l'inventaire


La structure de la fiche décrivant un orgue est le coeur de l'inventaire. Elle a fait l'objet de longues réflexions, 
dans le but d'aboutir à un juste compromis entre niveau de détails suffisant et complexité limitée.
Elle s'inspire bien sûr des livres d'inventaire, ainsi que des sites existants. Elle présente toutefois une structure bien plus fine que la plupart des sites consacrés aux orgues.

La saisie d'une fiche est facilitée par l'organisation en plusieurs grandes rubriques, 
qui prennent la forme de différents onglets sur le portail de l'inventaire.

## Informations générales

### Edifice

`Valeur_par_defaut = ""`

Le nom de l'édifice hébergeant l'orgue. Il s'agit très souvent d'églises ou de temples.
La désignation des édifices peut prêter à discussion car, pour de grands édifices, il est fréquent qu'elle ait changé au cours des siècles.

Le terme église prend une majuscule lorsqu’il désigne l’institution ou l’ensemble des fidèles : l’Église catholique (ou absolument l’Église), les Églises protestantes, etc. La minuscule est réservée au bâtiment. Cette remarque s’applique à d’autres termes relevant de domaines différents, quand il s’agit de distinguer deux réalités bien distinctes que désigne un même mot (la raison d’État, l’état des lieux ; la Bourse de commerce, une bourse d’études).

Concernant les ordres et les congrégations, on met une majuscule quand on désigne l’ensemble de l’ordre, de la congrégation, etc. : les Jésuites, les Dominicains. Mais on met une minuscule lorsqu’on ne parle que d’une partie des membres : un couvent de dominicains.

Rappel concernant le mot Saint : quand il désigne le personnage lui-même, saint est un nom commun qui s’écrit sans majuscule : Les trois saints de glace sont saint Mamère, saint Pancrace et saint Servais. Seule exception Saint Louis, considéré comme un nom propre. En revanche, saint prend la majuscule lorsqu’il entre dans la formation d’un nom de famille, d’un nom de lieu, de rue, de ville, de fête, etc., et il est suivi d’un trait d’union : le duc de Saint-Simon, la Sainte-Chapelle, la place Saint-Marc, les feux de la Saint-Jean, l’île Saint-Louis ; Les Saint-Germanois sont les habitants de Saint-Germain-en-Laye. Il prend également la majuscule dans certaines expressions traditionnelles historiques ou religieuses : la Sainte-Alliance, le Saint-Empire, le Saint-Office, le Saint-Esprit, le Saint-Siège, la Sainte-Trinité, le Saint-Père.

Apostrophe typographique :
(https://fr.wikipedia.org/wiki/Apostrophe_(typographie))

### Désignation

La désignation d'un orgue pose très souvent problème. En effet, le titre "grand orgue" est subjectif, emphatique, et vaut généralement par opposition au titre "orgue de choeur".
Dans l'inventaire, la désignation permet de qualifier le type d'instrument. Ainsi, sans plus de particularité on parlera simplement d'un "orgue".
On employera le cas échéant les désignations d'"orgue coffre", d'"orgue polyphone", d'"orgue à cylindres", etc.

`Valeur_par_defaut = "orgue"`

Nota : dans les thésaurus du ministère de la culture, la désignation reprend l'emplacement : "orgue de choeur", "orgue de tribune". Cette classification n'est pas exactement adoptée ici, puisque nous distinguons désingation et emplacement.
En effet, vu le nombre d'orgues, nous avons besoin de plus de finesse de représentation que pour les édifices classés ou inscrits. Il n'y a pas trois orgues classés ou inscrits dans un même édifice, mais trois orgues, si (ex: collégiale Notre-Dame de Mantes-la-Jolie, église Notre-Dame de Versailles)!

### Emplacement

L'emplacement permet de positionner sans erreur l'orgue dans l'édifice. Il correspond aux coordonnées géographiques indiquées par ailleurs dans la fiche.
Exemples d'emplacement : "crypte", "choeur", "transept", "sacristie", "triforium", "salle Marcel Dupré", etc.

Cet attribut permet donc aussi la distinction, dans la majorité des cas, entre orgue de choeur et orgue de tribune, voire le cas échéant entre plusieurs orgues de choeur ou de tribune.

`Valeur_par_defaut = <Néant>`

### Etat de fonctionnement
Il s'agit d'un avis à date de mise à jour de la fiche descriptive.
Nécessairement pour partie subjectif, il se rapporte à l'utilisation possible de l'instrument.
Les défauts courants et réversibles d'un orgue (cornement occasionnel par exemple) ne rentrent pas en compte dans l'appréciation.
L'état de fonctionnement ne décrit pas l'état du buffet ou des boiseries dès lors que le jeu n'est pas altéré.

`Valeur_par_defaut = <Néant>`

    "Très bon ou bon : tout à fait jouable",
    "Altéré : difficilement jouable",
    "Dégradé ou en ruine : injouable"

### Orgues polyphones de Louis Debierre
is_polyphone [bool] spécifie si l'orgue est un polyphone de la manufacture Debierre.
Les polyphones sont des orgues coffres dont certains tuyaux de basse permettent l'émission de plusieurs notes distinctes.
(Musica et memora)[http://www.musimem.com/debierre.htm]

`Valeur_par_defaut = False`

Nota : cet attribut sera supprimé, l'attribut désignation étant suffisant.

### Propriété de l'orgue
Le propriétaire de l'orgue (qui n'est pas nécessairement le même que l'édifice).
Le plus souvent, il s'agit de la commune pour des instruments datant d'avant 1905 (de l'Etat pour les orgues de cathédrales), et d'association cultuelle (généralement paroisse) pour les orgues d'après 1905 ou de congrégation.
Bien sûr, il existe plusieurs exceptions : par exemple, les orgues des cathédrales de la petite couronne parisienne, n'appartiennent pas à l'Etat, mais l'orgue de la basilique royale de Saint-Denis si.

`Valeur_par_defaut = "commune"`

    "commune",
    "Etat",
    "association culturelle",
    "diocèse",
    "paroisse"

### Organisme auquel s'adresser

`Valeur_par_defaut = ""`

Libellé du lien, et lien, vers un organisme, le plus souvent une association, au plus proche de l'instrument.
Il s'agit de l'organisme le plus à même de fournir un renseignement ou un contact pour visiter et jouer l'orgue.
Le libellé du lien est le terme qui apparaîtra comme lien dans la visualisation de la fiche (cartouche de synthèse).

### Lien de référence

Lien Internet vers l'organisme auquel s'adresser.

`Valeur_par_defaut = ""`

### Résumé

`Valeur_par_defaut = ""`

Cette courte description (500 caractères maximum) est une synthèse rédigée sur l'histoire et la description de l'instrument.
Elle doit être utilisée pour évoquer une particularité de l'instrument, ce qui fait son originalité et sa valeur.

### Commentaire rédacteurs

`Valeur_par_defaut = ""`

Ce commentaire n'est visible qu'en mode édition et sera affiché sur fond coloré en haut de la fiche lors de l'édition.
Il sert à transmettre une information entre rédacteurs de la fiche.
Par exemple : "La description de la tuyauterie semble erronée.", ou "Nous ne sommes pas certains de la composition du Récit."


## Localisation

### Commune

Il s'agit de la commune selon le dernier [code officiel géographique](https://www.insee.fr/) en vigueur de l'INSEE.
Celui-ci est aussi sur le site [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/#_)
Attention, de nombreuses communes ont fusionné au cours des dernières années, et de tels regroupements se poursuivront dans les années à venir.
Il faut donc prendre garde à ne pas renseigner le nom d'une ancienne commune, même s'il continue à être usuellement utilisé. L'attribut Ancienne commune est dédié à cet effet.
Trois types de communes sont couramment référencées dans le code officiel géographique en vigueur : commune (de plein droit), commune associée, commune déléguée, auquels s'ajoutent les arrondissements de Paris, Lyon et Marseille.
Par convention, seules les communes de plein droit sont indiquées dans l'attribut Commune.

### Code INSEE

Code de la commune selon le code géographique officiel de l'INSEE. On le trouve aussi généralement dans la fiche de la commune sur Wikipédia.
Il est unique, et donc distinct du code postal utilisé pour l'adressage du courrier. Il est indispensable pour identifier sans équivoque une commune française, car plusieurs communes peuvent avoir le même nom.

### Ancienne commune

Cet attribut est une aide pour faciliter la localisation.
Il est à prendre dans une acceptation large : il peut s'agir d'une ancienne commune disparue suite à un regroupement de communes, 
d'une commune déléguée, d'une commune associée.

### Adresse

L'adresse de l'édifice considéré. Elle est utilisé pour distinguer deux édifices de même nom sur une même commune, car de plus en plus fréquent au gré des fusions de communes.
Souvent, ce peut-être un lieu-dit, ou une rue.

### Code département

Code du département selon le code géographique officiel de l'INSEE.

### Département

Nom du département selon le code géographique officiel de l'INSEE.

### Région

Nom de la région selon le code géographique officiel de l'INSEE.

### Latitude

Latitude, selon le système de coordonnées WGS84, couramment connu comme "coordonnées GPS".
Nota : celui-ci n'est pas le système de coordonnées officiel français.
Pour des facilités de saisie et d'export des données, le format adopté est un nombre réel signé, et non la notation en degrés, minutes et secondes.

Cf. la [page sur OSM](osm.md).

### Longitude

Cf. latitude.

Cf. la [page sur OSM](osm.md).

### Type OpenStreetMap

Type d'objet représentant l'édifice selon la nomenclature utilisée par le projet [OpenStreetMap](https://www.openstreetmap.org).
Il peut s'agir :
- way : d'un chemin, ensemble de points
- node : d'un simple points
- relation : d'une combinaison libre de ces trois types d'objets

On préfèrera définir des "way" ou "relation", représentant le contour exact de l'édifice.

Cf. la [page sur OSM](osm.md).

### Id OpenStreetMap

Identifiant unique de l'objet selon la nomenclature utilisée par le projet [OpenStreetMap](https://www.openstreetmap.org).

Cf. la [page sur OSM](osm.md).


## Historique

L'historique d'un orgue est une succession d'évènements.

Un évènement est lui-même décrit par les quatres informations suivantes :
- l'année de l'évènement [int]
- le type d'évènement [string]
- la liste des facteurs ayant contribué à l'évènement [liste]
- une description libre de l'évènement [string]

Les types d'évènement possibles sont les suivants :

Valeur_par_defaut = Néant

    "Construction",
    "Reconstruction",
    "Destruction",
    "Restauration",
    "Déménagement",
    "Relevage",
    "Disparition",
    "Dégâts",
    "Classement aux monuments historiques",
    "Inscription aux monuments historiques"

- Reconstruction : des éléments nouveaux sont ajoutés en grand nombre, la structure de l'instrument est modifiée.
- Destruction : dégâts sur l'ensemble de l'instrument, rendu totalement inutilisable.
- Restauration : opération d'importance, à caractère patrimonial : il s'agit de revenir à un état antérieur de l'instrument.
- Déplacement : déplacement de l'instrument d'un lieu à un autre, que ce soit dans l'édifice ou entre deux édifices. 
- Relevage : simple opération de conservation de l'instrument, menée à intervalles réguliers.
- Disparition : distincte de destruction, car l'orgue a pu disparaître suit à un déménagement, ou être stocké dans un endroit inconnu.
- Dégâts : destruction partielle ou altération de l'instrument.
- Classement ou incription au titre des monuments historiques :
On ne distingue que Inscription au titres des monuments historiques et Classement au titre des monuments historiques, comme objets evenement.
Le champ TICO de Palissy sera mis dans le commentaire de l'évenement.
De même pour les autres champs issus de la mise en correspondance entre l'inventaire et la base Palissy, par exemple le numéro d'arrêté de classement ou inscription.



## Buffet / Console

### Description du buffet

Champ libre [html sans limite de taille] pour la description du buffet et de son état.

`Valeur_par_defaut = ""`

### Description de la console

Champ libre [html sans limite de taille] pour la description de la console et de son état.
La notion de console est assez récente : elle survient avec l'apparition de meubles séparés du buffet au XIXe siècle, souvent tournés vers l'autel ou mobiles au XXe siècle.
Aussi la console peut-être, lorsqu'elle n'est pas distincte du buffet, décrite dans un sous-chapitre de la section buffet.

Hormi la construction dans une fenêtre pratiquée dans le buffet, les dispositions les plus courantes sont :
- séparée, organiste tourné vers l'orgue
- séparée, organiste dos à l'orgue

Dans le cas d'une console mobile ou en fenêtre sur le côté (ex : église Saint-Pierre de Prat) ou encore à l'arrière de l'instrument (ex : église Saint-Jean de Lamballe), on précisera la disposition.
Idem dans le cas d'une seconde console (ex : basilique Sainte-Clotilde et Sainte-Valère à Paris).

`Valeur_par_defaut = ""`

## Partie instrumentale

### Transmission des notes

Le type de transmission des notes est indiqué pour tout l'instrument, et non par clavier.
Lorsque les claviers disposent d'un autre mode de transmission que celle généralement ou originellement utilisée pour l'instrument (ex: pédalier à transmission électrique, récit sans Barker) seront précisés dans les commentaires du plan sonore concerné.

    <Néant>,
    "Mécanique",
    "Mécanique non suspendue",
    "Mécanique suspendue",
    "Mécanique à balanciers",
    "Mécanique avec Barker",
    "Pneumatique",
    "Electrique",
    "Electro-pneumatique"

Lorsque la mécanique n'est pas suspendue, on indiquera "Mécanique non suspendue". La valeur "Mécanique" sera utilisée en cas de doute sur le type de transmission mécanique. 

### Transmission commentaire

Une grande variété de systèmes de transmission des notes existe. Cet attribut permet d'apporter un complément d'information sur le type de transmission et sa particularité.

## Tirage des jeux

Le type de transmission des notes est indiqué pour tout l'instrument

    "Mécanique",
    "Pneumatique haute pression",
    "Pneumatique basse pression",
    "Electrique",
    "Electro-pneumatique"

On distingue le tirage pneumatique basse pression (systèmes de la période symphonique) des tirages haute pression utilisé dans la facture d'orgue contemporaine, avec emploi de relais pneumatiques issus de l'industrie.

## Tirage commentaire

Cet attribut permet d'apporter un complément d'information sur le type de tirage des registres et sa particularité.

### Diapason

`Valeur_par_defaut = <Néant>`

Hauteur, notée en Hertz, du A2 donné par le Prestant 4 ou équivalent, avec indication de température de prise du diapason sans laquelle celui-ci n'a pas de sens.
ex : "412 Hz à 14°C"

### Tempérament

`Valeur_par_defaut = <Néant>`

Champ texte libre [string].

Il existe une infinité de temparément dans le monde de la musique. Cet attribut est donc un texte libre, permettant l'indication du tempérament de la façon la plus précise possible.
ex : "mésotonique au sixième modifié"

#### Sommiers

Champ HTML libre [string]

`Valeur_par_defaut = <Néant>`

### Soufflerie

Champ HTML libre [string]

`Valeur_par_defaut = <Néant>`

### Description de la tuyauterie

Champ HTML libre [string]

`Valeur_par_defaut = <Néant>`

Commentaire général sur la tuyauterie et description jeu par jeu, dans l'ordre de la composition.

Note importante : on veillera à respecter les [conventions](conventions.md) de l'inventaire.

    
## Composition

### Plans sonores

La composition distingue plusieurs plans sonores.

Un plan sonore est nommé et son étendue est précisée sous la forme suivante :
C1-G5 (cf. les [conventions](conventions.md)).

Souvent, les orgues de facture du XIXe siècle possèdent 56 notes au claviers (C1-G5) et 30 notes à la pédale (C1-F3).


Cf. [le lexique de l'inventaire](https://vocabulaire.inventaire-des-orgues.fr/)
et [Wikipédia](https://fr.wikipedia.org/wiki/Liste_des_jeux_d%27orgue)

De très nombreux jeux sont déjà enregistrés. Merci d'utiliser le formulaire de contact si vous souhaitez citer un jeu qui ne serait pas déjà répertorié.

`Valeur_par_defaut = "Bourdon 8"`

Les registres sont énumérés selon un ordre harmonique (hauteur du jeu).
On suivra la disposition suivante :
- Fonds
- Mixtures
- Cornet
- Batterie d'anches
- Anches de détail

La hauteur est indiquée par convention en pieds, en chiffres arabes, sans précision de l'unité.
La nombre de rangs des fournitures, plein-jeux, cornet, etc. est indiqué en chiffre romains, sans précision du terme "rangs" (ni "rgs").

Un champ libre permet pour de joindre pour chaque jeu une courte information optionnelle.
Par exemple :
- Emprunté au Grand orgue
- Transmission électrique du registre
En particulier, les basses et dessus seront notés :
- Basse.
- Dessus.

Astuce : Aide à la saisie : une composition peut rapidement se saisir au clavier, sans utiliser la souris.
Il faut pour cela :
- utiliser la touche tabulation pour passer d'une case à l'autre du formulaire;
- appuyer sur la touche espace pour dérouler le menu présentant les jeux.


### Accessoires

Valeur_par_defaut = Néant

Les accessoires peuvent être :

- accouplement :
    - on peut préciser s'il s'agit d'un accouplement classique à l'unisson, à l'octave basse ou bien à l'octave aigüe.
    - on doit préciser le clavier accouplé et le clavier jouant avec l'accouplement.
- trémolo : on peut préciser le clavier
- appel : appel d'un jeu ou de plusieurs jeux, généralement les jeux d'anches ou mixtures.
- renvoi : renvoi d'un jeu ou de plusieurs jeux, généralement les jeux d'anches ou mixtures. N'est renseigné que si une cuillère spécifique effectue le renvoi. Si la cuillère de l'appel permet le renvoi lorsqu'elle est relâchée, il n'y pas lieu d'indiquer un renvoi.

Quelques accessoires courants sont proposés pour accélérer la rédaction d'une fiche.
Pour les accessoires qui ne sont pas proposés au choix, on veillera à respecter les mêmes conventions de nommage, notamment pour ce qui concerne les abréviations:

- Réc. : Récit
- G.O. : Grand orgue
- Pos. : Positif
- Ped. : Pédale
- G.C. : Grand choeur
- Bom. : Bombarde


----

## Images

On veillera à joindre des images de bonne qualité et bonne résolution, sans toutefois que leur taille n'excède 2 Mo.
Par image, on parle ici de documents purement visuels, c'est-à-dire des dessins, croquis et photos.
Les autres documents doivent être déposés sur le site comme des fichiers. (Cf. ci-après.)

Il faut désigner une des images comme image principale, à savoir celle qui apparaîtra en tête de la fiche sur le portail, et dans l'index de tous les orgues.

La rubrique crédit doit obligatoirement être renseignées. Toutes les images déposées sur le site sont impérativement en licence ouverte permettant une libre réutilisation, commerciale ou non.
Cf. la [foire aux questions](faq.md) pour toutes les questions ayant trait au droit d'auteur.

----

## Fichiers

Touts les fichiers déposées sur le site sont impérativement en licence ouverte permettant une libre réutilisation, commerciale ou non.
Cf. la [foire aux questions](faq.md) pour toutes les questions ayant trait au droit d'auteur.
