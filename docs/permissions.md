# Permissions

## Portail

Le portail de l'inventaire, réalisé en Python/Django, autorise de nombreux niveaux de permissions.

Ceux retenus à ce jour sont les suivants, par ordre croissant :

### Visiteur

N'importe quel internaute. Permet de visualiser l'ensemble du site et des cartes, à l'exception du commentaire administrateur de chaque fiche.

### Contributeur

A le pouvoir :

- de modifier une fiche pour la compléter, mais pas d'en créer une.

### Créateur

On distingue le rôle de créateur de celui de contributeur car la création d'une nouvelle fiche réclame quelques précautions en ce qui concerne la localisation de l'orgue (il faut par exemple impérativement renseigner le code INSEE de la commune et le nom INSEE de celle-ci).

A le pouvoir :

- de modifier une fiche,
- de créer une fiche pour un nouvel orgue,
- d'ajouter un nouveau type de jeu.

### Administrateur

A le pouvoir :

- de modifier une fiche,
- de créer une fiche pour un nouvel orgue,
- d'ajouter un nouveau type de jeu
- d'ajouter (ou supprimer) un utilisateur et d'en modifier les permissions

## Serveur

### Gestionnaire du serveur

A le pouvoir :

- d'accéder au serveur et d'y exécuter toute manipulation
- de créer des identifiants pour un nouveau gestionnaire du serveur
