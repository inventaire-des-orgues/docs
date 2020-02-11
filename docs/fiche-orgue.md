# Structure de la fiche descriptive d'un orgue de l'inventaire

[TODO] Reprendre fiche type des orgues d'Ile-de-France (Pierre Dumoulin).

La structure de la fiche décrivant un orgue est le coeur de l'inventaire. Elle a fait l'objet de longues réflexions, 
dans le but d'aboutir à un juste compromis entre niveau de détails suffisant et complexité limitée.
La saisie d'une fiche est facilitée par l'organisation en plusieurs grandes rubriques, 
qui prennent la forme de différents onglets sur le portail de l'inventaire.

## Informations générales

### Edifice

Valeur_par_defaut = ""

Le nom de l'édifice hébergeant l'orgue. Il s'agit très souvent d'églises ou de temples.
La désignation des édifices peut prêter à discussion car, pour de grands édifices, il est fréquent qu'elle ait changé au cours des siècles.

### Désignation

La désignation d'un orgue pose très souvent problème. En effet, le titre "Grand orgue" est subjectif, emphatique, et vaut généralement par opposition au titre "Orgue de choeur".
C'est l'option adoptée pour l'inventaire : par défaut, on parlera simplement d'un "Orgue", et en employera les désignations de ""


    "Grand orgue",
    "Orgue de choeur",
    "Orgue"

Valeur_par_defaut = "Orgue"

### Etat de fonctionnement
Il s'agit d'un avis à date de mise à jour de la fiche descriptive. Nécessairement pour partie subjectif, il est rapporté à l'utilisation possible de l'instrument. Les défauts courants et réversible d'un orgue (cornement occasionnel par exemple) ne rentrent pas en compte dans l'appréciation. L'état de fonctionnement ne décrit pas l'état du buffet ou des boiseries dès lors qu'il n'altère pas le jeu.

Valeur_par_defaut = Néant

    "Très bon ou bon : tout à fait jouable",
    "Altéré : difficilement jouable",
    "Dégradé ou en ruine : injouable"

### Elévation
Permet la distinction, dans la majorité des cas, entre orgue de choeur et orgue de tribune.

Valeur_par_defaut = Néant

    "en tribune",
    "au sol"

Nota : Emplacement dans l'édifice.
A ce stade, aucun attribut n'est prévu pour préciser la position de l'orgue dans l'édifice.
Dans le cas de plusieurs instruments au sein d'un même édifice, l'attribut élévation et les coordonnées géographiques permettent de positionner et distinguer précisément l'instrument.

### Orgues polyphones de Louis Debierre
is_polyphone [bool] spécifie si l'orgue est un polyphone de la manufacture Debierre.
Les polyphones sont des orgues coffres dont certains tuyaux de basse permettent l'émission de plusieurs notes distinctes.
(Musica et memora)[http://www.musimem.com/debierre.htm]

Valeur_par_defaut = False

### Propriété de l'orgue
Le propriétaire de l'orgue (qui n'est pas nécessairement le même que l'édifice).
Le plus souvent, il s'agit de la commune pour des instruments datant d'avant 1905 (de l'Etat pour les orgues de cathédrales), et d'association cultuelle (généralement paroisse) pour les orgues d'après 1905 ou de congrégation.
Bien sûr, il existe plusieurs exceptions : par exemple, les orgues des cathédrales de la petite couronne parisienne, n'appartiennent pas à l'Etat, mais l'orgue de la basilique royale de Saint-Denis si.

Valeur_par_defaut= commune

    "commune",
    "Etat",
    "association culturelle",
    "diocèse",
    "paroisse"

### Organisme de référence

Valeur_par_defaut = ""

Libellé du lien, et lien, vers un organisme, le plus souvent une association, au plus proche de l'instrument.
Il s'agit de l'organisme le plus à même de fournir un renseignement ou un contact pour visiter et jouer l'orgue.
Le libellé du lien est le terme qui apparaîtra comme lien dans la visualisation de la fiche (cartouche de synthèse).

### Résumé

champ_texte

Valeur_par_defaut = ""

Cette courte description est une synthèse rédigée sur l'histoire de l'instrument.
Elle doit être utilisée pour évoquer une particularité de l'instrument, ce qui fait son originalité et sa valeur.

### Commentaire admin

Valeur_par_defaut = ""

Ce commentaire n'est visible qu'en mode édition et sera affiché sur fond coloré en haut de la fiche lors de l'édition.
Il sert à transmettre une information entre rédacteurs de la fiche.
Par exemple : "La description de la tuyauterie est à compléter", ou "Nous ne sommes pas certain de la composition du Récit".

## Localisation

### Commune

Il s'agit de la commune selon le dernier [code officiel géographique](https://www.insee.fr/fr/information/2560452) en vigueur de l'INSEE.
Attention, de nombreuses communes ont fusionné au cours des dernières années, et de tels regroupements se poursuivront dans les années à venir.
Il faut donc prendre garde à ne pas renseigner le nom d'une ancienne commune, même s'il continue à être usuellement utilisé. L'attribut Ancienne commune est dédié à cela.

### Code INSEE

Code de la commune selon le code géographique officiel de l'INSEE. On le trouve aussi généralement dans la fiche de la commune sur Wikipédia.
Il est unique, et donc distinct du code postal utilisé pour l'adressage du courrier.

### Ancienne commune

Cet attribut est une aide pour faciliter la localisation.
Il est à prendre dans une acceptation large : il peut s'agir d'une ancienne commune disparue suite à un regroupement de communes, 
d'une commune déléguée, d'une commune associée, ou bien d'un simple lieu-dit.

### Code département

Code du département selon le code géographique officiel de l'INSEE.

### Département

Nom du département selon le code géographique officiel de l'INSEE.

### Région

Nom de la région selon le code géographique officiel de l'INSEE.

### Latitude

Latitude selon le système de coordonnées WGS84, couramment connu comme "coordonnées GPS". Nota : celui-ci n'est pas le système de coordonnées officiel français.
Pour des facilités de saisie et d'export des données, le format adopté est un nombre réel signé, et non la notation en degrés, minutes et secondes.

Cf. la [page sur OSM](osm.md).

### Longitude

Cf. latitude.

Cf. la [page sur OSM](osm.md).

### Type OpenStreetMap

Type d'objet selon la nomenclature utilisée par le projet [OpenStreetMap](https://www.openstreetmap.org).
Il peut s'agir :
- way : d'un chemin, ensemble de points
- node : d'un simple points
- relation : d'une combinaison libre de ces trois types d'objets

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
On ne distingue que Inscription au titres des monuments historiques et Classement au titre des monuments historiques, comme objets evenement. Le champ TICO de Palissy sera mis dans le commentaire de l'évenement.
De même pour les autres champs issus de la mise en correspondance entre l'inventaire et la base Palissy, par exemple le numéro d'arrêté de classement ou inscription.

## Buffet

Champ libre [string sans limite de taille] pour la description du buffet et de son état.

Valeur_par_defaut = Néant

La notion de console est assez récente : elle survient avec l'apparition de meubles séparés du buffet au XIXe siècle, souvent tournés vers l'autel ou mobiles au XXe siècle.
Aussi n'y a-t-il pas de champ dédié et la console peut-être, le cas échéant, décrite dans un sous-chapitre de la section buffet.

Les types les plus courants sont :
- en fenêtre
- séparée, organiste tourné vers l'orgue
- séparée, organiste dos à l'orgue

Dans le cas d'une console mobile ou en fenêtre sur le côté ou l'arrière de l'instrument, on précisera la disposition.
Idem dans le cas d'une seconde console.

## Partie instrumentale

### Transmission des notes

Le type de transmission des notes est indiqué pour tout l'instrument, et non par clavier.
Lorsque les claviers disposent d'un autre mode de transmission que celle généralement ou originellement utilisée pour l'instrument (ex: pédalier à transmission électrique) seront précisés dans les commentaires du clavier.

    "Mécanique",
    "Mécanique suspendue",
    "Mécanique à balanciers",
    "Mécanique Barker",
    "Pneumatique",
    "Electrique",
    "Electro-pneumatique"

### Diapason
Valeur_par_defaut = Néant

Hauteur en hertz du A2 donné par le Prestant 4 ou équivalent.

### Transmission des registres

Le type de transmission des notes est indiqué pour tout l'instrument

    "Mécanique",
    "Pneumatique",
    "Electrique",
    "Electro-pneumatique"
    
### Sommiers
Champ texte libre [string]

Valeur_par_defaut = Néant

### Soufflerie
Champ texte libre [string]

Valeur_par_defaut = Néant

## Composition

### Composition

La composition distingue plusieurs plans sonores.

Un plan sonore est nommé et son étendue est précisée sous la forme suivante :
C1-G5

Cf. [le lexique de l'inventaire](https://vocabulaire.inventaire-des-orgues.fr/)
et [Wikipédia](https://fr.wikipedia.org/wiki/Liste_des_jeux_d%27orgue)

Valeur_par_defaut = "Bourdon 8"

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

### Description de la tuyauterie

Commentaire général sur la tuyauterie et description jeu par jeu, dans l'ordre de la composition.

Note importante : Une seule notation doit être retenue dans l'inventaire des orgues pour la description des notes : les octaves sont numérotées de 1 à 6.
C1, C#1, D1, D#1...

Pour

### Accessoires

Valeur_par_defaut = Néant

Les accessoires peuvent être :
- accouplement :
    - on peut préciser s'il s'agit d'un accouplement classique à l'unisson, à l'octave basse ou bien à l'octave aigüe.
    - On peut aussi préciser le clavier accouplé et le clavier jouant avec l'accouplement.
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


## Images

On veillera à joindre des images de bonne qualité et bonne résolution, sans toutefois que leur taille n'excède 2 Mo.
Par image, on parle ici de documents purement visuels, c'est-à-dire des dessins, croquis et photos.
Les autres documents doivent être déposés sur le site comme des fichiers. (Cf. ci-après.)

Il faut désigner une des images comme image principale, à savoir celle qui apparaîtra en tête de la fiche sur le portail, et dans l'index de tous les orgues.

La rubrique crédit doit obligatoirement être renseignées. Toutes les images déposées sur le site sont impérativement en licence ouverte permettant une libre réutilisation, commerciale ou non.
Cf. la [foire aux questions](faq.md) pour toutes les questions ayant trait au droit d'auteur.

## Fichiers

Touts les fichiers déposées sur le site sont impérativement en licence ouverte permettant une libre réutilisation, commerciale ou non.
Cf. la [foire aux questions](faq.md) pour toutes les questions ayant trait au droit d'auteur.
