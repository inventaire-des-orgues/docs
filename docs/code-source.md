# Code source

## Quelles sont les technologies utilisées pour le portail de l'inventaire ?
- Le portail est codé en langage Python, en utilisant le framework Django, dédié aux applications internet, ainsi que Bootstrap pour les feuilles de style CSS et un peu de Javascript. Les cartes employent la librairie Javascript Leaflet. Les fonds de cartes proviennent d'OpenStreetMap.
- Les utilitaires de traitement des données sont aussi codés en Python.
- La documentation est rédigée au format Markdown et compilée sous forme de site web statique à l'aide du module Python Mkdocs.
- La reconnaissance de caractères des livres numérisés a été effectuée à l'aide du logiciel non libre ABBYY.
- Les fichiers PDF produits ont été manipulés et réagencés à l'aide de l'outil PDFTK et de l'interface graphique PDFTKBuilder, ainsi qu'à l'aide de scripts Python faisant appel à au module PyPDF2.

## Dépôts de code

Le code source des applications développées pour l’Inventaire national des orgues
est disponible sur [GitHub](https://github.com/inventaire-des-orgues/)

| Nom                                                                         | Description                                                               | Langage               | Licence    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------- | ---------- |
| [portail](https://github.com/inventaire-des-orgues/portail)                 | Le site Internet de l'inventaire                                          | Python, javascript, HTML, CSS |  	GNU GPLv3+   |
| [docs](https://github.com/inventaire-des-orgues/docs)                       | Le site de documentation                                                  | Markdown/MkDocs       |  	GNU GPLv3+           |
| [paillasse](https://github.com/inventaire-des-orgues/paillasse)             | Utilitaires de construction de l'index                                    | Python                |  	GNU GPLv3+           |


## Dépôts de données

Cf. aussi la page sur les [données](donnees.md).

| Nom                                                                         | Description                                                               | Format                | Licence    |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------- | ---------- |
| [livres](https://github.com/inventaire-des-orgues/livres)                   | L'index des livre d'inventaire                                            | Excel                 |            |
| [indexes](https://github.com/inventaire-des-orgues/indexes)                 | L'index des orgues de l'inventaire                                        | JSON, CSV             |            |
