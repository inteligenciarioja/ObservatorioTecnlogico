# Alojar proyectos Europeos Abiertos en una BBDD MongoDB
# Author: Marcos Cochi
# Date: 31/03/2020
# Fuente de Información: http://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json

import requests
from pymongo import MongoClient
import json

# Inicializamos la conexión con mongodb localhost 
client = MongoClient('localhost',27017)
db = client['Proyectos_Europeos']
collection_calls = db['Calls']
collection_type0 = db['type0']
collection_type1 = db['type1']

# Obtenemos la información de la API

url = "http://ec.europa.eu/info/funding-tenders/opportunities/data/referenceData/grantsTenders.json"
response = requests.get(url)
rjson = response.json()

#print(rjson["fundingData"]["GrantTenderObj"])
# Meter Items en MongoDB
#x = collection_calls.insert_many(rjson["fundingData"]["GrantTenderObj"])
#print(x.inserted_ids)

# Una vez tenemos todos las calls metidas, vamos a ver cómo podemos hacer en vez operaciones de upsert

# Como alterar un campo de un documento existente, o varios valores a la vez
#collection_calls.update_one({'callIdentifier': "EP-PP-CLEAN-STEEL-2019"}, {'$inc': {'cftId': 3}}, True)

# Ahora falta colocarr la BBDD accesible a través de la API
mydoc1 = collection_calls.find({"type": 0})
type1 = collection_type0.insert_many(mydoc1)
mydoc2 = collection_calls.find({"type": 1})
type2 = collection_type1.insert_many(mydoc2)
#for d in mydoc:
#    print(d)

