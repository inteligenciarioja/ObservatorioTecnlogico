import feedparser
import ssl
from codaio import Coda
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time
from datetime import datetime, date, time, timedelta

API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
docid="G6ody-h41g"
tabid="grid-wZqn8JWTuU"
ineurl="http://www.ine.es/ss/Satellite?L=es_ES&c=Page&cid=1254735597426&p=1254735566700&pagename=INEHome%2FHOMELayoutRss&param3=rss"
titleid = "c-7mTcT21whJ"
summaryid = "c-GTsOQNPNV0"
interesanteid = "c-PoW_xVOrHJ"
intwords = ["innovación","i+d","alta","tecnología","(tic)","comunicación","biotecnología","comercio electrónico", "tecnologías de la información"]
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

coda = Coda(API_KEY)
d = feedparser.parse(ineurl)
if (len(d.entries)>10) :
    ent = 8
else :
    ent = len(d.entries)

for i in range (0,int(ent)) :
    try:
        entries_interesante = "false"
        entries_title = d.entries[i].title
        entries_summary = d.entries[i].summary
        for c in range (0,len(intwords)) :
            if (str(entries_title).lower().find(intwords[c])>= 0):
                entries_interesante = "true" 
        payload = {
            'rows': [
                {
                    'cells': [
                        {'column': titleid, 'value': entries_title},
                        {'column': summaryid, 'value':entries_summary},
                        {'column': interesanteid, 'value':entries_interesante}
                    ],
                },
            ],
        }
        coda.upsert_row(docid,tabid,payload)
    except:
        pass



