# Hébergement de la plate-forme

L’application principale est hébergée sur une machine virtuelle louée
chez *DigitalOcean* et physiquement située à Amsterdam.

## Sauvegarde des données

Le service DigitalOcean permet une sauvegarde complète de la machine
toutes les semaines.

# Langages, frameworks et système de base de données

## Langages et frameworks

- Le portail est codé en langage Python, en utilisant le framework Django, dédié aux applications web, ainsi que Bootstrap pour les feuilles de style CSS et un peu de Javascript. Les cartes employent Leaflet. Les fonds de cartes proviennent d'OpenStreetMap.
- Les utilitaires de traitement des données sont aussi codés en Python.
- La documentation est rédigée au format Markdown et compilé sous forme de site web statique à l'aide du module Python Mkdocs.
- La reconnaissance de caractères des livres numérisés a été effectuée à l'aide du logiciel non libre ABBYY.
- Les fichiers PDF produits ont été manipulés et réagencés à l'aide de l'outil PDFTK et de l'interface graphique PDFTKBuilder.
- Les livres numérisés sont proposés sur la plate-forme Datashare.

## Système de base de données

Le système de base de données utilisé est SQLite.

## Déploiement

Deux chaînes d'intégration continue (une pour le portail, une autre pour la documentation) sont mises en place.
Elles sont basées sur le module 'Actions' de Github.
La recopie et le déploiement sur le serveur sont déclenchés à chaque action push vers le dépôt distant Github.

# Liste des logiciels libres utilisés

  - [DataShare]
  
  - [Python]
  
  - [Django]
  
  - [PDFTK]
  
  - [PDFTKBuilder]
  
  - [Discourse](https://www.discourse.org)  
    Logiciel libre de forum.

  - [Docker](https://www.docker.com/)  
    Logiciel libre pour « containeriser » des services. En l’occurrence,
    Piwik, Discourse et Nextcloud sont lancés sur le serveur depuis
    docker.

  - [Gogs](https://gogs.io/)  
    Logiciel libre pour publier une forge de projets sous git.

  - [Jekyll](https://jekyllrb.com)  
    Logiciel libre pour construire des blogs en HTML statique.
    Nécessaire de connaître le langage
    [Markdown](https://fr.wikipedia.org/wiki/Markdown) pour écrire.

  - [Letsencrypt](https://letsencrypt.org/)  
    Service gratuit pour l’obtention de certicats SSL/TLS valides,
    utilisé pour le passage en `https` de tous les services.

  - [Nextcloud](https://nextcloud.com/)  
    Logiciel libre pour le partage de fichiers en ligne.

  - [Piwik](https://piwik.org/)  
    Logiciel libre pour la collecte de données sur les visites d’un site
    web.

# Dépôts de code

Dépôts principaux sur placé sur Github :

  - [Portail](https://github.com/inventaire-des-orgues/portail)
  
  - [Docs](https://github.com/inventaire-des-orgues/docs)

  - [Indexes](https://github.com/inventaire-des-orgues/indexes)
  
  - [Organslist](https://github.com/inventaire-des-orgues/organslist)
  
  - [Organslexicon](https://github.com/inventaire-des-orgues/organslexicon)

  - [API](https://github.com/inventaire-des-orgues/api)
  
Liste des dépôts disponibles depuis *la forge* du projet :

  - [legito](https://git.inventaire-des-orgues.fr/bzg/legito)  
    Code source de l’application d’inventaire des orgues.

  - [rbc-owl](https://git.inventaire-des-orgues.fr/bzg/rbc-owl)  
    Code source (`rbc-owl.org` et `rbc-owl.clj`) pour la génération d’un
    fichier `.owl` correspondant au référentiel HADOC.

  - [ox-skos](https://git.inventaire-des-orgues.fr/bzg/ox-skos)  
    Code source pour un outil de conversion de fichiers écrits en .org
    vers le format `SKOS` utilisé pour l’import de vocabulaire dans
    [GINCO](https://ginco.culture.fr).

  - [ghislaine](https://git.inventaire-des-orgues.fr/bzg/ghislaine)  
    Code source pour une application de conversion d’un fichier d’export
    Gertrude `.zip` vers un mini-site web présentant les données du
    fichier.

  - [clj-rgf93-wgs84](https://git.inventaire-des-orgues.fr/bzg/clj-rgf93-wgs84)  
    Code source pour une bibliothèque de conversion des coordonnées
    Lambert93 en WGS84.

  - [ido-docs](https://git.inventaire-des-orgues.fr/bzg/ido-docs)  
    Code source des informations disponibles sur le site
    <https://docs.inventaire-des-orgues.fr>

  - [ido-blog](https://git.inventaire-des-orgues.fr/bzg/ido-blog)  
    (Dépôt privé) Code source pour le blog publié sur
    <https://blog.inventaire-des-orgues.fr>

  - [ido-web](https://git.inventaire-des-orgues.fr/bzg/ido-web)  
    (Dépôt privé) Code source pour le site publié sur
    <https://www.inventaire-des-orgues.fr>

# Services web externes

## Services utilisés en dehors du logiciel

  - gandi.net  
    service de location de noms de domaine.

  - digitalocean.com  
    service de location de machines virtuelles.

  - mailchimp.com  
    service pour la collecte d’adresses électroniques, ainsi que la
    rédaction et le suivi de lettres d’information.

  - flipmail.co  
    service pour faire suivre le contenu d’un formulaire web vers une
    adresse email, utilisé sur le site de présentation principal.

  - tawk.to  
    service de discussion en ligne, utilisé sur les sites statiques du
    projet (www/blog/docs).

## Services utilisés par l’application

  - mailgun.com  
    service d’envoi d’emails utilisé par l’application pour les emails
    transactionnels, par exemple lors de la confirmation lors de
    l’inscription d’un utilisateur.

  - filestack.com  
    service d’hébergement de fichiers, utilisé par l’application lorsque
    les contributeurs envoient des fichiers d’images ou autres
    documents.

## Noms de domaine et adresses email utilisées

  - inventaire-des-orgues.fr  
    nom de domaine principal, utilisé pour le portail et les services
    associés. Pas de service mail actif sur ce nom de domaine depuis
    gandi.net. La zone DNS est gérée par les serveurs DNS de
    digitalocean : `ns1.digitalocean.com`. Tous les emails envoyés à
    `@inventaire-des-orgues.fr` sont pour l’instant redirigés vers
    l’adresse du développeur, depuis le service `mailgun.com`.

  - inventaire-des-orgues.org  
    nom de domaine secondaire, utilisé par
    <https://forum.inventaire-des-orgues.fr> pour la passerelle email,
    i.e. la possibilité de répondre par email à un sujet du forum. Deux
    adresses email configurées depuis le compte gandi.net :
    `forum@inventaire-des-orgues.org` utilisée pour le forum, et
    `contact@inventaire-des-orgues.org` utilisée pour flipmail.co et
    l’envoi d’information sur le formulaire du site principal.

## Synthèse des services et coûts associés

| Service          | Coût mensuel (\() | Coût annuel (\)) | Type d’abonnement |
| ---------------- | ------------------------------------ | ----------------- |
| digitalocean.com | 44                                   | 528               |
| filestack.com    | 49                                   | 588               |
| flipmail.co      | 0                                    | 0                 |
| mailchimp.com    | 0                                    | 0                 |
| mailgun.com      | 0                                    | 0                 |
| tawk.to          | 0                                    | 0                 |
| Total            | 93                                   | 1116              |

## Synthèse des étapes nécessaires au tranfert

| Service          | Transfert                                         |
| ---------------- | ------------------------------------------------- |
| gandi.net        | Transfert du nom de domaine                       |
| mailgun.com      | Changement d’adresse de contact et de facturation |
| mailchimp.com    | Changement d’adresse de contact et de facturation |
| digitalocean.com | Changement d’adresse de contact et de facturation |
| filestack.com    | Changement d’adresse de contact et de facturation |

# Domaines, sous-domaines et services associés

| Sous-domaine                      | Service           | Logiciel associé |
| --------------------------------- | ----------------- | ---------------- |
| blog.inventaire-des-orgues.fr     | Blog du projet    | Jekyll           |
| fichiers.inventaire-des-orgues.fr | Fichiers partagés | Nextcloud        |
| forum.inventaire-des-orgues.fr    | Forum             | Discourse        |
| git.inventaire-des-orgues.fr      | Dépôt de code     | gogs             |
| www.inventaire-des-orgues.fr      | Portail du projet | Jekyll           |
