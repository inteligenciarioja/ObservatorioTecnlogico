# Transferencia a CODA de Contexto7.py
import csv
from codaio import Coda
import ssl


API_KEY = 'c5d228f1-a38e-4956-b6e6-f6ceaac089d0'
docid="G6ody-h41g"
tabid = "grid-r2hvl_u-eJ"
columnid = "c-JLQHCL5TG3"
columnind = "c-yMpK7A9JuM"
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

coda = Coda(API_KEY)

with open ('Contexto7.csv',mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    for row in csv_reader:
        #print(row)
        payload = {
                        'rows': [
                        {   
                    'cells': [
                        {'column': columnid, 'value': row["id"]},
                        {'column': columnind, 'value':row["TasaParo"]}
                        ],
                        },
                        ],
                    "keyColumns" : [
                        columnid
                        ]
        }
        coda.upsert_row(docid,tabid,payload)
