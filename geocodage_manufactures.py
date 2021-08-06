import json
import requests
import geojson

"""
Geocodage avec api-adresse.data.gouv.
Pour chaque adresse, une liste de points est renvoyée. Ces points sont calculés de manière décroissante par rapport à un score de confiance dans le résultat.
Les latitudes et longitudes sont celles du point ayant le score le plus élevé.
datas.json est le résultat du programme requetes_facteurs.py.
"""


url="https://api-adresse.data.gouv.fr/search/?q="

with open('datas.json') as json_data:
    data_dict = json.load(json_data)
for facteur in data_dict:
    adresseplus=facteur['adresse'].replace(" ", "+")
    res = requests.get(url+adresseplus)
    featureCollection=geojson.loads(res.text)
    point=featureCollection['features'][0]['geometry']['coordinates']
    facteur['latitude']=point[1]
    facteur['longitude']=point[0]

with open('facteurs_localisation.json', 'w') as g:
    json.dump(data_dict, g)
