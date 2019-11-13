# La documentation de l'inventaire national des orgues

Le site de [documentation](https://docs.inventaire-des-orgues.fr) pour l'inventaire des orgues. 

## Ancienne documentation

Initialement, ce site avait été mis en place par Bastien Guerry à l'aide de :
- module Org mode pour l'éditeur EMACS (https://github.com/fniessen/refcard-org-mode)
- modèle ReadTheOrg (https://github.com/fniessen/org-html-themes)

## Nouvelle documentation

Le fichiers .org ont pour ce faire été convertis en fichiers Markdown .md façon Github Flavored Markdown (style gfm)(https://pandoc.org/MANUAL.html#atx-style-headings), à l'aide de l'outil Pandoc (https://pandoc.org).

```
./pandoc --from org --to gfm -o ido-docs/donnees.md ido-docs/donnees.org
```

Une [documentation](https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/) sur Markdown

La documentation est générée depuis Markdown en HTML à l'aide de l'utilitaire Python de génération de site statiques Mkdocs (https://www.mkdocs.org)

Pour générer le site de documentation avec Mkdocs et éventuellement lancer le [serveur local](http://127.0.0.1:8000) :
1- installer le module mkdocs avec pip
2a- soit depuis une console, via la ligne de commande `mkdocs build`
2b- soit directement depuis Python via un script de lancement `generate.py` adapté depuis [un exemple trouvé sur le web](https://github.com/ASoftTech/Gbd.IO.Serial/blob/master/Docs/MkDocs/build.py)

Le fichier de configuration, en langage yaml, peut-être [personnalisé](https://www.mkdocs.org/user-guide/configuration/).