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
