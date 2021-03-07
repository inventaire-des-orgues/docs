# Aspects techniques

## Hébergement de la plate-forme

L’application principale est hébergée sur une machine virtuelle louée
chez *DigitalOcean* et physiquement située à Amsterdam.

L'application annexe de recherche avancées dans les livres d'inventaire numérisés est hébergée sur une autre machine virtuelle, aussi chez *DigitalOcean*.

### Sauvegarde des données

- Le service DigitalOcean permet une sauvegarde complète de la machine
toutes les semaines (administration, fiches descriptives des orgues, images).

- Un crontab permet une sauvegarde quotidienne par simple copie sur le serveur de la base de données SQLite (administration et fiches descriptives).

### Services web externes

  - gandi.net
    service de location de noms de domaine.

  - digitalocean.com
    service de location de machines virtuelles.

### Noms de domaine et adresses email utilisés

  - inventaire-des-orgues.fr
    nom de domaine principal, utilisé pour le portail et les services
    associés. Pas de service mail actif sur ce nom de domaine depuis
    gandi.net. La zone DNS est gérée par les serveurs DNS de
    digitalocean : `ns1.digitalocean.com`. Tous les emails envoyés à
    `@inventaire-des-orgues.fr` sont redirigés vers
    l’adresse des administrateurs.

### Domaines, sous-domaines et services associés

| Sous-domaine                      | Service           | Logiciel associé |
| --------------------------------- | ----------------- | ---------------- |
| inventaire-des-orgues.fr      | Portail du projet | Django           |
| docs.inventaire-des-orgues.fr     | Blog du projet    | MkDocs       |
| fichiers.inventaire-des-orgues.fr | Fichiers partagés | Nextcloud    |


## Déploiement

Deux chaînes d'intégration continue (une pour le portail, une autre pour la documentation) sont mises en place.
Elles sont basées sur le module 'Actions' de Github.
La recopie et le déploiement sur le serveur sont déclenchés à chaque action push vers le dépôt distant Github.

### Dépôts de code sur Github

  - [portail](https://github.com/inventaire-des-orgues/portail)
  
  - [docs](https://github.com/inventaire-des-orgues/docs)

  - [livres](https://github.com/inventaire-des-orgues/livres)

  - [Indexes](https://github.com/inventaire-des-orgues/indexes)
  
  - [Organslist](https://github.com/inventaire-des-orgues/organslist)
  
  - [Organslexicon](https://github.com/inventaire-des-orgues/organslexicon)

  - [API](https://github.com/inventaire-des-orgues/api)


## Langages, frameworks et système de base de données

### Langages et frameworks

- Le portail est codé en langage Python, en utilisant le framework Django, dédié aux applications web, ainsi que Bootstrap pour les feuilles de style CSS et un peu de Javascript. Les cartes employent Leaflet. Les fonds de cartes proviennent d'OpenStreetMap.
- Les utilitaires de traitement des données sont aussi codés en Python.
- La documentation est rédigée au format Markdown et compilé sous forme de site web statique à l'aide du module Python Mkdocs.
- La reconnaissance de caractères des livres numérisés a été effectuée à l'aide du logiciel non libre ABBYY.
- Les fichiers PDF produits ont été manipulés et réagencés à l'aide de l'outil PDFTK et de l'interface graphique PDFTKBuilder.
- Les livres numérisés sont proposés sur la plate-forme Datashare.

### Système de base de données

Le système de base de données utilisé est SQLite.

## Logiciels libres utilisés

  - [DataShare] Recherche dans les livres scannés
  
  - [Python] Documentation et portail
  
  - [Django] Portail
  
  - [PDFTK] Manipulation de fichiers PDF
  
  - [PDFTKBuilder] Manipulation de fichiers PDF
  
  - [Nextcloud](https://nextcloud.com/)  
    Logiciel libre pour le partage de fichiers

