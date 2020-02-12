# Code source

## Quelles sont les technologies utilisées pour le portail de l'inventaire ?
- Le portail est codé en langage Python, en utilisant le framework Django, dédié aux applications web, ainsi que Bootstrap pour les feuilles de style CSS et un peu de Javascript. Les cartes employent la librairie Javascript Leaflet. Les fonds de cartes proviennent d'OpenStreetMap.
- Les utilitaires de traitement des données sont aussi codés en Python.
- La documentation est rédigée au format Markdown et compilée sous forme de site web statique à l'aide du module Python Mkdocs.
- La reconnaissance de caractères des livres numérisés a été effectuée à l'aide du logiciel non libre ABBYY.
- Les fichiers PDF produits ont été manipulés et réagencés à l'aide de l'outil PDFTK et de l'interface graphique PDFTKBuilder, ainsi qu'à l'aide de scripts Python faisant appel à au module PyPDF2.

## Dépôts de code

Le code source des applications développées pour l’inventaire des orgues
est disponible :

- sur [GitHub](https://github.com/inventaire-des-orgues/) pour les outils en service
- sur la [forge dédiée](https://git.inventaire-des-orgues.fr/) pour les prototypes

| Nom                                                                         | Description                                                               | Langage               | Licence    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------- | ---------- |
| [portail](https://github.com/inventaire-des-orgues/portail)                 | Le site Internet de l'inventaire                                          | Python, javascript, HTML, CSS |  	GNU GPLv3+   |
| [docs](https://github.com/inventaire-des-orgues/docs)                       | Le site de documentation                                                  | Markdown/MkDocs       |  	GNU GPLv3+           |
| [paillasse](https://github.com/inventaire-des-orgues/paillasse)             | Utilitaires de construction de l'index                                    | Python                |  	GNU GPLv3+           |
|                                                                             |                                                                           |                       |            |
| [OrgansLexicon](https://github.com/inventaire-des-orgues/organslexicon)     | Application pour l'affichage du vocabulaire de l'orgue                    | Clojure/Clojurescript | Apache 2.0 |
| [OrgansList](https://github.com/inventaire-des-orgues/organslist)           | Prototype de mise en ligne de l'index                                     | Clojure/Clojurescript | Apache 2.0 |
| [Api](https://github.com/inventaire-des-orgues/api)                         | API pour le vocabulaire et l'index                                        | Clojure/Clojurescript | Apache 2.0 |
|                                                                             |                                                                           |                       |            |
| [Legito](https://git.inventaire-des-orgues.fr/bzg/legito)                   | Prototype de portail                                                      | Clojure/Clojurescript | Apache 2.0 |
| [ox-skos.el](https://git.inventaire-des-orgues.fr/bzg/ox-skos)              | Outil d’export vers le format SKOS                                        | Emacs Lisp            | GNU GPLv3+ |
| [Ghislaine](https://git.inventaire-des-orgues.fr/bzg/ghislaine)                     | Application de visualisation d’export Gertrude                            | Clojure/Clojurescript | Apache 2.0 |
| [ido-docs](https://git.inventaire-des-orgues.fr/bzg/ido-docs)               | Sources de l'ancien site de documentation                                 | Markdown/Jekyll       |            |
| [clj-rgf93-wgs84](https://git.inventaire-des-orgues.fr/bzg/clj-rgf93-wgs84) | Bibliothèque de conversion de Lambert93 vers WGS84                        | Clojure               | Apache 2.0 |
| [Tempero](https://git.inventaire-des-orgues.fr/bzg/tempero)                 | Outils de traitement des données Gertrude                                 | Clojure               | Apache 2.0 |
| [rbc-owl](https://git.inventaire-des-orgues.fr/bzg/rbc-owl)                 | Outil d’exploration du schéma HADOC en .owl                               | Clojure               | Apache 2.0 |







## Dépôts de données

Cf. aussi la page sur les [données](donnees.md).

| Nom                                                                         | Description                                                               | Format                | Licence    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------- | ---------- |
| [vocabulaire](https://github.com/inventaire-des-orgues/vocabulaire)         | Le lexique de la facture d'orgue                                          | JSON, CSV, ODS        |            |
| [livres](https://github.com/inventaire-des-orgues/livres)                   | L'index des livre d'inventaire                                            | Excel                 |            |
| [indexes](https://github.com/inventaire-des-orgues/indexes)                 | L'index des orgues de l'inventaire                                        | JSON, CSV             |            |

### API

- [vocabulaire](http://api.inventaire-des-orgues.fr/vocabulaire)
- [orgues](http://api.inventaire-des-orgues.fr/orgues)

### Visualisation simplifiée

- [liste](https://liste.inventaire-des-orgues.fr)