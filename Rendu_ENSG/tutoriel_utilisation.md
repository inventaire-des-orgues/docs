# Présentation générale du site

Lors de l'arrivée sur le site l'utilisateur peut naviguer entre cinq onglets. Il a le choix entre la page d'accueil qui est ouverte par défaut, la carte de localisation des orgues, la recherche sur les orgues, le lexique et une foire aux questions (FAQ).

## Accueil

## Carte

## Les orgues

## Lexique

## Questions/Réponses

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
