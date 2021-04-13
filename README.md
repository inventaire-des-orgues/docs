# La documentation de l'Inventaire national des orgues

Le site de [documentation](https://docs.inventaire-des-orgues.fr) pour l'inventaire des orgues. 


## Nouvelle documentation

Une [documentation](https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/) sur Markdown

La documentation est générée depuis Markdown en HTML à l'aide de l'utilitaire Python de génération de site statiques Mkdocs (https://www.mkdocs.org)

Pour générer le site de documentation avec Mkdocs et éventuellement lancer le [serveur local](http://127.0.0.1:8000) :

1. installer le module mkdocs avec pip
2. construire le site statique :
  a- soit depuis une console, via la ligne de commande `mkdocs build`
  b- soit directement depuis Python via un script de lancement `generate.py` adapté depuis [un exemple trouvé sur le web](https://github.com/ASoftTech/Gbd.IO.Serial/blob/master/Docs/MkDocs/build.py)

Le fichier de configuration, en langage yaml, peut-être [personnalisé](https://www.mkdocs.org/user-guide/configuration/).

Lors d'un *push* sur le dépôt Github, une *Action* Github déploie automatiquement la documentation sur le serveur de l'inventaire des orgues :

- les sources en format Markdown sont copiées sur ce serveur,
- la documentation est immédiatement regénérée,
- les fichiers HTML déployés et le serveur Nginx redémarré.

Causes d'échec du déploiement automatique déjà rencontrées :

- une erreur d'encodage peut mettre en echec la commande `mkdocs build`
- il y a pu avoir désynchronisation du dépôt Git du serveur en cas de modification directement dessus. Solution :
  - `git fetch --all`
  - `git reset --hard github_inventairedesorgues/master`
  - `git pull github_inventairedesorgues master`
  - `mkdocs build`


## Pour mémoire : ancienne documentation

Initialement, ce site avait été mis en place par Bastien Guerry à l'aide de :
- module Org mode pour l'éditeur EMACS (https://github.com/fniessen/refcard-org-mode)
- modèle ReadTheOrg (https://github.com/fniessen/org-html-themes)

Le fichiers .org ont pour ce faire été convertis en fichiers Markdown .md façon Github Flavored Markdown (style gfm)(https://pandoc.org/MANUAL.html#atx-style-headings), à l'aide de l'outil Pandoc (https://pandoc.org).

```
./pandoc --from org --to gfm -o ido-docs/donnees.md ido-docs/donnees.org
```

