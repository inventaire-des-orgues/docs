import requests
from bs4 import BeautifulSoup
import json

"""
Scrapping du site Orgue en France avec BeautifulSoup.
Chaque facteur d'orgue se trouve dans une balise p.
Les balises <p> des facteurs d'orgue sont les seules à n'avoir aucun nom de classe et d'id.
A l'intérieur de ces balises <p>, les noms des facteurs sont dans une balise <strong>,
les noms des manufactures sont dans une balise <em>, le téléphone dans <small> et le mail dans <a> lui-même dans <small>.
Si l'information n'est pas connue, renvoie None.
"""

url="https://www.orgue-en-france.org/linstrument/informations-pratiques/annuaire-facteurs-dorgues/"
res = requests.get(url)

html = BeautifulSoup(res.text, 'html.parser')

liste_p = html.find_all('p', class_="", id="")

liste_facteur=[]
for element in liste_p:
    facteur = element.find('strong', class_="", id="")
    if facteur:
        #Cas de Faye, les informations sont séparées en deux balises <p>, .
        facteur=facteur.text.strip()
        manufacture = element.find('em', class_="", id="")
        if manufacture:
            manufacture=manufacture.text.strip()
        adresse=element.text.split("\n")[1]
        telephone=element.find('small', class_="", id="")
        mail=element.find('a', class_="", id="")
        if telephone:
            telephone=telephone.text
            telephone=telephone.replace("Tél.", "").strip()#Suppression de l'en-tête Tél.
            telephone=telephone[:14]#Cas de Fossaert pour lequel le mail est écrit juste après le téléphone
        if mail:
            mail=mail.text.strip()
        if mail==telephone:
            #Comme le mail est parfois dans <small>, il peut être vu comme un téléphone.
            telephone=None

        #dictionnaire={"facteur":facteur, "manufacture":manufacture, "adresse":adresse, "telephone":telephone, "mail":mail, "latitude":None, "longitude":None}
        dictionnaire={"facteur":facteur, "manufacture":manufacture, "adresse":adresse, "latitude":None, "longitude":None}
        liste_facteur.append(dictionnaire)


with open('datas.json', 'w') as f:
    json.dump(liste_facteur, f)