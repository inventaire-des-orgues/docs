# Json public

Pour chaque orgue il est possible d'obtenir un Json en ajoutant `?format=json` à la fin de l'URL publique de la fiche ou
en cliquant sur le lien en bas de page. 
Cette fonctionnalité ne requiert pas d'authentification.

# API : 

Pour pouvoir obtenir des listes de fiches au format JSON il faut suivre les étapes suivantes : 

1. Demander à un administrateur de créer un jeton (token) pour l'utilisateur en question
    ![Extrait admin](./img/jeton_admin.png)
2. Utiliser le token pour faire des requêtes avec n'importe quel langage de programmation.   


### Exemples de requêtes en Python 

**Récupérer les 50 premiers orgues** : 

```python
import requests

headers={'Authorization': 'Token b6d113e8bc1b0f205893bca22e46681b4c2f210c'}
response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",headers=headers)
```


**Récupérer les 50 suivants** : 

```python
import requests

headers={'Authorization': 'Token b6d113e8bc1b0f205893bca22e46681b4c2f210c'}
response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",params={"offset":"50"},headers=headers)
```


**Récupérer les orgues de la Marne** : 

```python
import requests

headers={'Authorization': 'Token b6d113e8bc1b0f205893bca22e46681b4c2f210c'}
response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",params={"code_departement":51},headers=headers)
```
