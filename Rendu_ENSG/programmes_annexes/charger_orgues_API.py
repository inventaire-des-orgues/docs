import requests
import json

"""
Exporte via l'API du site un extrait de la base de données des orgues et l'enregistre sous format json.
"""

autorisation='Token '#A compléter avec la clef fournie par les administrateurs du site. Doit être sous le format autorisation='Token 0123456789'

headers={'Authorization': autorisation}

#Décommenter la ligne souhaitée :

#Charge 50 orgues d'un département
#response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",params={"code_departement":74},headers=headers)

#Charge 50 orgues de la base de données
#response = requests.get("https://inventaire-des-orgues.fr/api/v1/orgues/",headers=headers)


fichier_json=json.loads(response.text)
resultat=fichier_json['results']
with open('orgues1_50.json', 'w') as f:
    json.dump(resultat, f)









