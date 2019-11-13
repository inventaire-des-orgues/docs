# Fiche descriptive minimale de l'orgue

Les termes en lettres majuscules et entre parenthèses correspondent au
nom des champs dans la base de données Palissy.

La fiche contiendra trois volets :

  - la description de la partie instrumentale ;
  - celle du buffet d'orgue ;
  - celle de l'édifice contenant l'orgue.

La description de la partie instrumentale contiendra elle-même :

  - une liste de propriétés « générales » ;
  - une description des composants matériels ;
  - la composition des jeux ;
  - un historique ;
  - des données extérieures.

À noter que des propriétés générales (comme le fait « d'être un Merklin
») pourront être *affichées* dans la présentation sommaire de l'orgue,
mais seulement *éditée* depuis l'historique de l'orgue.

## Partie instrumentale ou phonique

### Propriétés générales

| Champ                                                            | Type de données | Lexique associé    |
| ---------------------------------------------------------------- | --------------- | ------------------ |
| Auteur                                                           | Structuré       | AUTR               |
| Appellations (par ex: "grand orgue", cf. thesaurus)              | Structuré       | TICO               |
| Appréciation générale sur l'état (ETAT)                          | Texte libre ?   | ETAT ?             |
| État (jouable, etc.)                                             | Texte libre ?   | Lexique existant ? |
| Référence/lien dans Palissy (REF)                                | Structuré       | REF                |
| Affectataire                                                     | Texte libre     |                    |
| Facteur assurant l'entretien                                     | Texte libre     |                    |
| Procédure et conditions d'accès à l'instrument                   | Texte libre     |                    |
| Propriétaire (ou statut (STAT) ?)                                | Structuré ?     | STAT ?             |
| Observations (OBS)                                               | Texte libre     |                    |
| Inscription/classement MH                                        | texte libre     |                    |
| Intérêt (INTE)                                                   | Structuré       | Thesaurus ?        |
| Date notice (Palissy/Gertrude) par contributeur (DMIS/DMAJ/PERS) | Date            |                    |

### Description des composants

| Champ                     | Type de données | Lexique associé   |
| ------------------------- | --------------- | ----------------- |
| Accessoires               | Texte libre     |                   |
| Accouplements et tirasses | Texte libre     |                   |
| Alimentation              | Texte libre     |                   |
| Boîte expressive          | Texte libre     |                   |
| Combinateur               | Texte libre     |                   |
| Claviers                  | Texte libre     |                   |
| Console                   | Texte libre     |                   |
| Diapason et température   | Texte libre     |                   |
| Meuble de console         | Texte libre     |                   |
| Pédalier                  | Texte libre     |                   |
| Sommiers I                | Texte libre     |                   |
| Sommiers II               | Texte libre     |                   |
| Sommiers III              | Texte libre     |                   |
| Sommiers IV               | Texte libre     |                   |
| Sommiers V                | Texte libre     |                   |
| Sommiers pédale           | Texte libre     |                   |
| Soufflerie / pressions    | Texte libre     |                   |
| Tempérament               | Structuré       | Vocabulaire orgue |
| Transmission des notes    | Structuré       | Vocabulaire orgue |
| Transmission des jeux     | Structuré       | Vocabulaire orgue |
| Tuyauterie                | Texte libre     |                   |

### Composition

Nous proposons de présenter la composition de l'orgue en séparant la
liste des claviers (incluant la pédale) et la liste des jeux, chaque jeu
étant bien sûr associé à un clavier.

Pour les claviers :

| Champ             | Type de données     | Lexique associé      |
| ----------------- | ------------------- | -------------------- |
| Nom               | Chaîne de caractère | Lexique des claviers |
| Inscription       | Texte libre         | Aucun                |
| Nombre de touches | Nombre              | Aucun                |
| Commentaire       | Texte libre         | Aucun                |

Pour les jeux :

| Champ                    | Type de données     | Lexique associé                |
| ------------------------ | ------------------- | ------------------------------ |
| Nom                      | Chaîne de caractère | Lexique des jeux               |
| Inscription              | Texte libre         | Aucun                          |
| Hauteur / Tessiture      | Texte libre         | Aucun                          |
| Première / dernière note | Structuré           | XX / XX avec mini 1 et maxi 73 |
| Rangs                    | Texte libre         |                                |
| Clavier associé          | Clavier             | Lexique des claviers           |
| Matériaux                | Texte libre         |                                |
| Commentaire              | Texte libre         | Aucun                          |
| Accessoires              | Texte libre         |                                |

**Attention** : les emprunts, extensions et accouplements seraient ainsi
décrits dans un champ distinct, non en regard de la description des
jeux.

Si nous prenons la [description de l'ancien orgue de
Bazas](http://orgue-aquitaine.fr/Ancien-orgue-de-Bazas-Cathedrale-Saint-Jean-Baptiste.html),
nous aurions donc trois "claviers" (Grand-Orgue, Récit expressif et
Pédale) avec respectivement 54, 54 et 27 "touches".

Nous aurions en outre 19 jeux, dont 17 sont associés à un seul clavier
et deux d'entre eux sont associés à deux claviers (la bombarde 16 et la
trompette 8).

En supposant que l'inscription du jeu (sur la tirasse) est semblable au
nom du jeu, cela donne ce tableau de données :

| Jeu (et inscription) | Hauteur | Clavier(s) associé(s)   |
| -------------------- | ------- | ----------------------- |
| Basson-Hautbois      | 8       | Récit expressif         |
| Bombarde             | 16      | Récit expressif, pédale |
| Bourdon              | 16      | Grand-Orgue             |
| Bourdon              | 8       | Grand-Orgue             |
| Clairon              | 4       | Récit expressif         |
| Contrebasse          | 16      | Pédale                  |
| Flûte                | 8       | Pédale                  |
| Flûte harmonique     | 8       | Grand-Orgue             |
| Flûte octaviante     | 4       | Récit expressif         |
| Flûte à pavillon     | 8       | Récit expressif         |
| Kérolophone          | 8       | Grand-Orgue             |
| Montre               | 8       | Grand-Orgue             |
| Octavin              | 2       | Grand-Orgue             |
| Prestant             | 4       | Grand-Orgue             |
| Salicional           | 8       | Grand-Orgue             |
| Trompette            | 8       | Récit expressif, pédale |
| Violoncelle          | 8       | Récit expressif         |
| Voix Céleste         | 8       | Récit expressif         |
| Voix Humaine         | 8       | Récit expressif         |

N'hésitez pas à commenter cette proposition sur la [page du
forum](https://forum.inventaire-des-orgues.fr/t/description-de-la-composition-dun-orgue/65).

### Historique

| Champ                                       | Type de données | Lexique associé |
| ------------------------------------------- | --------------- | --------------- |
| En YYYY, l'orgue est construit par A        |                 |                 |
| En YYYY, l'orgue est restauré par A         |                 |                 |
| En YYYY, l'orgue est déplacé de A à B       |                 |                 |
| EN YYYY, l'orgue a pour nouveau titulaire A |                 |                 |
| EN YYYY, orgue est protégé en tant que XXX  |                 |                 |
| En YYYY, date d'enquête (DENQ)              |                 |                 |
| En YYYY, date bordereau (DBOR)              |                 |                 |
| Date de contrat d'entretien                 |                 |                 |

### Données extérieures

| Champ                                                    | Type de données | Lexique associé |
| -------------------------------------------------------- | --------------- | --------------- |
| Archives (paroissiales, diocésaines, associatives, etc.) | Texte libre     |                 |
| Bibliographie                                            | Texte libre     |                 |
| Vidéo (+ auteur, licence, description)                   | Fichier         |                 |
| Audio (+ auteur, licence, description)                   | Fichier         |                 |
| Photo (+ auteur, licence, description)                   | Fichier         |                 |
| Discographie                                             | Texte libre     |                 |
| Documentation                                            | Texte libre     |                 |

## Buffet

| Champ                             | Type de données | Lexique associé |
| --------------------------------- | --------------- | --------------- |
| Description (DESC)                | Texte libre     |                 |
| Décor (REPR)                      | Texte libre     |                 |
| Inscriptions (INSC)               | Texte libre     |                 |
| Auteur(s) (AUTR)                  | Texte libre     |                 |
| Historique (DATE)                 | Date structurée |                 |
| Matériau (MATR)                   | Structuré       | Matériaux       |
| État (ETAT)                       | Structuré       | État            |
| Inscription/classement MH         | texte libre     |                 |
| Référence/lien dans Palissy (REF) | Structuré       | REF             |

## Édifice contenant l'orgue

| Champ                                                               | Type de données | Lexique associé |
| ------------------------------------------------------------------- | --------------- | --------------- |
| Localisation (Adresse postal, coordonnées GPS)                      | Texte libre     |                 |
| Titre courant (Dénomination/Genre/Appellation/Titre)                | Structuré       |                 |
| Propriétaire                                                        | Texte libre     |                 |
| Protection MH                                                       | Structuré       | Protection      |
| Référence/lien dans Mérimée (REFA)                                  | Structuré       | REFA            |
| Localisation de l'instrument dans l'édifice et accès à l'instrument | Texte libre     |                 |
| Nombre de places assises                                            | Nombre          |                 |
| Acoustique de l'édifice                                             | Texte libre     | ?               |

# Contribuer à construire la fiche

Pour contribuer à faire évoluer cette fiche, vous pouvez :

  - télécharger sa version [odt](data/docs/modele_orgue_complet.odt) ou
    [docx](data/docs/modele_orgue_complet.docx) et
    [m'envoyer](mailto:bzg@bzg.fr) une version modifiée, si possible
    avec le suivi de modifications ;

  - ou participer à la discussion sur le
    [forum](https://forum.inventaire-des-orgues.fr/t/fiche-descriptive-minimale-de-lorgue/21)
    ;

  - m'envoyer un [simple email](mailto:bzg@bzg.fr).

# Questions

  - Quels éléments importants manquent encore ?

  - Est-ce que la structuration actuelle est la bonne ?

  - Faut-il indiquer l'état seulement pour le buffet et la partie
    instrumentale de l'orgue, ou bien la tuyauterie, etc ?

# Autres sources pour construire la fiche minimale

  - Les inventaires papiers
  - La fiche « Orgue » du plan 1990 ([lien](fiche-orgue-plan-1990.org))
