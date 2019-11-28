import feedparser
import ssl
from codaio import Coda
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time
from datetime import datetime, date, time, timedelta


limite = date.today() - timedelta(days = 1)
# Obtener rows de una tabla: ejemplo: https://coda.io/apis/v1beta1/docs/G6ody-h41g/Tables/grid-LOFVqGm0t5/rows
### La tabla en la que quiero insertar las noticias es:
# https://coda.io/apis/v1beta1/docs/G6ody-h41g/Tables/grid-30lv9fOPY1/rows
# DocId: G6ody-h41g
# TableId: grid-30lv9fOPY1


# SACAR URL DE FEEDLY.XML COMO FUENTES

infile = open('feedly.xml', 'r')
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
urlaux = soup.find_all('outline')
listaulr = []
for i in range(0,len(urlaux)) :
    if (len(urlaux[i]) == 0) :
        urlseg = str(urlaux[i]).split("xmlUrl=")
        listaulr.append(urlseg[1].replace("/>",""))

for i in listaulr: 
    print(i)
# LER FUENTES EXTRA DESDE CODA:
# "id": "grid-bkLoQsMy38",
#            "type": "table",
#            "href": "https://coda.io/apis/v1beta1/docs/G6ody-h41g/tables/grid-bkLoQsMy38",
#            "browserLink": "https://coda.io/d/_dG6ody-h41g#_tugrid-bkLoQsMy38",
#            "name": "Fuentes añadidas",
#            "parent": {
#                "id": "canvas-_43PyvtFma",
#                "type": "section",
#                "href": "https://coda.io/apis/v1beta1/docs/G6ody-h41g/sections/canvas-_43PyvtFma",
#                "browserLink": "https://coda.io/d/_dG6ody-h41g/_suFma",
#                "name": "Feed Noticias"
#            }
API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
if hasattr(ssl, '_create_unverified_context'):
	 ssl._create_default_https_context = ssl._create_unverified_context
docid = 'G6ody-h41g'
tabid='grid-bkLoQsMy38'
coda = Coda(API_KEY)
b = coda.list_rows(docid,tabid)

for i in range (0,len(b['items'])):
	aux = '"' + b['items'][i]['values']['c-H6Y2WhxKjs'] + '"'
	listaulr.append(aux)
### La Tabla de la que quiero leer datos es:
print("------------------------------")
for i in listaulr: 
    print(i)

# ESTE SCRIPT RECOGE LAS NOTICIAS DE FEEDLY Y LAS RECOGE EN CODA
API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
#rss = 'https://www.incibe-cert.es/bfeed/avisos-sci/all'
b = float('0.0')
lenlista = len(listaulr)
for rss in listaulr :
    print((b/lenlista)*100)
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    d = feedparser.parse(rss.replace('"','')) #<<WORKS!!
    if (len(d.entries) > 10) :
        ent = 10
    else:
        ent = len(d.entries)
    coda = Coda('c5d228f1-a38e-4956-b6e6-f6ceaac089d0')
    for i in range(0,int(ent)) :
        try:
            payload = {
                  'rows': [
                    {
                      'cells': [
                        {'column': 'c-_zKlSZgEHp', 'value': d.entries[i].title}, {'column': 'c-FaaJIgjDAb', 'value': d.entries[i].link}, 
                      ],
                    },
                  ],
                  "keyColumns" : [
                    "c-_zKlSZgEHp"
                  ]
            }
            print(payload)
            coda.upsert_row('G6ody-h41g','grid-30lv9fOPY1',payload)
        except:
            pass
    b = b+1

