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
tabid="grid-s7f1qkU3ft"
ineurl="http://www.boa.aragon.es/cgi-bin/EBOA/BRSCGI?CMD=RSSLST&DOCS=1-200&BASE=BOLE&SEC=BOARSS&SEPARADOR=&PUBL-C=lafechaxx"
titleid = "c-ocsPoYlMiZ"
summaryid = "c-18AXO60PgC"
interesanteid = "c-kQDxVnTc04"
intwords = ["ingeniero","telecomunicaciones","terapeuta","ocupacional","concurso","oposición"]
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

coda = Coda(API_KEY)
d = feedparser.parse(ineurl)
if (len(d.entries)>10) :
    ent = 8
else :
    ent = len(d.entries)

for i in range (0,len(d.entries)) :
    entries_interesante = "false"
    entries_title = d.entries[i].title
    entries_summary = d.entries[i].link
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
            "keyColumns" : [
                titleid
            ]
    }
    coda.upsert_row(docid,tabid,payload)

